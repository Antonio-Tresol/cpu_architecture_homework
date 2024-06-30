#ifndef RAM_H
#define RAM_H

#include <vector>
#include "RAM_Component.h"

class RAM
{
public:
    RAM(size_t size);
    std::string read(size_t address) const;
    void write(size_t address, const std::string &value);

private:
    std::vector<RAM_Component> memory;
    size_t ramSize;
};

#endif