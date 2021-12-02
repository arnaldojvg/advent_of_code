def parse_movement(movement: str) -> tuple[str, int]:
    direction, value = movement.split()

    if direction == "forward":
        return "x", int(value)
    elif direction == "up":
        return "y", -int(value)
    elif direction == "down":
        return "y", int(value)
    else:
        print("Invalid direction")


def solution(movements: list[str]) -> int:

    pos = {"x": 0, "y": 0}
    for movement in movements:
        direction, value = parse_movement(movement)
        pos[direction] += value

    return pos["x"] * pos["y"]


if __name__ == "__main__":

    with open("inputs/a2.txt", "r") as f:
        inputs = f.readlines()

    print(solution(inputs))
