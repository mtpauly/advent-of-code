import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def is_solved(boards, nums):
    for i in range(5):
        for j in range(5):
            if boards[5 * i + j] not in nums:
                break
        else:
            return True
    for j in range(5):
        for i in range(5):
            if boards[5 * i + j] not in nums:
                break
        else:
            return True
    return False


def part_one(lines: list[str]) -> int:
    nums = [int(i) for i in lines[0].split(",")]
    boards_raw = "\n".join(lines[2:]).split("\n\n")
    boards = [[int(i) for i in "".join(b).split()] for b in boards_raw]

    for i in range(len(nums)):
        nums_set = set(nums[: i + 1])
        for board in boards:
            if is_solved(board, nums_set):
                unmarked = [b for b in board if b not in nums_set]
                return sum(unmarked) * nums[i]

    raise RuntimeError()


def part_two(lines: list[str]) -> int:
    nums = [int(i) for i in lines[0].split(",")]
    boards_raw = "\n".join(lines[2:]).split("\n\n")
    boards = [[int(i) for i in "".join(b).split()] for b in boards_raw]

    for i in range(len(nums)):
        nums_set = set(nums[: i + 1])
        for j in range(len(boards) - 1, -1, -1):
            if is_solved(boards[j], nums_set):
                if len(boards) == 1:
                    unmarked = [b for b in boards[j] if b not in nums_set]
                    return sum(unmarked) * nums[i]
                boards.pop(j)

    raise RuntimeError()


if __name__ == "__main__":
    main()
