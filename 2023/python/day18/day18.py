import argparse
import re
from collections import deque


Point = tuple[int, int]

DIRECTION_MAP: dict[str, Point] = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "3": (-1, 0),
    "1": (1, 0),
    "2": (0, -1),
    "0": (0, 1),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().strip().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    vertices: list[Point] = [(0, 0)]
    boundary_count = 0

    x = 0
    y = 0
    for line in lines:
        dir, count = re.findall("([UDLR]) (\\d+)", line)[0]
        count = int(count)

        dx, dy = DIRECTION_MAP[dir]
        x += count * dx
        y += count * dy
        vertices.append((x, y))
        boundary_count += count

    # shoelace formula
    trapezoids = [
        (vertices[-1][1] + vertices[0][1]) * (vertices[-1][0] - vertices[0][0])
    ]
    for (x1, y1), (x2, y2) in zip(vertices[:-1], vertices[1:]):
        trapezoids.append((y1 + y2) * (x1 - x2))
    area = abs(sum(trapezoids)) // 2

    # pick's formula
    interior_count = area - boundary_count // 2 + 1

    return boundary_count + interior_count


def part_two(lines: list[str]) -> int:
    vertices: list[Point] = [(0, 0)]
    boundary_count = 0

    x = 0
    y = 0
    for line in lines:
        hex, dir = re.findall("\\(#([a-z\\d]+)(\\d)\\)", line)[0]

        dx, dy = DIRECTION_MAP[dir]
        count = int(hex, 16)
        x += count * dx
        y += count * dy
        vertices.append((x, y))
        boundary_count += count

    # shoelace formula
    trapezoids = [
        (vertices[-1][1] + vertices[0][1]) * (vertices[-1][0] - vertices[0][0])
    ]
    for (x1, y1), (x2, y2) in zip(vertices[:-1], vertices[1:]):
        trapezoids.append((y1 + y2) * (x1 - x2))
    area = abs(sum(trapezoids)) // 2

    # pick's formula
    interior_count = area - boundary_count // 2 + 1

    return boundary_count + interior_count


if __name__ == "__main__":
    main()
