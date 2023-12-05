import argparse
from typing import List


NUMBER_STRS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part1(lines)}")
    print(f"part 2 solution: {part2(lines)}")


def part1(lines: List[str]) -> int | None:
    total = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for char in line:
            if char.isnumeric():
                if first_digit is None:
                    first_digit = char
                last_digit = char
                continue

        if first_digit is None or last_digit is None:
            return None

        total += int(first_digit + last_digit)

    return total


def part2(lines: List[str]) -> int | None:
    total = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for i, char in enumerate(line):
            if char.isnumeric():
                if first_digit is None:
                    first_digit = char
                last_digit = char
                continue
            else:
                for word, number in NUMBER_STRS.items():
                    if line[i:].startswith(word):
                        if first_digit is None:
                            first_digit = number
                        last_digit = number
                        break

        if first_digit is None or last_digit is None:
            return None

        total += int(first_digit + last_digit)

    return total


if __name__ == "__main__":
    main()
