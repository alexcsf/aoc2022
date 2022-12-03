from functools import reduce


def split(line):
    n = len(line) // 2
    return (line[:n], line[n:])


def common_item(iterable):
    for first in reduce(lambda acc, x: acc & x, map(set, iterable)):
        return first


def get_ord(ch):
    return ord(ch) - 38 if ch < "a" else ord(ch) - 96


with open("day03/input.txt", mode="r", encoding="utf-8") as file:
    lines = [line[:-1] for line in file.readlines()]
    items = [common_item(split(line)) for line in lines]
    groups = [common_item(lines[i : i + 3]) for i in range(0, len(lines), 3)]
    print("1:", sum(map(get_ord, items)))
    print("2:", sum(map(get_ord, groups)))
