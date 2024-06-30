#ifndef CACHE_SIMULATOR_H
#define CACHE_SIMULATOR_H

#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>

#include "RAM.h" // Include RAM.h

using namespace std;

struct CacheLine
{
    int tag;
    bool valid;
    int lastUsedTime;
    vector<string> data;
};

class CacheSimulator
{
public:
    CacheSimulator(int cacheSize, int blockSize, int associativity, CacheSimulator *lowerLevel = nullptr);
    bool access(int address);
    void toString();

    int cacheLevel = 1;

private:
    int cacheSize;
    int blockSize;
    int associativity;

    vector<vector<CacheLine>> cache;

    int currentTime = 0;
    CacheSimulator *lowerLevelCache = nullptr;

    int getSetIndex(int address);

    int getTag(int address);

    bool searchCache(int setIndex, int tag);

    void updateCache(int setIndex, int tag, string data);
};

#endif