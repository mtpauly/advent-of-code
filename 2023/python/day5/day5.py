import argparse
from typing import List, Tuple
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    seeds = [int(i) for i in re.findall("(\\d+)", lines[0])]

    # encode the maps
    maps = []
    map = []
    in_map = False
    for line in lines[2:] + [""]:
        if line and not in_map:
            in_map = True
        elif line and in_map:
            map.append([int(i) for i in re.findall("(\\d+)", line)])
        else:
            map.sort(key=lambda m: m[1])
            maps.append(map)
            map = []
            in_map = False

    # follow each seed through the maps
    end_values = []
    for seed in seeds:
        value = seed
        for map in maps:
            for line in map:
                dst, src, range_ = line
                if value >= src and value < src + range_:
                    value += dst - src
                    break
        end_values.append(value)

    return min(end_values)


def part_two(lines: List[str]) -> int:
    # encode the maps
    maps = []
    map = []
    in_map = False
    for line in lines[2:] + [""]:
        if line and not in_map:
            in_map = True
        elif line and in_map:
            map.append([int(i) for i in re.findall("(\\d+)", line)])  # dst, src, range
        else:
            map.sort(key=lambda m: m[1])
            maps.append(map)
            map = []
            in_map = False

    # follow each range through maps
    ranges = []  # (start, end not inclusive)
    seed_pairs = [int(i) for i in re.findall("(\\d+)", lines[0])]
    for start, length in zip(seed_pairs[::2], seed_pairs[1::2]):
        ranges.append((start, start + length))
    
    for map in maps:
        new_ranges = []
        for range_ in ranges:
            new_ranges.extend(map_range(range_, map))
        ranges = new_ranges

    range_starts = [r[0] for r in ranges]
    return min(range_starts)


def map_range(range_: Tuple[int, int], map: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    start, end = range_

    ranges = []
    for line in map:
        dst, src, rge = line
        line_start = src
        line_end = src + rge
        line_offset = dst - src

        if start < line_start:
            new_start = min(end, line_start)
            ranges.append((start, new_start))
            start = new_start

        if line_start <= start < line_end:
            new_start = min(end, line_end)
            ranges.append((start + line_offset, new_start + line_offset))
            start = new_start

        if start == end:
            break

    if start != end:
        ranges.append((start, end))

    return ranges


if __name__ == "__main__":
    main()
