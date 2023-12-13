import argparse
from typing import List, Tuple
import functools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


@functools.cache
def count_options(springs: str, blocks: Tuple[int]) -> int:
    if not springs:
        if not blocks:
            return 1
        return 0

    if springs[0] == ".":
        return count_options(springs[1:], blocks)

    if springs[0] == "#":
        if not blocks:
            return 0
        if len(springs) < blocks[0]:
            return 0

        for i in range(blocks[0]):
            if springs[i] == ".":
                return 0

        if len(springs) == blocks[0]:
            return count_options("", blocks[1:])
        if springs[blocks[0]] == "#":
            return 0
        return count_options(springs[blocks[0] + 1 :], blocks[1:])

    operational_options = count_options("." + springs[1:], blocks)
    damaged_options = count_options("#" + springs[1:], blocks)
    return operational_options + damaged_options


def part_one(lines: List[str]) -> int:
    total = 0
    for line in lines:
        springs, blocks = line.split()
        blocks = [int(i) for i in blocks.split(",")]
        total += count_options(springs, tuple(blocks))
    return total


def part_two(lines: List[str]) -> int:
    total = 0
    for line in lines:
        springs, blocks = line.split()
        blocks = 5 * [int(i) for i in blocks.split(",")]
        springs = "?".join([springs for _ in range(5)])
        total += count_options(springs, tuple(blocks))
    return total


if __name__ == "__main__":
    main()
