#include "RAM.h"
#include <iostream>

RAM::RAM(size_t size) : ramSize(size) {
    memory.resize(ramSize); 
}

std::string RAM::read(size_t address) const {
    if (address < ramSize) {
        return memory[address].data;
    } else {
        std::cerr << "RAM Error: Out-of-bounds read at address " << address << std::endl;
        return ""; 
    }
}

void RAM::write(size_t address, const std::string& value) {
    if (address < ramSize) {
        memory[address].data = value;
    } else {
        std::cerr << "RAM Error: Out-of-bounds write at address " << address << std::endl;
    }
}