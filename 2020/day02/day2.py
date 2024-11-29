import argparse
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
    total = 0
    for line in lines:
        min, max, letter, password = re.search('(\\d+)-(\\d+) ([a-z]): ([a-z]+)', line).groups()
        min = int(min)
        max = int(max)

        c = password.count(letter)
        if c >= min and c <= max:
            total += 1

    return total


def part_two(lines: list[str]) -> int:
    total = 0
    for line in lines:
        min, max, letter, password = re.search('(\\d+)-(\\d+) ([a-z]): ([a-z]+)', line).groups()
        min = int(min)
        max = int(max)

        a = password[min-1] == letter
        b = password[max-1] == letter

        total += a ^ b
    return total


if __name__ == '__main__':
    main()
