import argparse
from typing import List


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def next_diff(nums: List[int]) -> int:
    diffs = []
    all_zero = True
    for a, b in zip(nums[:-1], nums[1:]):
        diff = b - a
        if diff != 0:
            all_zero = False
        diffs.append(diff)

    if all_zero:
        return 0

    return diffs[-1] + next_diff(diffs)


def part_one(lines: List[str]) -> int:
    total = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        total += nums[-1] + next_diff(nums)
    return total


def part_two(lines: List[str]) -> int:
    total = 0
    for line in lines:
        nums = [int(i) for i in line.split()][::-1]
        total += nums[-1] + next_diff(nums)
    return total


if __name__ == "__main__":
    main()
