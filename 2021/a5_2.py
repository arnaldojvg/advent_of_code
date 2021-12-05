point = tuple[int, int]
line = tuple[point, point]


def solution(lines: list[line]):
    """
    Return the number of lines that intersect.
    """
    table = [[0 for _ in range(1000)] for _ in range(1000)]
    greater_than_1: set[tuple] = set()
    for ((x1, y1), (x2, y2)) in lines:

        if x1 == x2:
            min_y, max_y = min(y1, y2), max(y1, y2)
            for yi in range(min_y, max_y + 1):
                table[yi][x1] += 1
                if table[yi][x1] > 1:
                    greater_than_1.add((x1, yi))
        elif y1 == y2:
            min_x, max_x = min(x1, x2), max(x1, x2)
            for xi in range(min_x, max_x + 1):
                table[y1][xi] += 1
                if table[y1][xi] > 1:
                    greater_than_1.add((xi, y1))
        else:
            while x1 != x2 and y1 != y2:
                table[y1][x1] += 1
                if table[y1][x1] > 1:
                    greater_than_1.add((x1, y1))

                if x1 < x2:
                    x1 += 1
                else:
                    x1 -= 1
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1
            table[y1][x1] += 1
            if table[y1][x1] > 1:
                greater_than_1.add((x1, y1))

    return len(greater_than_1)


if __name__ == '__main__':

    with open("inputs/a5.txt") as f:
        input_ = f.readlines()

    lines_ = []
    for row in input_:
        row = row.rstrip()
        a, b = row.split(" -> ")
        a, b = ((int(x), int(y)) for x, y in (a.split(","), b.split(",")))
        lines_.append((a, b))

    print(solution(lines_))
