import argparse
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    one_count = defaultdict(lambda: 0)
    for line in lines:
        for i, char in enumerate(line):
            if char == "1":
                one_count[i] += 1

    gamma = ""
    epsilon = ""
    for i in range(len(lines[0])):
        if one_count[i] > len(lines) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part_two(lines: list[str]) -> int:
    lines_oxy = lines.copy()
    pos = 0
    while len(lines_oxy) > 1:
        one_count = sum([1 for line in lines_oxy if line[pos] == "1"])
        if one_count >= len(lines_oxy) / 2:
            lines_oxy = [line for line in lines_oxy if line[pos] == "1"]
        else:
            lines_oxy = [line for line in lines_oxy if line[pos] == "0"]
        pos += 1

    lines_co2 = lines.copy()
    pos = 0
    while len(lines_co2) > 1:
        one_count = sum([1 for line in lines_co2 if line[pos] == "1"])
        if one_count < len(lines_co2) / 2:
            lines_co2 = [line for line in lines_co2 if line[pos] == "1"]
        else:
            lines_co2 = [line for line in lines_co2 if line[pos] == "0"]
        pos += 1

    return int(lines_oxy[0], 2) * int(lines_co2[0], 2)


if __name__ == "__main__":
    main()
