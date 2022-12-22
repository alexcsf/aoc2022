from json import loads
from functools import cmp_to_key
from math import prod


def comp(left, right):
    left, right = left[::-1], right[::-1]
    while left and right:
        a, b = left.pop(), right.pop()
        if isinstance(a, int) and isinstance(b, int):
            if a != b:
                return -1 if a < b else 1
            continue
        if isinstance(a, list) and isinstance(b, list):
            result = comp(a, b)
            if not result:
                continue
            return result
        a, b = ([a], b) if isinstance(a, int) else (a, [b])
        left.append(a)
        right.append(b)
    if not left and not right:
        return 0
    return -1 if right else 1


def main():
    with open("day13/input.txt", mode="r", encoding="utf-8") as file:
        dividers = [[[2]], [[6]]]
        lines = [line.rstrip() for line in file]
        packets = [[loads(a) for a in b] for b in zip(lines[::3], lines[1::3])]
        packets_flat = dividers + [packet for pair in packets for packet in pair]
        packets_flat.sort(key=cmp_to_key(comp))

        print("1:", sum(i for i, (a, b) in enumerate(packets, 1) if comp(a, b) == -1))
        print("2:", prod(packets_flat.index(d) + 1 for d in dividers))


if __name__ == "__main__":
    main()
