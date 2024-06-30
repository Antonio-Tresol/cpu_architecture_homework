#include "cache_simulator.h"
#include <iostream>
#include <climits>


RAM ram(1024 * 1024); // 1MB of RAM

string accessRAM(int address) {
    cout << "Accessing RAM at address " << address << endl;
    return ram.read(address);
}


// Constructor implementation
CacheSimulator::CacheSimulator(int cacheSize, int blockSize, int associativity, CacheSimulator *lowerLevel)
    : cacheSize(cacheSize), blockSize(blockSize), associativity(associativity), lowerLevelCache(lowerLevel)
{
    // Calculate the number of sets in the cache
    int numSets = cacheSize / (blockSize * associativity);

    // Initialize the cache structure
    cache.resize(numSets, vector<CacheLine>(associativity));
    for (int i = 0; i < numSets; i++)
    {
        for (int j = 0; j < associativity; j++)
        {
            cache[i][j].valid = false;
            cache[i][j].lastUsedTime = 0;
        }
    }

    // write random memory data to RAM
    for (int i = 0; i < 1024; i++)
    {
        ram.write(i, "Data" + to_string(i));
    }
    
}

// Access function implementation (for now, just a placeholder)
bool CacheSimulator::access(int address)
{
    int setIndex = getSetIndex(address);
    int tag = getTag(address);

    if (searchCache(setIndex, tag))
    {
        cout << "Cache Hit at level " << cacheLevel << "!" << endl;
        return true;
    }
    else
    {
        cout << "Cache Miss at level " << cacheLevel << "!" << endl;

        // If miss, try lower level (if it exists)
        bool hitLowerLevel = false;
        if (lowerLevelCache != nullptr)
        {
            hitLowerLevel = lowerLevelCache->access(address);
        }

        string data = accessRAM(address); // Simulate fetching from RAM
        updateCache(setIndex, tag, data);

        toString();
        return hitLowerLevel;
    }
}

void CacheSimulator::toString()
{
    for (int i = 0; i < cache.size(); i++)
    {
        cout << "Set " << i << ": ";
        for (int j = 0; j < associativity; j++)
        {
            cout << "Tag: " << cache[i][j].tag << " Valid: " << cache[i][j].valid << " Last Used: " << cache[i][j].lastUsedTime << " || ";
            cout << "Data: "; 
            for (auto &d : cache[i][j].data) {
                cout << d << " ";
            }

            cout << " | ";
        }
        cout << endl;
    }

    cout << "level " << cacheLevel << " cache" << endl;
}


int CacheSimulator::getSetIndex(int address)
{
    int numSets = cacheSize / (blockSize * associativity);
    int setIndexBits = log2(numSets);
    return (address >> (int)log2(blockSize)) & ((1 << setIndexBits) - 1);
}

int CacheSimulator::getTag(int address)
{
    int tagBits = 32 - (int)log2(blockSize) - (int)log2(cacheSize / (blockSize * associativity));
    int tag = address >> (32 - tagBits);
    return tag;
}

bool CacheSimulator::searchCache(int setIndex, int tag)
{
    for (int way = 0; way < associativity; ++way)
    {
        if (cache[setIndex][way].valid && cache[setIndex][way].tag == tag)
        {
            cache[setIndex][way].lastUsedTime = currentTime++;
            return true;
        }
    }
    return false;
}

void CacheSimulator::updateCache(int setIndex, int tag, string data)
{
    int lruWay = 0;
    int lruTime = INT_MAX;
    for (int way = 0; way < associativity; ++way)
    {
        if (!cache[setIndex][way].valid)
        {
            lruWay = way;
            break;
        }
        if (cache[setIndex][way].lastUsedTime < lruTime)
        {
            lruTime = cache[setIndex][way].lastUsedTime;
            lruWay = way;
        }
    }

    cache[setIndex][lruWay].tag = tag;
    cache[setIndex][lruWay].valid = true;
    cache[setIndex][lruWay].lastUsedTime = currentTime++;
    cache[setIndex][lruWay].data.push_back(data);
}
