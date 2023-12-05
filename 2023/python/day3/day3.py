import argparse
from typing import List, Tuple


GEAR_SYMBOL = "*"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    # pad with periods so we don't need to check boundary conditions
    for i in range(len(lines)):
        lines[i] = "." + lines[i] + "."
    period_line = "." * len(lines[0])
    lines.insert(0, period_line)
    lines.append(period_line)

    part1_total = 0

    in_number = False
    number = 0
    number_col = 0
    gears = {}  # (row, col): (count, ratio)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isnumeric():
                number = number * 10 + int(char)

                if not in_number:
                    in_number = True
                    number_col = col
            elif in_number:
                symbol = find_symbol(row, number_col, col, lines)
                if symbol:
                    part1_total += number

                    if lines[symbol[0]][symbol[1]] == GEAR_SYMBOL:
                        if symbol in gears:
                            gears[symbol][0] += 1
                            gears[symbol][1] *= number
                        else:
                            gears[symbol] = [1, number]

                in_number = False
                number = 0

    part2_total = 0
    for count, ratio in gears.values():
        if count == 2:
            part2_total += ratio

    print(f"part 1 solution: {part1_total}")
    print(f"part 2 solution: {part2_total}")


def find_symbol(
    row: int, start_col: int, end_col: int, lines: List[str]
) -> Tuple[int, int] | None:
    # check above and below, including corners
    for rix in [row - 1, row + 1]:
        for cix in range(start_col - 1, end_col + 1):
            if cell_has_symbol(rix, cix, lines):
                return rix, cix

    # check left and right
    if cell_has_symbol(row, start_col - 1, lines):
        return row, start_col - 1
    if cell_has_symbol(row, end_col, lines):
        return row, end_col

    return None


def cell_has_symbol(row: int, col: int, lines: List[str]) -> bool:
    cell = lines[row][col]
    if cell.isnumeric():
        return False
    if cell == ".":
        return False
    return True


if __name__ == "__main__":
    main()
