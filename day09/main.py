def add_pairs(a, b):
    return (a[0] + b[0], a[1] + b[1])


with open("day09/input.txt", mode="r", encoding="utf-8") as file:
    lines = map(lambda x: (x[0], int(x[1])), [line.rstrip().split() for line in file])

    directions = {"D": (0, -1), "U": (0, 1), "L": (-1, 0), "R": (1, 0)}
    adjacent = {(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)}  # and overlap
    two_steps_away = {(-2, 0), (0, -2), (0, 2), (2, 0)}  # excluding diagonals

    knots = [(0, 0) for _ in range(10)]
    positions = [{knots[i]} for i in range(len(knots))]

    for direction, steps in lines:
        for _ in range(steps):
            knots[0] = add_pairs(knots[0], directions[direction])
            positions[0].add(knots[0])
            for i, (x, y) in enumerate(knots[1:], 1):
                (a, b) = add_pairs((-x, -y), knots[i - 1])
                if (a, b) in adjacent:
                    break
                if (a, b) in two_steps_away:
                    knots[i] = add_pairs(knots[i], (a // 2, b // 2))
                    positions[i].add(knots[i])
                else:
                    # normalize (a, b) to {-1, 1}
                    a, b = map(lambda x: -1 if x < 0 else 1, (a, b))
                    knots[i] = add_pairs(knots[i], (a, b))
                    positions[i].add(knots[i])

    tail_start, *_, tail_end = map(len, positions[1:])
    print("1:", tail_start)
    print("2:", tail_end)
