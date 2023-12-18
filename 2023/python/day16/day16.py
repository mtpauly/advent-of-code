import argparse
from typing import Deque
from collections import deque


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def count_energized(lines: list[str], start: tuple[int, int, int, int]) -> int:
    m = len(lines)
    n = len(lines[0])

    seen = set()
    stack: Deque[tuple[int, int, int, int]] = deque([start])
    while stack:
        row, col, drow, dcol = stack.pop()

        if row < 0 or row >= m:
            continue
        if col < 0 or col >= n:
            continue

        if (row, col, drow, dcol) in seen:
            continue
        seen.add((row, col, drow, dcol))

        match lines[row][col]:
            case ".":
                stack.append((row + drow, col + dcol, drow, dcol))
            case "|":
                if dcol == 0:
                    stack.append((row + drow, col + dcol, drow, dcol))
                else:
                    stack.append((row + 1, col, 1, 0))
                    stack.append((row - 1, col, -1, 0))
            case "-":
                if drow == 0:
                    stack.append((row + drow, col + dcol, drow, dcol))
                else:
                    stack.append((row, col + 1, 0, 1))
                    stack.append((row, col - 1, 0, -1))
            case "/":
                if drow == 0:
                    stack.append((row - dcol, col, -dcol, 0))
                else:
                    stack.append((row, col - drow, 0, -drow))
            case "\\":
                if drow == 0:
                    stack.append((row + dcol, col, dcol, 0))
                else:
                    stack.append((row, col + drow, 0, drow))

    seen_unique = set([(r, c) for r, c, _, _ in seen])
    return len(seen_unique)


def part_one(lines: list[str]) -> int:
    return count_energized(lines, (0, 0, 0, 1))


def part_two(lines: list[str]) -> int:
    m = len(lines)
    n = len(lines[0])

    energy_totals = []
    # left and right
    for i in range(m):
        energy_totals.append(count_energized(lines, (i, 0, 0, 1)))
        energy_totals.append(count_energized(lines, (i, n - 1, 0, -1)))

    # top and bottom
    for i in range(n):
        energy_totals.append(count_energized(lines, (0, i, 1, 0)))
        energy_totals.append(count_energized(lines, (m - 1, i, -1, 0)))

    return max(energy_totals)


if __name__ == "__main__":
    main()
