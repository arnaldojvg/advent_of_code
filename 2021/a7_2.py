def fuel(value: int) -> int:
    return int((value / 2) * (value + 1))


def solution(h_positions: list[int]):

    counter = {}
    for pos in h_positions:
        counter[pos] = counter.get(pos, 0) + 1

    counter_keys = sorted(counter.keys())
    cost_matrix = [[0 for _ in counter_keys] for _ in range(max(counter_keys))]

    for n in range(max(counter_keys)):
        for m, pos2 in enumerate(counter_keys):
            cost_matrix[n][m] = fuel(abs(n - pos2)) * counter[pos2]

    return min([sum(adj) for adj in cost_matrix])


if __name__ == "__main__":
    with open("inputs/a7.txt") as f:
        crabs = [int(x) for x in f.read().split(",")]

    print(solution(crabs))
