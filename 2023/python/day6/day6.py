import argparse
from typing import List
import re
from math import sqrt, floor, ceil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    times = [int(i) for i in re.findall("(\\d+)", lines[0])]
    dists = [int(i) for i in re.findall("(\\d+)", lines[1])]

    solutions = []
    for time, dist in zip(times, dists):
        count = 0
        for button_time in range(0, time + 1):
            if get_dist(button_time, time) > dist:
                count += 1
        solutions.append(count)

    prod = 1
    for n in solutions:
        prod *= n
    return prod


def part_two(lines: List[str]) -> int:
    time = int("".join(re.findall("(\\d+)", lines[0])))
    dist = int("".join(re.findall("(\\d+)", lines[1])))

    # compute the roots of the equation: dist = button_time * (time - button_time)
    bt_low = (time - sqrt(time**2 - 4 * dist)) / 2
    bt_high = (time + sqrt(time**2 - 4 * dist)) / 2

    count = floor(bt_high) - ceil(bt_low) + 1
    return count


def get_dist(button_time: int, total_time: int) -> int:
    return button_time * (total_time - button_time)


if __name__ == "__main__":
    main()
