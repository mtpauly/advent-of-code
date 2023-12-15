import argparse
from collections import defaultdict
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        line = file.read().strip()

    print(f"part 1 solution: {part_one(line)}")
    print(f"part 2 solution: {part_two(line)}")


def hash(string: str):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value


def part_one(line: str) -> int:
    total = 0
    for step in line.split(","):
        total += hash(step)
    return total


def part_two(line: str) -> int:
    boxes = defaultdict(list)  # box_ix: [[label, focal_len],]

    for step in line.split(","):
        label, operation, focal_len = re.findall("([a-z]+)([=-])(\\d*)", step)[0]
        box_ix = hash(label)

        if operation == "=":
            for i, (box_label, _) in enumerate(boxes[box_ix]):
                if box_label == label:
                    boxes[box_ix][i][1] = int(focal_len)
                    break
            else:
                boxes[box_ix].append([label, int(focal_len)])
        else:  # operation == "-"
            for i, (box_label, _) in enumerate(boxes[box_ix]):
                if box_label == label:
                    boxes[box_ix].pop(i)
                    break

    total = 0
    for box_ix, lenses in boxes.items():
        for slot, (_, focal_len) in enumerate(lenses, start=1):
            total += (int(box_ix) + 1) * slot * focal_len
    return total


if __name__ == "__main__":
    main()
