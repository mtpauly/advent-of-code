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
    nums = [int(l) for l in lines]
    for i, n in enumerate(nums):
        for m in (nums[i+1:]):
            return n * m

    raise ValueError()


def part_two(lines: list[str]) -> int:
    nums = [int(l) for l in lines]
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i+1:]):
            for o in nums[i+j+1:]:
                if n + m + o == 2020:
                    return n * m * o

    raise ValueError()


if __name__ == "__main__":
    main()
