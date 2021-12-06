def solution(lantern_fishes: list[int], days: int) -> int:

    fishes_count = {}

    for fish_ in lantern_fishes:
        if fish_ not in fishes_count:
            fishes_count[fish_] = 0
        fishes_count[fish_] += 1

    for i in range(days):
        new_fish_count = {}
        for fish in range(8, -1, -1):
            if fish in fishes_count:
                if fish > 0:
                    new_fish_count[fish - 1] = fishes_count[fish]
                else:
                    new_fish_count[8] = fishes_count[fish]
                    if 6 not in new_fish_count:
                        new_fish_count[6] = 0
                    new_fish_count[6] += fishes_count[fish]
                fishes_count.pop(fish)

        fishes_count = new_fish_count

    return sum(fishes_count.values())


if __name__ == "__main__":

    with open("inputs/a6.txt", "r") as f:
        data = f.read()

    fishes = [int(x) for x in data.split(",")]
    print(solution(fishes, 256))
