def sum_table(table: list[list[int]]) -> int:
    return sum([sum(row_) for row_ in table])


def solution(draw_numbers: list[int], tables: list[list[list[int]]]) -> int:
    for number in draw_numbers:
        for table in tables:
            for row_i in range(len(table)):
                for col_i in range(5):
                    if table[row_i][col_i] == number:
                        table[row_i][col_i] = 0
                        if not any([table[row_i][n] for n in range(5)]) or not any([table[n][col_i] for n in range(5)]):
                            return sum_table(table) * number


if __name__ == '__main__':

    with open("inputs/a4.txt", "r") as f:
        inputs = f.read().splitlines()

    numbers = [int(x) for x in inputs[0].split(",")]

    total_tables = []
    current_table = []
    for row in inputs[1:]:
        if row == "":
            if current_table:
                total_tables.append(current_table)
            current_table = []
        else:
            current_table.append([int(x) for x in row.split()])

    if current_table:
        total_tables.append(current_table)

    print(solution(numbers, total_tables))
