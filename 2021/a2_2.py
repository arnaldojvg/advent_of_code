def solution(movements: list[str]) -> int:

    hz = 0
    vt = 0
    aim = 0

    for movement in movements:
        direction, value = movement.split()
        value = int(value)

        if direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        elif direction == "forward":
            hz += value
            vt += aim * value

    return hz * vt


if __name__ == "__main__":

    with open("inputs/a2.txt", "r") as f:
        inputs = f.readlines()

    print(solution(inputs))
