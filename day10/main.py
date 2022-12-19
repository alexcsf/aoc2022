from itertools import accumulate
from operator import add


def parsed_lines(file):
    yield 1
    for line in file:
        yield 0
        parsed_line = line.rstrip().split()
        if parsed_line[0] == "addx":
            yield int(parsed_line[1])


with open("day10/input.txt", mode="r", encoding="utf-8") as file:
    program = list(accumulate(parsed_lines(file), add))
    crt = ""
    for i, x in enumerate(program[:-1], 1):
        h_pos = i % 40
        crt += "#" if h_pos in [(x + i) % 40 for i in range(3)] else "."
        if h_pos == 0:
            crt += "\n"

    cycles = [20, 60, 100, 140, 180, 220]
    result = sum(program[cycle - 1] * cycle for cycle in cycles)
    print("1:", result)
    print("2:", crt, sep="\n")
