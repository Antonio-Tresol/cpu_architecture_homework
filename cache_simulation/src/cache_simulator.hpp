#pragma once

#include <cmath>
#include <list>
#include <unordered_map>
#include <vector>

#include "RAM.hpp"  // Include RAM.h

using namespace std;

enum class WritePolicy { WRITE_THROUGH, WRITE_BACK };

struct CacheLine {
  int tag;
  bool valid;
  bool dirty;
  int lastUsedTime;
  vector<string> data;
};

class CacheSimulator {
 public:
  CacheSimulator(int cacheSize, int blockSize, int associativity,
                 CacheSimulator* lowerLevel = nullptr,
                 WritePolicy writePolicy = WritePolicy::WRITE_BACK); 
  bool access(int address, bool isWrite = false);
  void displayCache();
  void displayRAM();

  int cacheLevel = 1;

 private:
  int cacheSize;
  int blockSize;
  int associativity;
  WritePolicy writePolicy;

  vector<vector<CacheLine>> cache;

  int currentTime = 0;
  CacheSimulator* lowerLevelCache = nullptr;

  int getSetIndex(int address);

  int getTag(int address);

  bool searchCache(int setIndex, int tag);

  void updateCache(int setIndex, int tag, string data);

  void handleWrite(int setIndex, int tag, string data);
  int getAddressFromTagSet(int tag, int setIndex); 

  void printHeaders() const;
  void printCacheLine(size_t i, int j) const;
  void printSeparatorLine() const;
};