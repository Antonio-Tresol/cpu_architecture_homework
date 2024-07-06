#include "cache_simulator.hpp"

#include <climits>
#include <iomanip>
#include <iostream>

RAM ram(1024 * 1024);  // 1MB of RAM

string accessRAM(int address) {
  cout << "Accessing RAM at address " << address << endl;
  return ram.read(address);
}

// Constructor implementation
CacheSimulator::CacheSimulator(int cacheSize, int blockSize, int associativity,
                               CacheSimulator* lowerLevel,
                               WritePolicy writePolicy)
    : cacheSize(cacheSize),
      blockSize(blockSize),
      associativity(associativity),
      lowerLevelCache(lowerLevel),
      writePolicy(writePolicy) {
  // Calculate the number of sets in the cache
  int numSets = cacheSize / (blockSize * associativity);

  // Initialize the cache structure
  cache.resize(numSets, vector<CacheLine>(associativity));
  for (int i = 0; i < numSets; i++) {
    for (int j = 0; j < associativity; j++) {
      cache[i][j].valid = false;
      cache[i][j].dirty = false;
      cache[i][j].lastUsedTime = 0;
    }
  }

  // write random memory data to RAM
  for (int i = 0; i < 1024; i++) {
    ram.write(i, to_string(i));
  }
}

// Access function implementation
bool CacheSimulator::access(int address, bool isWrite) {
  int setIndex = getSetIndex(address);
  int tag = getTag(address);

  if (searchCache(setIndex, tag)) {
    cout << "Cache Hit at level " << cacheLevel << "!" << endl;
    if (isWrite) {
      handleWrite(setIndex, tag, "sadaa"); 
    }
    return true;
  } else {
    cout << "Cache Miss at level " << cacheLevel << "!" << endl;

    // If miss, try lower level (if it exists)
    bool hitLowerLevel = false;
    if (lowerLevelCache != nullptr) {
      hitLowerLevel = lowerLevelCache->access(address, isWrite);
    }

    string data = accessRAM(address);  // Simulate fetching from RAM
    updateCache(setIndex, tag, data);

    if (isWrite) {
      handleWrite(setIndex, tag, "assad");
    }

    displayCache();
    return hitLowerLevel;
  }
}

void CacheSimulator::handleWrite(int setIndex, int tag, string data) {
  for (int way = 0; way < associativity; ++way) {
    if (cache[setIndex][way].valid && cache[setIndex][way].tag == tag) {
      if (writePolicy == WritePolicy::WRITE_BACK) {
        cache[setIndex][way].dirty = true;  
      } else if (writePolicy == WritePolicy::WRITE_THROUGH) {
        ram.write(getAddressFromTagSet(tag, setIndex), data); 
      }
      break; 
    }
  }
}


void CacheSimulator::printHeaders() const {
  printSeparatorLine();
  cout << "Cache Level " << cacheLevel << ":\n";
  cout << left << setw(8) << "Set" << setw(12) << "Tag" << setw(8) << "Valid"
       << setw(6) << "Dirty" << setw(12) << "Last Used" << setw(20) << "Data"
       << endl;
  printSeparatorLine();
}

void CacheSimulator::printCacheLine(size_t setIndex, int lineIndex) const {
  // Print set number only once per row, then align other columns
  cout << left << setw(8) << (lineIndex == 0 ? to_string(setIndex) : "")
       << setw(12) << cache[setIndex][lineIndex].tag << setw(8)
       << cache[setIndex][lineIndex].valid << setw(6)
       << cache[setIndex][lineIndex].dirty << setw(12)
       << cache[setIndex][lineIndex].lastUsedTime << setw(20);

  if (cache[setIndex][lineIndex].data.empty()) {
    cout << "Empty";
  } else {
    for (const auto& d : cache[setIndex][lineIndex].data) {
      cout << d << " ";
    }
  }
  cout << endl;
}

void CacheSimulator::printSeparatorLine() const {
  cout << string(70, '-') << endl;
}

void CacheSimulator::displayCache() {
  printHeaders();
  for (std::size_t i = 0; i < cache.size(); i++) {
    for (int j = 0; j < associativity; j++) {
      printCacheLine(i, j);
    }
    printSeparatorLine();
  }
}

int CacheSimulator::getSetIndex(int address) {
  int numSets = cacheSize / (blockSize * associativity);
  int setIndexBits = log2(numSets);
  return (address >> (int)log2(blockSize)) & ((1 << setIndexBits) - 1);
}

int CacheSimulator::getTag(int address) {
  int tagBits = 32 - (int)log2(blockSize) -
                (int)log2(cacheSize / (blockSize * associativity));
  int tag = address >> (32 - tagBits);
  return tag;
}

bool CacheSimulator::searchCache(int setIndex, int tag) {
  for (int way = 0; way < associativity; ++way) {
    if (cache[setIndex][way].valid && cache[setIndex][way].tag == tag) {
      cache[setIndex][way].lastUsedTime = currentTime++;
      return true;
    }
  }
  return false;
}

// Function to get the full address from tag and set index
int CacheSimulator::getAddressFromTagSet(int tag, int setIndex) {
  int tagBits = 32 - (int)log2(blockSize) -
                (int)log2(cacheSize / (blockSize * associativity));
  int setIndexBits = log2(cacheSize / (blockSize * associativity));

  int address = (tag << (setIndexBits + (int)log2(blockSize))) |
               (setIndex << (int)log2(blockSize));
  return address;
}

void CacheSimulator::updateCache(int setIndex, int tag, string data) {
  int lruWay = 0;
  int lruTime = INT_MAX;
  for (int way = 0; way < associativity; ++way) {
    if (!cache[setIndex][way].valid) {
      lruWay = way;
      break;
    }
    if (cache[setIndex][way].lastUsedTime < lruTime) {
      lruTime = cache[setIndex][way].lastUsedTime;
      lruWay = way;
    }
  }

  // If the cache line is dirty, write back to lower level/RAM
  if (cache[setIndex][lruWay].dirty) {
    int addressToWriteBack =
        getAddressFromTagSet(cache[setIndex][lruWay].tag, setIndex);
    if (lowerLevelCache != nullptr) {
      lowerLevelCache->access(addressToWriteBack, true);  // Write to lower
                                                        // level
    } else {
      ram.write(addressToWriteBack,
                 cache[setIndex][lruWay].data.front()); 
    }
  }

  cache[setIndex][lruWay].tag = tag;
  cache[setIndex][lruWay].valid = true;
  cache[setIndex][lruWay].dirty = false;  
  cache[setIndex][lruWay].lastUsedTime = currentTime++;
  cache[setIndex][lruWay].data.clear(); 
  cache[setIndex][lruWay].data.push_back(data);
}

void CacheSimulator::displayRAM() { ram.printRAM(); }