import pytest
from riscv_assembler import *


def test_binary_encode_rv32i_line_addi():
    assert (
        binary_encode_rv32i_line("addi x5, x5, 1", readable=True)
        == "000000000001 00101 000 00101 0010011"
    )


def test_binary_encode_rv32i_line_add():
    assert (
        binary_encode_rv32i_line("add x10, x5, x6", readable=True)
        == "0000000 00110 00101 000 01010 0110011"
    )


def test_binary_encode_rv32i_line_sw():
    assert (
        binary_encode_rv32i_line("sw x11, 4(x10)", readable=True)
        == "0000000 01011 01010 010 00100 0100011"
    )


def test_binary_encode_rv32i_r_format():
    assert (
        binary_encode_rv32i_r_format(parts=["add", "x10", "x5", "x6"])
        == "0000000 00110 00101 000 01010 0110011"
    )


def test_binary_encode_rv32i_i_format():
    assert (
        binary_encode_rv32i_i_format(parts=["addi", "x5", "x5", "1"])
        == "000000000001 00101 000 00101 0010011"
    )


def test_binary_encode_rv32i_i_format_with_offset():
    assert (
        binary_encode_rv32i_i_format(parts=["lw", "x11", "4(x10)"])
        == "000000000100 01010 010 01011 0000011"
    )


def test_binary_encode_rv32i_s_format():
    assert (
        binary_encode_rv32i_s_format(parts=["sw", "x11", "4(x10)"])
        == "0000000 01011 01010 010 00100 0100011"
    )


def test_binary_encode_rv32i_u_format():
    assert (
        binary_encode_rv32i_u_format(parts=["lui", "x1", "524288"])
        == "10000000000000000000 00001 0110111"
    )


def test_binary_encode_rv32i_b_format():
    assert (
        binary_encode_rv32i_b_format(parts=["beq", "x4", "x5", "0"])
        == "0 000000 00101 00100 000 00000 1100011"
    )


def test_int_to_binary():
    assert int_to_binary(1) == "000000000001"
    assert int_to_binary(-1) == "111111111111"
    assert int_to_binary(2048) == "100000000000"


def test_get_rs1_from_offset():
    assert get_rs1_from_offset(parts=["sw", "x11", "4(x10)"]) == "x10"


def test_get_immediate_from_offset():
    assert get_immediate_from_offset(parts=["sw", "x11", "4(x10)"]) == "4"


def test_binary_encode_rv32i_line_jal():
    # Assuming imm is a multiple of 2 and encoded as a 21-bit signed offset
    assert (
        binary_encode_rv32i_line("jal x1, 2", readable=True)
        == "0 0000000001 0 00000000 00001 1101111"
    )


def test_binary_encode_rv32i_line_lui():
    assert (
        binary_encode_rv32i_line("lui x1, -3", readable=True)
        == "11111111111111111101 00001 0110111"
    )


def test_binary_encode_rv32i_line_auipc():
    assert (
        binary_encode_rv32i_line("auipc x1, 3", readable=True)
        == "00000000000000000011 00001 0010111"
    )


def test_binary_encode_rv32i_line_jalr():
    assert (
        binary_encode_rv32i_line("jalr x1, 4(x2)", readable=True)
        == "000000000100 00010 000 00001 1100111"
    )


def test_binary_encode_rv32i_line_bne():
    assert (
        binary_encode_rv32i_line("bne x1, x2, 4", readable=True)
        == "0 000000 00010 00001 001 00100 1100011"
    )


def test_binary_encode_rv32i_line_blt():
    assert (  # 4 = 0000 0000 0100 -> -4 = 1111 1111 1100
        binary_encode_rv32i_line("blt x1, x2, -4", readable=True)
        == "1 111111 00010 00001 100 11101 1100011"
    )


def test_binary_encode_rv32i_line_bge():
    assert (
        binary_encode_rv32i_line("bge x1, x2, 4", readable=True)
        == "0 000000 00010 00001 101 00100 1100011"
    )


def test_binary_encode_rv32i_line_bltu():
    assert (
        binary_encode_rv32i_line("bltu x1, x2, 4", readable=True)
        == "0 000000 00010 00001 110 00100 1100011"
    )


def test_binary_encode_rv32i_line_bgeu():
    assert (
        binary_encode_rv32i_line("bgeu x1, x2, 4", readable=True)
        == "0 000000 00010 00001 111 00100 1100011"
    )


def test_binary_encode_rv32i_line_lb():
    assert (
        binary_encode_rv32i_line("lb x1, -1(x2)", readable=True)
        == "111111111111 00010 000 00001 0000011"
    )


def test_binary_encode_rv32i_line_lh():
    assert (
        binary_encode_rv32i_line("lh x1, -1(x3)", readable=True)
        == "111111111111 00011 001 00001 0000011"
    )


def test_binary_encode_rv32i_line_lw():
    assert (
        binary_encode_rv32i_line("lw x1, 10(fp)", readable=True)
        == "000000001010 01000 010 00001 0000011"
    )


def test_binary_encode_rv32i_line_lbu():
    assert (
        binary_encode_rv32i_line("lbu x1, 0(x2)", readable=True)
        == "000000000000 00010 100 00001 0000011"
    )


def test_binary_encode_rv32i_line_lhu():
    assert (
        binary_encode_rv32i_line("lhu x1, 0(x2)", readable=True)
        == "000000000000 00010 101 00001 0000011"
    )


def test_binary_encode_rv32i_line_sb():
    assert (
        binary_encode_rv32i_line("sb x1, 0(x2)", readable=True)
        == "0000000 00001 00010 000 00000 0100011"
    )


def test_binary_encode_rv32i_line_sh():
    assert (
        binary_encode_rv32i_line("sh x1, 0(x2)", readable=True)
        == "0000000 00001 00010 001 00000 0100011"
    )


def test_binary_encode_rv32i_line_sw():
    assert (
        binary_encode_rv32i_line("sw x1, 0(x2)", readable=True)
        == "0000000 00001 00010 010 00000 0100011"
    )


def test_binary_encode_rv32i_line_slti():
    assert (
        binary_encode_rv32i_line("slti x1, x2, 1", readable=True)
        == "000000000001 00010 010 00001 0010011"
    )


def test_binary_encode_rv32i_line_sltiu():
    assert (
        binary_encode_rv32i_line("sltiu x1, x2, 2", readable=True)
        == "000000000010 00010 011 00001 0010011"
    )


def test_binary_encode_rv32i_line_xori():
    assert (
        binary_encode_rv32i_line("xori x1, x2, -1", readable=True)
        == "111111111111 00010 100 00001 0010011"
    )


def test_binary_encode_rv32i_line_ori():
    assert (
        binary_encode_rv32i_line("ori x1, x2, 7", readable=True)
        == "000000000111 00010 110 00001 0010011"
    )


def test_binary_encode_rv32i_line_andi():
    assert (
        binary_encode_rv32i_line("andi x1, x2, 1", readable=True)
        == "000000000001 00010 111 00001 0010011"
    )


def test_binary_encode_rv32i_line_slli():
    assert (
        binary_encode_rv32i_line("slli x1, x2, 1", readable=True)
        == "000000000001 00010 001 00001 0010011"
    )


def test_binary_encode_rv32i_line_srli():
    assert (
        binary_encode_rv32i_line("srli x1, x2, 1", readable=True)
        == "000000000001 00010 101 00001 0010011"
    )


def test_binary_encode_rv32i_line_srai():
    assert (
        binary_encode_rv32i_line("srai x1, x2, -1", readable=True)
        == "111111111111 00010 101 00001 0010011"
    )


def test_binary_encode_rv32i_line_sub():
    assert (
        binary_encode_rv32i_line("sub x1, x2, x3", readable=True)
        == "0100000 00011 00010 000 00001 0110011"
    )


def test_binary_encode_rv32i_line_sll():
    assert (
        binary_encode_rv32i_line("sll x1, x2, x3", readable=True)
        == "0000000 00011 00010 001 00001 0110011"
    )


def test_binary_encode_rv32i_line_slt():
    assert (
        binary_encode_rv32i_line("slt x1, x2, x3", readable=True)
        == "0000000 00011 00010 010 00001 0110011"
    )


def test_binary_encode_rv32i_line_sltu():
    assert (
        binary_encode_rv32i_line("sltu x1, x2, x3", readable=True)
        == "0000000 00011 00010 011 00001 0110011"
    )


def test_binary_encode_rv32i_line_xor():
    assert (
        binary_encode_rv32i_line("xor x1, x2, x3", readable=True)
        == "0000000 00011 00010 100 00001 0110011"
    )


def test_binary_encode_rv32i_line_srl():
    assert (
        binary_encode_rv32i_line("srl x1, x2, x3", readable=True)
        == "0000000 00011 00010 101 00001 0110011"
    )


def test_binary_encode_rv32i_line_sra():
    assert (
        binary_encode_rv32i_line("sra x1, x2, x3", readable=True)
        == "0100000 00011 00010 101 00001 0110011"
    )


def test_binary_encode_rv32i_line_or():
    assert (
        binary_encode_rv32i_line("or x1, x2, x3", readable=True)
        == "0000000 00011 00010 110 00001 0110011"
    )


def test_binary_encode_rv32i_line_and():
    assert (
        binary_encode_rv32i_line("and x1, x2, x3", readable=True)
        == "0000000 00011 00010 111 00001 0110011"
    )


def test_int_to_binary():
    assert int_to_binary(1) == "000000000001"
