from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from os import cpu_count
from re import findall


def parse_signals(file):
    for line in file:
        a, b, c, d = findall(r"-?\d+", line)
        yield (int(a), int(b)), (int(c), int(d))


def get_ranges(signals, row):
    for (x, y), (x_beacon, y_beacon) in signals:
        dist = abs(x_beacon - x) + abs(y_beacon - y)
        k = dist - abs(y - row)
        if k > 0:
            yield (x - k, x + k)


def merge_ranges(ranges):
    ranges = sorted(ranges, reverse=True)
    while ranges:
        x, y = ranges.pop()
        while ranges:
            a, b = ranges.pop()
            if a <= y + 1:
                y = max(y, b)
            else:
                yield x, y
                x, y = a, b
        yield x, y


def find_beacon(signals, start, end):
    for row in range(start, end + 1):
        (_, a), *tail = merge_ranges(get_ranges(signals, row))
        if len(tail) == 1:
            return a + 1, row


def main():
    with open("day15/input.txt", mode="r", encoding="utf-8") as file:
        signals = list(parse_signals(file))

    beacons = {y: 1 for (_, (_, y)) in signals}
    row, limit = 2000000, 4000000

    range_lo, range_hi = next(merge_ranges(get_ranges(signals, row)))
    print("1:", range_hi - range_lo + 1 - beacons.get(row, 0))

    max_workers = cpu_count() or 1
    starts = ((limit // max_workers) * i for i in range(max_workers))
    ends = ((limit // max_workers) * i for i in range(1, max_workers))

    with ProcessPoolExecutor(max_workers) as pool:
        results = pool.map(find_beacon, repeat(signals), starts, ends)
        for result in results:
            if result:
                x, y = result
                print("2:", x * limit + y)
                break

    # Without ProcessPoolExecutor:
    #   x, y = find_beacon(signals, 0, limit)
    #   print("2:", x * limit + y)


if __name__ == "__main__":
    main()
