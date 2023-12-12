import argparse
from typing import List
import itertools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    galaxies_orig = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxies_orig.append((i, j))

    rows = set(g[0] for g in galaxies_orig)
    cols = set(g[1] for g in galaxies_orig)

    galaxies = []
    for i, j in galaxies_orig:
        row_offset = sum([1 for r in range(i) if r not in rows])
        col_offset = sum([1 for c in range(j) if c not in cols])
        galaxies.append((i + row_offset, j + col_offset))

    total = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        total += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

    return total


def part_two(lines: List[str]) -> int:
    galaxies_orig = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxies_orig.append((i, j))

    rows = set(g[0] for g in galaxies_orig)
    cols = set(g[1] for g in galaxies_orig)

    galaxies = []
    for i, j in galaxies_orig:
        row_offset = sum([999_999 for r in range(i) if r not in rows])
        col_offset = sum([999_999 for c in range(j) if c not in cols])
        galaxies.append((i + row_offset, j + col_offset))

    total = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        total += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

    return total


if __name__ == "__main__":
    main()
