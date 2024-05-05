def hex_line_to_bin(hex_line):
    # Convert hex line to binary
    bin_line = bin(int(hex_line, 16))[2:]
    return bin_line


def transform_hex_file_to_bin(hex_file):
    bin_file = []
    with open(hex_file, "r") as f:
        for line in f:
            bin_line = hex_line_to_bin(line.strip())
            bin_line = bin_line.zfill(32)
            # Split binary line into 8-bit chunks and join them with spaces
            bin_line = " ".join(
                [bin_line[i : i + 8] for i in range(0, len(bin_line), 8)]
            )
            bin_file.append(bin_line)
    return bin_file


def write_bin_file(bin_file, bin_file_name):
    # Write binary file
    with open(bin_file_name, "w") as f:
        for line in bin_file:
            f.write(line + "\n")


write_bin_file(transform_hex_file_to_bin("bin.txt"), "bin2.txt")
