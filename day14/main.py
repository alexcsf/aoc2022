from sys import maxsize


class Cave:
    AIR, ROCK, SAND, SOURCE = ".", "#", "o", "+"

    left = top = maxsize
    right = bottom = -maxsize

    def __init__(self, paths, source, infinite_floor=False) -> None:
        self.cave = {}
        self.source = source
        self.infinite_floor = infinite_floor
        for path in paths:
            self.__update_cave(path)
        if self.infinite_floor:
            bottom = self.bottom + 2
            self.__update_cave([(self.left, bottom), (self.right, bottom)])

    def __update_cave(self, path):
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            if x1 > x2 or y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            self.left, self.top = min(self.left, x1), min(self.top, y1)
            self.right, self.bottom = max(self.right, x2), max(self.bottom, y2)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    self.cave[(i, j)] = Cave.ROCK

    def pour_sand(self):
        count = 0
        (x, y), cave = self.source, self.cave
        if self.infinite_floor:
            left, right, bottom = -maxsize, maxsize, self.bottom - 1
        else:
            left, right, bottom = self.left, self.right, self.bottom
        while (x, y) not in cave:
            while y < bottom and left <= x <= right:
                if (x, y + 1) not in cave:
                    y += 1
                elif (x - 1, y + 1) not in cave:
                    x, y = x - 1, y + 1
                elif (x + 1, y + 1) not in cave:
                    x, y = x + 1, y + 1
                else:
                    break

            if not self.infinite_floor:
                if y >= bottom or not left <= x <= right:
                    break
                cave[(x, y)], count = Cave.SAND, count + 1
            else:
                cave[(x, y)], count = Cave.SAND, count + 1
                start, end = min(self.left, x), max(self.right, x)
                self.__update_cave([(start, bottom + 1), (end, bottom + 1)])
            x, y = self.source

        return count

    def print_cave(self):
        cave = self.cave
        for i in range(self.bottom + 1):
            padding = len(str(self.right))
            print(str(i).ljust(padding), end=" ")
            for j in range(self.right - self.left + 1):
                x, y = (self.left + j, i)
                default = Cave.SOURCE if (x, y) == self.source else Cave.AIR
                print(cave.get((x, y), default), end="")
            print()
        print()


def split_path(line):
    for xs in line.strip().split(" -> "):
        x, y = xs.split(",")
        yield int(x), int(y)


def main():
    with open("day14/input.txt", mode="r", encoding="utf-8") as file:
        paths = [list(split_path(line)) for line in file]
        cave_1 = Cave(paths, (500, 0))
        cave_2 = Cave(paths, (500, 0), infinite_floor=True)
        print("1:", cave_1.pour_sand())
        print("2:", cave_2.pour_sand())


if __name__ == "__main__":
    main()
