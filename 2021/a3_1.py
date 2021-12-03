def find_common(binaries: list[str], pos: int) -> str:

    ones = 0
    zeros = 0

    for n, bn in enumerate(binaries):
        if bn[pos] == "0":
            zeros += 1
        else:
            ones += 1

    return "1" if ones >= zeros else "0"


def solution(binaries: list[str]) -> int:

    gamma = ""
    epsilon = ""

    for pos in range(len(binaries[0])):
        common = find_common(binaries, pos)
        gamma += common
        epsilon += "0" if common == "1" else "1"

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':

    with open("inputs/a3.txt", "r") as f:
        inputs = [x.rstrip() for x in f.readlines()]

    print(solution(inputs))
