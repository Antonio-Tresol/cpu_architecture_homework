#include <iostream>

#include "cache_simulator.hpp"
#include "RAM.hpp"

int main() {
  // Create L2 cache (Write-Back)
  CacheSimulator l2Cache(2 * 1024, 64, 2, nullptr,
                        WritePolicy::WRITE_BACK);
  l2Cache.cacheLevel = 2;

  // Create L1 cache (Write-Through)
  CacheSimulator l1Cache(1 * 1024, 64, 2, &l2Cache,
                        WritePolicy::WRITE_THROUGH);

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

  cout << "\n---- Write to L1 (Write-Through) ----" << endl;
  l1Cache.access(0, true);  // Write to address 0

  cout << "\n---- Read from L1 after write ----" << endl;
  l1Cache.access(0); 

  l1Cache.displayRAM();  
  return 0;
}