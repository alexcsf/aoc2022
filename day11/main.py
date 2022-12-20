from collections import namedtuple
from operator import add, mul
from math import prod
import re

Monkey = namedtuple("Monkey", ["items", "op", "test", "true", "false"])


def get_op(operator, operand):
    op_dict = {"+": add, "*": mul}
    if operand == "old":
        return lambda x: op_dict[operator](x, x)
    return lambda x: op_dict[operator](x, int(operand))


def parse_monkeys(file):
    while file.readline():
        items = map(int, re.split(r"[:,] ", file.readline().rstrip())[1:])
        op = get_op(*re.split(r" ", file.readline().rstrip())[-2:])
        test = int(re.split("divisible by ", file.readline().rstrip())[1])
        true = int(re.split("monkey ", file.readline().rstrip())[1])
        false = int(re.split("monkey ", file.readline().rstrip())[1])
        file.readline()
        yield Monkey(list(items), op, test, true, false)


def count_inspections(n=20, div=3):
    with open("day11/input.txt", mode="r", encoding="utf-8") as file:
        monkeys = list(parse_monkeys(file))
        inspections = [0] * len(monkeys)
        m = prod(monkey.test for monkey in monkeys)
        for _ in range(n):
            for i, monkey in enumerate(monkeys):
                items, op, test, true, false = monkey
                for item in items:
                    new = op(item) // div if div else op(item) % m
                    throw_to = true if new % test == 0 else false
                    monkeys[throw_to].items.append(new)
                    inspections[i] += 1
                items.clear()
        return mul(*sorted(inspections)[-2:])


def main():
    print("1:", count_inspections())
    print("2:", count_inspections(10000, None))


if __name__ == "__main__":
    main()
