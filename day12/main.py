# Requires Python >= 3.10 (insort uses the new 'key' param).
from bisect import insort
from collections import defaultdict
import math


def find(grid, vals):
    for k, v in grid.items():
        if v in vals:
            yield k


def get_neighbors(grid, pos):
    row, col = pos
    for target in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
        if target in grid and ord(grid[target]) <= ord(grid[pos]) + 1:
            yield target


def shortest_path(grid, start, end):
    path_costs = defaultdict(lambda: math.inf, {k: 0 for k in start})
    heap = start  # poor man's min-heap
    heap.sort(key=lambda x: path_costs[x], reverse=True)
    while heap:
        node = heap[-1]
        if node == end:
            return path_costs[end]
        heap.pop()
        for neighbor in get_neighbors(grid, node):
            if path_costs[node] + 1 < path_costs[neighbor]:
                path_costs[neighbor] = path_costs[node] + 1
                insort(heap, neighbor, key=lambda x: -path_costs[x])
    return None


def main():
    with open("day12/input.txt", mode="r", encoding="utf-8") as file:
        grid = {(i, j): v for j, row in enumerate(file) for i, v in enumerate(row[:-1])}
        start, end = find(grid, set("SE"))
        grid[start], grid[end] = "a", "z"
        print("1:", shortest_path(grid, [start], end))
        print("2:", shortest_path(grid, [k for k in grid if grid[k] == "a"], end))


if __name__ == "__main__":
    main()
