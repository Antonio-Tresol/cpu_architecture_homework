import io
import riscv32_im_assembler as assembler
import hex_to_bin as binhex


def raw_assemble_riscv32im(
    file_to_assemble: str, output_file: str, format: str, padding_lines: int = 0
) -> None:
    """
    Assemble a file of RISC-V 32 Interger-Multiply assembly instructions into a file of hexadecimal or binary machine code.

    This function reads each line of the input file, assembles it into binary using
    the `binary_encode_rv32i_line` function, converts the binary to hexadecimal if format is `hex`, and
    writes the result to the output file.

    Parameters
    ----------
    file_to_assemble : str
      The name of the file containing the RISC-V 32IM assembly instructions.
    output_file : str
      The name of the file to write the hexadecimal machine code to.
    format: str
      binary `bin` or hexadecimal `hex`. Default value is `bin`
    padding_lines: int
      a number of padding lines to add
    Returns
    -------
    None
    """
    with open(file_to_assemble, mode="r") as asm_file, open(
        output_file, mode="w"
    ) as out_file:
        pad_with_zeros(out_file, padding_lines, format)
        for asm_line in asm_file:
            encoding = assembler.binary_encode_rv32i_line(asm_line)
            if format == "hex":
                encoding = binhex.bin_line_to_hex(bin_line=encoding)
            out_file.write(encoding + "\n")


def pad_with_zeros(out_file: io.TextIOWrapper, n_lines: int, format: str) -> None:
    """
    Writes padding lines to the output file.

    This function writes a specified number of lines to the output file. Each line is a string of zeros. The length of the string depends on the specified format.

    Parameters
    ----------
    out_file : io.TextIOWrapper
        The output file to which the padding lines are written.
    n_lines : int
        The number of padding lines to write.
    format : str
        The format of the padding. If 'hex', each line will contain 8 zeros. Otherwise, each line will contain 32 zeros.

    Returns
    -------
    None

    """
    padding: str = (
        "00000000\n" if format == "hex" else "00000000000000000000000000000000\n"
    )
    for _ in range(n_lines):
        out_file.write(padding)


def main() -> None:

    filename: str = "basic_program.s"
    output_filename_hex: str = "output_hex"
    output_filename_bin: str = "output_bin"

    raw_assemble_riscv32im(
        file_to_assemble=filename, output_file=output_filename_bin, format="bin"
    )

    raw_assemble_riscv32im(
        file_to_assemble=filename, output_file=output_filename_hex, format="hex"
    )


if __name__ == "__main__":
    main()
