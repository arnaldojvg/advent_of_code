def solution(depths: list[int]) -> int:

    pre = None
    increases = 0

    for n in depths:
        if pre is not None:
            if n > pre:
                increases += 1
        pre = n

    return increases


if __name__ == "__main__":

    with open("inputs/a1.txt", "r") as f:
        input_ = [int(line) for line in f.readlines()]

    print(solution(input_))
