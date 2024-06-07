INSTRUCTION_INFO_MAP = {
    "lui": {  # check
        "format": "U",
        "opcode": "0110111",
    },
    "auipc": {  # check
        "format": "U",
        "opcode": "0010111",
    },
    "jal": {  # check
        "format": "J",
        "opcode": "1101111",
    },
    "jalr": {  # check
        "format": "I",
        "opcode": "1100111",
    },
    "beq": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "bne": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "blt": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "bge": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "bltu": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "bgeu": {  # check
        "format": "B",
        "opcode": "1100011",
    },
    "lb": {  # check
        "format": "I",
        "opcode": "0000011",
    },
    "lh": {  # check
        "format": "I",
        "opcode": "0000011",
    },
    "lw": {  # check
        "format": "I",
        "opcode": "0000011",
    },
    "lbu": {  # check
        "format": "I",
        "opcode": "0000011",
    },
    "lhu": {  # check
        "format": "I",
        "opcode": "0000011",
    },
    "sb": {  # check
        "format": "S",
        "opcode": "0100011",
    },
    "sh": {  # check
        "format": "S",
        "opcode": "0100011",
    },
    "sw": {  # check
        "format": "S",
        "opcode": "0100011",
    },
    "addi": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "slti": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "sltiu": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "xori": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "ori": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "andi": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "slli": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "srli": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "srai": {  # check
        "format": "I",
        "opcode": "0010011",
    },
    "add": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "sub": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "sll": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "slt": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "sltu": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "xor": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "srl": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "sra": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "or": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "and": {  # check
        "format": "R",
        "opcode": "0110011",
    },
    "fence": {  # check
        "format": "I",
        "opcode": "0001111",
    },
    "ecall": {  # check
        "format": "I",
        "opcode": "1110011",
    },
    "ebreak": {  # check
        "format": "I",
        "opcode": "1110011",
    },
    "mul": {
        "format": "R",
        "opcode": "0110011",
    },
    "mulh": {
        "format": "R",
        "opcode": "0110011",
    },
    "mulhsu": {
        "format": "R",
        "opcode": "0110011",
    },
    "mulhu": {
        "format": "R",
        "opcode": "0110011",
    },
    "div": {
        "format": "R",
        "opcode": "0110011",
    },
    "divu": {
        "format": "R",
        "opcode": "0110011",
    },
    "rem": {
        "format": "R",
        "opcode": "0110011",
    },
    "remu": {
        "format": "R",
        "opcode": "0110011",
    },
}

FUNCT_3_MAP = {
    "jalr": "000",  # check
    "beq": "000",  # check
    "bne": "001",  # check
    "blt": "100",  # check
    "bge": "101",  # check
    "bltu": "110",  # check
    "bgeu": "111",  # check
    "lb": "000",  # check
    "lh": "001",  # check
    "lw": "010",  # check
    "lbu": "100",  # check
    "lhu": "101",  # check
    "sb": "000",  # check
    "sh": "001",  # check
    "sw": "010",  # check
    "addi": "000",  # check
    "slti": "010",  # check
    "sltiu": "011",  # check
    "xori": "100",  # check
    "ori": "110",  # check
    "andi": "111",  # check
    "slli": "001",  # check
    "srli": "101",  # check
    "srai": "101",  # check
    "add": "000",  # check
    "sub": "000",  # check
    "sll": "001",  # check
    "slt": "010",  # check
    "sltu": "011",  # check
    "xor": "100",  # check
    "srl": "101",  # check
    "sra": "101",  # check
    "or": "110",  # check
    "and": "111",  # check
    "fence": "000",  # check
    "ecall": "000",  # check
    "ebreak": "000",  # check
    "mul": "000",
    "mulh": "001",
    "mulhsu": "010",
    "mulhu": "011",
    "div": "100",
    "divu": "101",
    "rem": "110",
    "remu": "111",
}

FUNCT_7_MAP = {  # check
    "slli": "0000000",
    "srli": "0000000",
    "srai": "0100000",
    "add": "0000000",
    "sub": "0100000",
    "sll": "0000000",
    "slt": "0000000",
    "sltu": "0000000",
    "xor": "0000000",
    "srl": "0000000",
    "sra": "0100000",
    "or": "0000000",
    "and": "0000000",
    "mul": "0000001",
    "mulh": "0000001",
    "mulhsu": "0000001",
    "mulhu": "0000001",
    "div": "0000001",
    "divu": "0000001",
    "rem": "0000001",
    "remu": "0000001",
}

ABI_INT_REGISTER_TO_BINARY_MAP = {
    "zero": "00000",
    "ra": "00001",
    "sp": "00010",
    "gp": "00011",
    "tp": "00100",
    "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "fp": "01000",
    "s1": "01001",
    "a0": "01010",
    "a1": "01011",
    "a2": "01100",
    "a3": "01101",
    "a4": "01110",
    "a5": "01111",
    "a6": "10000",
    "a7": "10001",
    "s2": "10010",
    "s3": "10011",
    "s4": "10100",
    "s5": "10101",
    "s6": "10110",
    "s7": "10111",
    "s8": "11000",
    "s9": "11001",
    "s10": "11010",
    "s11": "11011",
    "t3": "11100",
    "t4": "11101",
    "t5": "11110",
    "t6": "11111",
    # Identity mappings
    "x0": "00000",
    "x1": "00001",
    "x2": "00010",
    "x3": "00011",
    "x4": "00100",
    "x5": "00101",
    "x6": "00110",
    "x7": "00111",
    "x8": "01000",
    "x9": "01001",
    "x10": "01010",
    "x11": "01011",
    "x12": "01100",
    "x13": "01101",
    "x14": "01110",
    "x15": "01111",
    "x16": "10000",
    "x17": "10001",
    "x18": "10010",
    "x19": "10011",
    "x20": "10100",
    "x21": "10101",
    "x22": "10110",
    "x23": "10111",
    "x24": "11000",
    "x25": "11001",
    "x26": "11010",
    "x27": "11011",
    "x28": "11100",
    "x29": "11101",
    "x30": "11110",
    "x31": "11111",
}
