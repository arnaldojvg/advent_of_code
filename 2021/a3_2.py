from a3_1 import find_common


def calculate_oxygen(binaries: list[str], index: int) -> str:
    if len(binaries) == 1:
        return binaries[0]
    else:
        common = find_common(binaries, index)
        binaries = [bn for bn in binaries if bn[index] == common]
        return calculate_oxygen(binaries, index + 1)


def calculate_co2_scrubber(binaries: list[str], index: int) -> str:
    if len(binaries) == 1:
        return binaries[0]
    else:
        common = "0" if find_common(binaries, index) == "1" else "1"
        binaries = [bn for bn in binaries if bn[index] == common]
        return calculate_co2_scrubber(binaries, index + 1)


def solution(binaries: list[str]) -> int:

    oxygen = calculate_oxygen(binaries, 0)
    co2_scrubber = calculate_co2_scrubber(binaries, 0)

    return int(oxygen, 2) * int(co2_scrubber, 2)


if __name__ == '__main__':

    with open("inputs/a3.txt", "r") as f:
        inputs = [x.rstrip() for x in f.readlines()]

    print(solution(inputs))
