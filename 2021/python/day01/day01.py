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
    count = 0
    for l1, l2 in zip(lines[:-1], lines[1:]):
        if int(l2) > int(l1):
            count += 1
    return count


def part_two(lines: list[str]) -> int:
    count = 0
    for l1, l2 in zip(lines[:-3], lines[3:]):
        if int(l2) > int(l1):
            count += 1
    return count


if __name__ == "__main__":
    main()
