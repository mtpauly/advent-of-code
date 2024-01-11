import argparse
from collections import defaultdict
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    c = defaultdict(lambda: 0)

    for l in lines:
        x1, y1, x2, y2 = [int(i) for i in re.findall("(\\d+)", l)]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                c[(x1, y)] += 1
            continue

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                c[(x, y1)] += 1

    return sum([1 for v in c.values() if v > 1])


def part_two(lines: list[str]) -> int:
    c = defaultdict(lambda: 0)

    for l in lines:
        x1, y1, x2, y2 = [int(i) for i in re.findall("(\\d+)", l)]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                c[(x1, y)] += 1
            continue

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                c[(x, y1)] += 1
            continue

        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) == abs(dy):
            sx = 1 if dx > 0 else -1
            sy = 1 if dy > 0 else -1
            for i in range(abs(x2 - x1) + 1):
                c[(x1 + i * sx, y1 + i * sy)] += 1

    return sum([1 for v in c.values() if v > 1])


if __name__ == "__main__":
    main()
