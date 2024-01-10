import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    horiz = 0
    depth = 0
    for line in lines:
        dir, count = line.split()
        count = int(count)
        if dir == "forward":
            horiz += count
        elif dir == "up":
            depth -= count
        else:
            depth += count
    return horiz * depth


def part_two(lines: list[str]) -> int:
    horiz = 0
    depth = 0
    aim = 0
    for line in lines:
        dir, count = line.split()
        count = int(count)
        if dir == "forward":
            horiz += count
            depth += aim * count
        elif dir == "up":
            aim -= count
        else:
            aim += count
    return horiz * depth


if __name__ == "__main__":
    main()
