import argparse
import re
from itertools import combinations
import z3


CROSS_MIN = 200000000000000
CROSS_MAX = 400000000000000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    points = []
    for line in lines:
        x, y, _, dx, dy, _ = re.findall("([-\\d]+)", line)
        points.append((int(x), int(y), int(dx), int(dy)))

    total = 0
    for (x1, y1, dx1, dy1), (x2, y2, dx2, dy2) in combinations(points, 2):
        if dx1 / dy1 == dx2 / dy2:
            if x1 == x2 and y1 == y2:
                total += 1
        else:
            t1 = (dx2 * y1 - dx2 * y2 - dy2 * x1 + dy2 * x2) / (dx1 * dy2 - dx2 * dy1)
            t2 = (dx1 * y1 - dx1 * y2 - dy1 * x1 + dy1 * x2) / (dx1 * dy2 - dx2 * dy1)
            if (
                t1 >= 0
                and t2 >= 0
                and CROSS_MIN <= x1 + dx1 * t1 <= CROSS_MAX
                and CROSS_MIN <= y1 + dy1 * t1 <= CROSS_MAX
            ):
                total += 1

    return total


def part_two(lines: list[str]) -> int:
    s = z3.Solver()
    x, y, z, dx, dy, dz = z3.Reals("x y z dx dy dz")

    for i, line in enumerate(lines[:3]):
        px, py, pz, pdx, pdy, pdz = re.findall("([-\\d]+)", line)

        t = z3.Real(f"t{i}")

        s.add(t >= 0)
        s.add(x + t * dx == int(px) + t * int(pdx))
        s.add(y + t * dy == int(py) + t * int(pdy))
        s.add(z + t * dz == int(pz) + t * int(pdz))

    assert s.check() == z3.sat

    model = s.model()
    return sum([model[n].as_long() for n in (x, y, z)])


if __name__ == "__main__":
    main()
