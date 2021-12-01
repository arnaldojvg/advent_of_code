from a1_1 import solution as sol1_1


def solution(depths: list[int]) -> int:

    weighted_depths = []

    for i in range(len(depths)):

        slice_depths = depths[i : i + 3]
        if len(slice_depths) < 3:
            break
        weighted_depths.append(sum(slice_depths))

    return sol1_1(weighted_depths)


if __name__ == "__main__":

    with open("inputs/a1_2.txt", "r") as f:
        input_ = [int(line) for line in f.readlines()]

    print(solution(input_))
