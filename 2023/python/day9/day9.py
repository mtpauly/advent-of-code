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


def part_one(lines: List[str]) -> int:
    total = 0
    for line in lines:
        seq = [int(i) for i in line.split()]

        seq_ends = []
        while True:
            for d in seq:
                if d != 0:
                    break
            else:
                break
            
            seq_ends.append(seq[-1])

            new_seq = []
            for a, b in zip(seq[:-1], seq[1:]):
                new_seq.append(b - a)
            seq = new_seq

        total += sum(seq_ends)

    return total


def part_two(lines: List[str]) -> int:
    total = 0
    for line in lines:
        seq = [int(i) for i in line.split()]

        seq_starts = []
        while True:
            seq_starts.append(seq[0])

            for d in seq:
                if d != 0:
                    break
            else:
                break

            new_seq = []
            for a, b in zip(seq[:-1], seq[1:]):
                new_seq.append(b - a)
            seq = new_seq

        sol = 0
        for i in seq_starts[::-1]:
            sol = i - sol

        total += sol

    return total


if __name__ == "__main__":
    main()
