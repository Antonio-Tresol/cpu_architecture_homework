#pragma once

#include <vector>

#include "RAM_Component.hpp"

class RAM {
 public:
  RAM(size_t size);
  std::string read(size_t address) const;
  void write(size_t address, const std::string &value);

 private:
  std::vector<RAM_Component> memory;
  size_t ramSize;
};
