import argparse
import re
from typing import List


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    total = 0
    for line in lines:
        winning_nums = re.findall("(\\d+)", line.split(":")[1].split("|")[0])
        your_nums = re.findall("(\\d+)", line.split("|")[1])

        matches = set.intersection(set(winning_nums), set(your_nums))
        if matches:
            total += 2 ** (len(matches) - 1)

    return total


def part_two(lines: List[str]) -> int:
    card_counts = {i: 1 for i in range(len(lines))}

    for i, line in enumerate(lines):
        winning_nums = re.findall("(\\d+)", line.split(":")[1].split("|")[0])
        your_nums = re.findall("(\\d+)", line.split("|")[1])

        matches = set.intersection(set(winning_nums), set(your_nums))

        n_matches = len(matches)
        cur_count = card_counts[i]

        for j in range(n_matches):
            card_counts[i + j + 1] += cur_count

    return sum(card_counts.values())


if __name__ == "__main__":
    main()
