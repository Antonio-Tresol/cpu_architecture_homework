from typing import List
import re
import riscv32_im_maps as rv32_im_maps


def binary_encode_rv32i_line(
    instruction: str, readable: bool = False, verbose: bool = False
) -> str:
    """Encodes a given RISC-V interger E instruction into its 32-bit binary representation.

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
    >>> binary_encode_rv32i_line("addi x5, x5, 1")
    '00000000000101010010001010010011'

    >>> binary_encode_rv32i_line("add x10, x5, x6")
    '00000000101000101010000110011011'

    >>> binary_encode_rv32i_line("sw x11, 4(x10)")
    '00000000010110101000010100100011'
    """
    parts = [part.rstrip(",").rstrip("\n").lower() for part in instruction.split(" ")]
    opcode = parts[0]
    format = rv32_im_maps.INSTRUCTION_INFO_MAP.get(opcode)["format"]
    encoding = ""
    if format == "I":
        encoding = binary_encode_rv32i_i_format(parts=parts)
    elif format == "R":
        encoding = binary_encode_rv32i_r_format(parts=parts)
    elif format == "S":
        encoding = binary_encode_rv32i_s_format(parts=parts)
    elif format == "U":
        encoding = binary_encode_rv32i_u_format(parts=parts)
    elif format == "B":
        encoding = binary_encode_rv32i_b_format(parts=parts)
    elif format == "J":
        encoding = binary_encode_rv32i_j_format(parts=parts)
    if not readable:
        encoding = encoding.replace(" ", "")
    if verbose:
        print(f"final encoding for {parts}: {encoding}")
    return encoding


def binary_encode_rv32i_b_format(parts: List[str]) -> str:
    """Encodes a B-format (branch) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The 32-bit binary representation of the B-format instruction.

    """
    instruction = parts[0]
    rs1 = parts[1]
    rs2 = parts[2]
    imm = parts[3]

    print(parts)

    opcode = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rs1_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs1)
    rs2_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs2)
    funct3 = rv32_im_maps.FUNCT_3_MAP.get(instruction)
    imm_encoding = int_to_binary(imm, 13)  # 0 0 000000 00011
    print("imm encoding ", imm_encoding)
    print("opcode ", opcode)
    print("rs1 ", rs1_encoding)
    print("rs2 encoding ", rs2_encoding)
    print("funct3 ", funct3)
    result = f"{imm_encoding[0]} {imm_encoding[2:8]} {rs2_encoding} {rs1_encoding} {funct3} {imm_encoding[8:12]}{imm_encoding[1]} {opcode}"
    print("result ", result)
    return result


def binary_encode_rv32i_j_format(parts: List[str]) -> str:
    """Encodes a J-format (jump) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The 32-bit binary representation of the J-format instruction.

    """
    instruction = parts[0]
    rd = parts[1]
    imm = parts[2]

    opcode = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rd_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rd)
    # imm_encoding = int_to_binary(imm, 21)  # imm[20|10:1|11|19:12]
    imm_encoding = int_to_binary(imm, 21)
    print(imm_encoding)
    return f"{imm_encoding[0]} {imm_encoding[10:20]} {imm_encoding[9]} {imm_encoding[1:9]} {rd_encoding} {opcode}"


def binary_encode_rv32i_u_format(parts: List[str]) -> str:

    instruction = parts[0]
    rd = parts[1]
    imm = parts[2]

    opcode = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rd_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rd)
    imm_encoding = int_to_binary(imm, 20)

    return f"{imm_encoding} {rd_encoding} {opcode}"


def binary_encode_rv32i_r_format(parts: List[str]) -> str:
    """Encodes an R-format (register-register) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The 32-bit binary representation of the R-format instruction.

    """

    instruction = parts[0]
    rd = parts[1]
    rs1 = parts[2]
    rs2 = parts[3]

    opcode = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rd_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rd)
    rs1_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs1)
    rs2_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs2)

    funct3 = rv32_im_maps.FUNCT_3_MAP.get(instruction)
    funct7 = rv32_im_maps.FUNCT_7_MAP.get(instruction)

    return f"{funct7} {rs2_encoding} {rs1_encoding} {funct3} {rd_encoding} {opcode}"


def binary_encode_rv32i_s_format(parts: List[str]) -> str:
    """Encodes an S-format (store) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The 32-bit binary representation of the S-format instruction.

    """
    instruction = parts[0]
    rs2 = parts[1]
    rs1 = get_rs1_from_offset(parts)
    imm = get_immediate_from_offset(parts)

    opcode = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rs2_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs2)
    rs1_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs1)
    funct3 = rv32_im_maps.FUNCT_3_MAP.get(instruction)
    imm_encoding = int_to_binary(imm)

    print(imm_encoding)
    return f"{imm_encoding[0:7]} {rs2_encoding} {rs1_encoding} {funct3} {imm_encoding[7:12]} {opcode}"


def binary_encode_rv32i_i_format(parts: List[str]) -> str:
    """Encodes an I-format (immediate) RISC-V instruction.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The 32-bit binary representation of the I-format instruction.

    """

    instruction = parts[0]
    rd = parts[1]
    rs1 = 0
    imm = 0
    if is_i_format_with_offset(parts):
        rs1 = get_rs1_from_offset(parts)
        imm = get_immediate_from_offset(parts)
    else:
        rs1 = parts[2]
        imm = parts[3]
    instruction_encoding = rv32_im_maps.INSTRUCTION_INFO_MAP.get(instruction)["opcode"]
    rd_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rd)
    rs1_encoding = rv32_im_maps.ABI_INT_REGISTER_TO_BINARY_MAP.get(rs1)
    funct3_encoding = rv32_im_maps.FUNCT_3_MAP.get(instruction)
    imm_encoding = int_to_binary(imm)
    i_instructions_encoding = f"{imm_encoding} {rs1_encoding} {funct3_encoding} {rd_encoding} {instruction_encoding}"
    return i_instructions_encoding


def int_to_binary(imm, n_bits=12) -> str:
    """Converts an integer to its n_bits-bit binary representation.

    Parameters
    ----------
    imm : int
        The integer to convert.
    n_bits : int, optional
        The number of bits in the binary representation (default is 12).

    Returns
    -------
    str
        The n_bits-bit binary representation of the integer.

    """
    result = int(imm)
    if result < 0:
        result = bin(result & ((1 << n_bits) - 1))[2:]
    else:
        result = bin(result)[2:].zfill(n_bits)
    return result


regex_find_rs1_from_offset = r"(?<=\()(zero|ra|gp|sp|fp|[xs]{1}[0-9]{1,2})(?=\))"

regex_find_imm_from_offset = r"(-?[0-9]+)"


def is_i_format_with_offset(parts: List[str]) -> bool:
    """Checks if the given instruction parts represent an I-format instruction with an offset.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    bool
        True if the instruction is an I-format instruction with an offset, False otherwise.

    """
    return len(parts) == 3


def get_rs1_from_offset(parts: List[str]) -> str:
    """Extracts the rs1 register from an instruction with an offset.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The rs1 register.

    """
    result = re.search(regex_find_rs1_from_offset, parts[2])
    return result.group()


def get_immediate_from_offset(parts: List[str]) -> str:
    """Extracts the immediate value from an instruction with an offset.

    Parameters
    ----------
    parts : List[str]
        The instruction parts, split by spaces and stripped of commas.

    Returns
    -------
    str
        The immediate value.

    """
    result = re.search(regex_find_imm_from_offset, parts[2])
    return result.group()
