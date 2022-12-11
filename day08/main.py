from operator import mul
from functools import reduce


def scan_max(m):
    for i, row in enumerate(m):
        view_distances = []
        last_pos = [-1 for _ in range(10)]
        max_tot = -1
        for j, col in enumerate(row):
            if col > max_tot:
                max_tot = col
                view_distances.append(j)  # tallest tree in this row
            else:
                # get MRU index of a tree with a height >= to this one
                view_distances.append(j - max(last_pos[col:]))
            m[i][j] = max_tot
            last_pos[col] = j
        view_distances[0] = 0
        m[i] = list(zip([-1] + m[i], view_distances))
    return m


def transpose(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


with open("day08/input.txt", mode="r", encoding="utf-8") as file:
    m = [[int(x) for x in line.rstrip()] for line in file]
    W, H = len(m[0]), len(m)

    up = transpose(scan_max(transpose(m)))
    down = transpose(scan_max([row[::-1] for row in transpose(m)]))[::-1]
    left = scan_max([row.copy() for row in m])
    right = [row[::-1] for row in scan_max([row[::-1] for row in m])]

    visible_trees = scenic_score = 0
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            neighbors = up[i][j], down[i][j], left[i][j], right[i][j]
            maxima, distances = list(zip(*neighbors))
            visible_trees += 1 if any(map(lambda x: x < col, maxima)) else 0
            scenic_score = max(scenic_score, reduce(mul, distances, 1))

    print("1:", visible_trees)
    print("2:", scenic_score)
