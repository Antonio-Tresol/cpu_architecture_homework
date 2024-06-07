BIN_TO_HEX_MAP = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def hex_line_to_bin(hex_line: str) -> str:
    """
    Convert a hexadecimal string to a binary string.

    Parameters
    ----------
    hex_line : str
        The hexadecimal string to convert.

    Returns
    -------
    str
        The converted binary string.
    """
    bin_line = bin(int(hex_line, 16))[2:]
    return bin_line


def transform_hex_file_to_bin(hex_file: str) -> list[str]:
    """
    Convert a file with hexadecimal strings to a list of binary strings.

    Parameters
    ----------
    hex_file : str
        The name of the file with hexadecimal strings.

    Returns
    -------
    list
        A list of binary strings.
    """
    bin_file = []
    with open(hex_file, "r") as f:
        for line in f:
            bin_line = hex_line_to_bin(line.strip())
            bin_line = bin_line.zfill(32)
            bin_line = " ".join(
                [bin_line[i : i + 8] for i in range(0, len(bin_line), 8)]
            )
            bin_file.append(bin_line)
    return bin_file


def bin_line_to_hex(bin_line: str) -> str:
    """
    Convert a binary string to a hexadecimal string.

    Parameters
    ----------
    bin_line : str
        The binary string to convert.

    Returns
    -------
    str
        The converted hexadecimal string.
    """
    hex_line = ""
    for i in range(0, len(bin_line), 4):
        four_bits = bin_line[i : i + 4]
        hex_line = hex_line + BIN_TO_HEX_MAP.get(four_bits)
    return hex_line


def transform_bin_file_to_hex(bin_file: str) -> list[str]:
    """
    Convert a file with binary strings to a list of hexadecimal strings.

    Parameters
    ----------
    bin_file : str
        The name of the file with binary strings.

    Returns
    -------
    list
        A list of hexadecimal strings.
    """
    hex_file = []
    with open(bin_file, "r") as file:
        for line in file:
            hex_line = bin_line_to_hex(line.strip())
            hex_file.append(hex_line)
    return hex_file


def write_line_to_file(lines: list[str], file_name: str) -> None:
    """
    Write a list of strings to a file, one string per line.

    Parameters
    ----------
    lines : List[str]
        The list of strings to write to the file.
    file_name : str
        The name of the file to write to.
    """
    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")
