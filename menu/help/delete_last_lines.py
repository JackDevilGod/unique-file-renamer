from sys import stdout

def erase_output_lines(n: int=1) -> None:
    for _ in range(n):
        stdout.write("\x1b[1A")
        stdout.write("\x1b[2K\r")
    stdout.flush()