import riscv32_im_assembler as assembler
import hex_to_bin as binhex

filename: str = "basic_program.s"
output_filename_hex: str = "output_hex"
output_filename_bin: str = "output_bin"


def raw_assemble_riscv32im(
    file_to_assemble: str, output_file: str, format: str = "bin"
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
    Returns
    -------
    None
    """
    try:
        with open(file_to_assemble, mode="r") as asm_file, open(
            output_file, mode="w"
        ) as out_file:
            for asm_line in asm_file:
                encoding = assembler.binary_encode_rv32i_line(asm_line)
                if format == "hex":
                    encoding = binhex.bin_line_to_hex(bin_line=encoding)
                out_file.write(encoding + "\n")
    except Exception as e:
        print(f"error in 'raw_assemble_risc32vim_to_hex' -> description: {e}")


raw_assemble_riscv32im(file_to_assemble=filename, output_file=output_filename_bin)

raw_assemble_riscv32im(
    file_to_assemble=filename, output_file=output_filename_hex, format="hex"
)
