from typing import List
import re
from rv32f_maps import (
    RV32F_FUNCT3_MAP,
    RV32F_INSTRUCTION_INFO_MAP,
    RV32F_FUNCT5_MAP,
    RV32F_FUNCT7_MAP,
    ABI_FLOAT_REGISTER_TO_BINARY_MAP,
)
from rv32i_maps import ABI_INT_REGISTER_TO_BINARY_MAP


def binary_encode_rv32f_line(instruction: str, readable: bool = False) -> str:
    """Encodes a given RISC-V floating-point instruction into its 32-bit binary representation.

    This function takes a single RISC-V 32-bit instruction in assembly format
    and returns its binary representation. It supports I, R, and S formats.

    Parameters
    ----------
    instruction : str
        The RISC-V 32-bit instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.
        Returns "nop" if the instruction is not found or an error occurs.

    Examples
    --------

    """
    parts = [part.rstrip(",").lower() for part in instruction.split(" ")]
    opcode = parts[0]
    format = RV32F_INSTRUCTION_INFO_MAP.get(opcode)["format"]
    encoding = ""
    if opcode == "L":
        encoding = binary_encode_rv32f_l_format(parts=parts)
    elif opcode == "S":
        encoding = binary_encode_rv32f_s_format(parts=parts)
    elif opcode == "FMA":
        encoding = binary_encode_rv32f_fma_format(parts=parts)
    elif format == "R":
        encoding = binary_encode_rv32f_r_format(parts=parts)
    elif format == "N":
        encoding = binary_encode_rv32f_n_format(parts=parts)
    elif format == "FC":
        encoding = binary_encode_rv32f_fc_format(parts=parts)
    elif format == "FM":
        encoding = binary_encode_rv32f_fm_format(parts=parts)
    elif format == "C":
        encoding = binary_encode_rv32f_c_format(parts=parts)
    elif format == "FCL":
        encoding = binary_encode_rv32f_fcl_format(parts=parts)
    if not readable:
        encoding = encoding.replace(" ", "")
    return encoding


def binary_encode_rv32f_fma_format(parts: List[str]) -> str:
    """Encodes a FMA-format (fused multiply-add) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.
    """
    return ""


def binary_encode_rv32f_l_format(parts: List[str]) -> str:
    """Encodes a L-format (load) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_s_format(parts: List[str]) -> str:
    """Encodes a S-format (store) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_r_format(parts: List[str]) -> str:
    """Encodes an R-format (register-register format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_n_format(parts: List[str]) -> str:
    """Encodes an N-format (Inject format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_fc_format(parts: List[str]) -> str:
    """Encodes an FC-format (float convert format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_fm_format(parts: List[str]) -> str:
    """Encodes an FM-format (floating move format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_c_format(parts: List[str]) -> str:
    """Encodes a C-format (compare format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""


def binary_encode_rv32f_fcl_format(parts: List[str]) -> str:
    """Encodes a FCL-format (float class format) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The parts of the RISC-V instruction in assembly format.

    Returns
    -------
    str
        The 32-bit binary representation of the instruction.

    """
    return ""
