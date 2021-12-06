def solution(lantern_fishes: list[int], days: int) -> int:


    for i in range(days):
        lantern_fishes2 = lantern_fishes.copy()
        for n, fish in enumerate(lantern_fishes2):
            if fish > 0:
                lantern_fishes[n] = fish - 1
            else:
                lantern_fishes[n] = 6
                lantern_fishes.append(8)

    return len(lantern_fishes)


if __name__ == '__main__':

    with open("inputs/a6.txt", "r") as f:
        data = f.read()

    fishes = [int(x) for x in data.split(",")]
    print(solution(fishes, 256))
