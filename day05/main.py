import re


def parse_input(file):
    [xs, ys] = map(lambda x: x.split("\n"), file.read().split("\n\n"))
    xs = [[line[i] for i in range(len(line) - 2, -1, -4)] for line in reversed(xs)]
    ys = [re.split(" from | to ", line[5:]) for line in ys][:-1]
    return [[x.pop() for x in xs if x][1:] for _ in xs], [list(map(int, y)) for y in ys]


def move_crates(stacks, instructions, multi_crate=False):
    ret = [stack.copy() for stack in stacks]
    for n, a, b in instructions:
        n, k = (n, 1) if multi_crate else (1, n)
        for _ in range(k):
            ret[b - 1].extend(reversed([ret[a - 1].pop() for _ in range(n)]))
    return ret


def top_crates(stacks):
    return "".join(stack.pop() for stack in stacks if stack)


def main():
    with open("day05/input.txt", mode="r", encoding="utf-8") as file:
        [stacks, instructions] = parse_input(file)
        stacks = [[crate for crate in stack if crate != " "] for stack in stacks]
        print("1:", top_crates(move_crates(stacks, instructions)))
        print("2:", top_crates(move_crates(stacks, instructions, True)))


if __name__ == "__main__":
    main()
