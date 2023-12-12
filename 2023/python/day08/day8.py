import argparse
from typing import List, Dict
import re
import math


START = "AAA"
END = "ZZZ"
LEFT = "L"
RIGHT = "R"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    directions = lines[0]
    n = len(directions)

    nodes = {}  # AAA: (BBB, CCC)
    for line in lines[2:]:
        start, left, right = re.findall("([A-Z]+)", line)
        nodes[start] = (left, right)

    location = START
    steps = 0
    while location != END:
        direction = directions[steps % n]
        if direction == LEFT:
            location = nodes[location][0]
        else:
            location = nodes[location][1]
        steps += 1

    return steps


def part_two(lines: List[str]) -> int:
    directions = lines[0]
    n = len(directions)

    nodes = {}  # AAA: (BBB, CCC)
    for line in lines[2:]:
        start, left, right = re.findall("([1-9A-Z]+)", line)
        nodes[start] = (left, right)

    positions = []
    for node in nodes:
        if node[-1] == "A":
            positions.append(node)

    cycle_len = [get_cycle_length(p, directions, nodes) for p in positions]
    for c in cycle_len:
        assert c % n == 0

    lcm = math.lcm(*cycle_len)
    return lcm


def get_cycle_length(start: str, directions: str, nodes: Dict) -> int:
    position = start

    steps = 0
    while position[-1] != "Z":
        direction = directions[steps % len(directions)]
        if direction == LEFT:
            position = nodes[position][0]
        else:
            position = nodes[position][1]
        steps += 1

    return steps


if __name__ == "__main__":
    main()
