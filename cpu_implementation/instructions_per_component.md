# ALU INT

| Instruction Name | FMT | Opcode | funct3 | funct7 | Description (C)                     | Note                        |
| ---------------- | --- | ------ | ------ | ------ | ---------------------------------- | --------------------------- |
| add              |  R  | 0110011 | 0x0    | 0x00   | rd = rs1 + rs2                       |                             |
| sub              |  R  | 0110011 | 0x0    | 0x20   | rd = rs1 - rs2                       |                             |
| xor              |  R  | 0110011 | 0x4    | 0x00   | rd = rs1 ^ rs2                       |                             |
| or               |  R  | 0110011 | 0x6    | 0x00   | rd = rs1 \| rs2                      |                             |
| and              |  R  | 0110011 | 0x7    | 0x00   | rd = rs1 & rs2                       |                             |
| sll - shift left logical       |  R  | 0110011 | 0x1    | 0x00   | rd = rs1 << rs2                      |                             |
| srl - shift right logical       |  R  | 0110011 | 0x5    | 0x00   | rd = rs1 >> rs2                      |                             |
| sra - shift right arithmetic             |  R  | 0110011 | 0x5    | 0x20   | rd = rs1 >> rs2 (msb-extends)      |                             |
| slt - set less than signed            |  R  | 0110011 | 0x2    | 0x00   | rd = (rs1 < rs2) ? 1 : 0           |                             |
| sltu - set less than unsigned          |  R  | 0110011 | 0x3    | 0x00   | rd = (rs1 < rs2) ? 1 : 0 (zero-extends) |                             |
| addi             |  I  | 0010011 | 0x0    |        | rd = rs1 + imm                       |                             |
| xori             |  I  | 0010011 | 0x4    |        | rd = rs1 ˆ imm                       |                             |
| ori              |  I  | 0010011 | 0x6    |        | rd = rs1 \| imm                      |                             |
| andi             |  I  | 0010011 | 0x7    |        | rd = rs1 & imm                       |                             |
| slli             |  I  | 0010011 | 0x1    |        | imm[5:11]=0x00 rd = rs1 << imm[0:4] |                             |
| srli             |  I  | 0010011 | 0x5    |        | imm[5:11]=0x00 rd = rs1 >> imm[0:4] |                             |
| srai             |  I  | 0010011 | 0x5    |        | imm[5:11]=0x20 rd = rs1 >> imm[0:4] msb-extends |                 |
| slti             |  I  | 0010011 | 0x2    |        | rd = (rs1 < imm)?1:0                 |                             |
| sltiu            |  I  | 0010011 | 0x3    |        | rd = (rs1 < imm)?1:0 zero-extends    |                             |
| mul              |  R  | 0110011 | 0x0    | 0x01   | rd = (rs1 * rs2)[31:0]               |                             |
| mulh             |  R  | 0110011 | 0x1    | 0x01   | rd = (rs1 * rs2)[63:32]              |                             |
| mulsu            |  R  | 0110011 | 0x2    | 0x01   | rd = (rs1 * rs2)[63:32]              |                             |
| mulu             |  R  | 0110011 | 0x3    | 0x01   | rd = (rs1 * rs2)[63:32]              |                             |
| div              |  R  | 0110011 | 0x4    | 0x01   | rd = rs1 / rs2                       |                             |
| divu             |  R  | 0110011 | 0x5    | 0x01   | rd = rs1 / rs2                       |                             |
| rem              |  R  | 0110011 | 0x6    | 0x01   | rd = rs1 % rs2                       |                             |
| remu             |  R  | 0110011 | 0x7    | 0x01   | rd = rs1 % rs2                       |                             |

## Cache? Memory Controller?

| Instruction Name  | FMT | Opcode | funct3 | Description            |
| ---------------- | --- | ------ | ------ | --------------------- |
| lb - load byte                |  I  | 0000011 | 0x0 | rd = M[rs1+imm][0:7] |
| lh - load high                |  I  | 0000011 | 0x1 | rd = M[rs1+imm][0:15] |
| lw - load word               |  I  | 0000011 | 0x2 | rd = M[rs1+imm][0:31] |
| lbu - load byte unsigned               |  I  | 0000011 | 0x4 | rd = M[rs1+imm][0:7] zero-extends |
| lhu - load higher unsigned              |  I  | 0000011 | 0x5 | rd = M[rs1+imm][0:15] zero-extends |
| sb - store byte              |  S  | 0100011 | 0x0 | M[rs1+imm][0:7] = rs2[0:7] |
| sh - store higher               |  S  | 0100011 | 0x1 | M[rs1+imm][0:15] = rs2[0:15] |
| sw - store word              |  S  | 0100011 | 0x2 | M[rs1+imm][0:31] = rs2[0:31] |

## CONTROL UNIT?

| Instruction Name  | FMT | Opcode | funct3 | Description            |
| ---------------- | --- | ------ | ------ | --------------------- |
| beq              |  B  | 1100011 | 0x0 | if(rs1 == rs2) PC += imm |
| bne              |  B  | 1100011 | 0x1 | if(rs1 != rs2) PC += imm |
| blt              |  B  | 1100011 | 0x4 | if(rs1 < rs2) PC += imm |
| bge              |  B  | 1100011 | 0x5 | if(rs1 >= rs2) PC += imm |
| bltu             |  B  | 1100011 | 0x6 | if(rs1 < rs2) PC += imm zero-extends |
| bgeu             |  B  | 1100011 | 0x7 | if(rs1 >= rs2) PC += imm zero-extends |
| jal              |  J  | 1101111 |     | rd = PC+4; PC += imm |
| jalr             |  I  | 1100111 | 0x0 | rd = PC+4; PC = rs1 + imm |
| lui              |  U  | 0110111 |     | rd = imm << 12 |
| auipc            |  U  | 0010111 |     | rd = PC + (imm << 12) |
| ecall            |  I  | 1110011 | 0x0 | imm=0x0 Transfer control to OS |
| ebreak           |  I  | 1110011 | 0x0 | imm=0x1 Transfer control to debugger |
