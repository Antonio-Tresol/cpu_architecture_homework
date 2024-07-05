#include <iostream>

#include "cache_simulator.hpp"

int main() {
  // Create L2 cache
  CacheSimulator l2Cache(2 * 1024, 64, 2);
  l2Cache.cacheLevel = 2;

  // Create L1 cache
  CacheSimulator l1Cache(1 * 1024, 64, 2, &l2Cache);

  // 1. Force RAM Accesses (Cold Misses):
  cout << "---- Forcing RAM Accesses (Cold Misses) ----" << endl;
  for (int i = 0; i < 5; ++i) {
    l2Cache.access(i * 64);
  }

  cout << "\n---- Forcing L2 Hits ----" << endl;
  for (int i = 0; i < 2; ++i) {
    l1Cache.access(i * 64);
  }

  cout << "\n---- Forcing L1 hits ----" << endl;
  for (int i = 0; i < 2; ++i) {
    l1Cache.access(i * 64);
  }

  return 0;
}