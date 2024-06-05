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
        binary_encode_rv32i_u_format(parts=["lui", "x1", "0x80000"])
        == "10000000000000000000000000000011"
    )


def test_int_to_binary():
    assert int_to_binary(1) == "000000000001"
    assert int_to_binary(-1) == "111111111111"
    assert int_to_binary(2048) == "100000000000"


def test_get_rs1_from_offset():
    assert get_rs1_from_offset(parts=["sw", "x11", "4(x10)"]) == "x10"


def test_get_immediate_from_offset():
    assert get_immediate_from_offset(parts=["sw", "x11", "4(x10)"]) == "4"
