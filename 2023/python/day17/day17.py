import argparse
import heapq
from collections import defaultdict


Point = tuple[int, int, int, int, int]  # x, y, dx, dy, steps_remaining

DIRECTIONS: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def get_adj(x: int, y: int, dx: int, dy: int, steps_remaining: int) -> list[Point]:
    if steps_remaining == 0:
        if dx != 0:
            return [
                (x, y + 1, 0, 1, 2),
                (x, y - 1, 0, -1, 2),
            ]
        else:
            return [
                (x + 1, y, 1, 0, 2),
                (x - 1, y, -1, 0, 2),
            ]

    adj = [(x + dx, y + dy, dx, dy, steps_remaining - 1)]
    for dx_new, dy_new in DIRECTIONS:
        if dx_new == dx and dy_new == dy:
            continue
        if dx_new == -dx and dy_new == -dy:
            continue
        adj.append((x + dx_new, y + dy_new, dx_new, dy_new, 2))
    return adj


def part_one(lines: list[str]) -> int:
    m = len(lines)
    n = len(lines[0])

    heat: dict[tuple[int, int], int] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            heat[(x, y)] = int(char)

    min_heat: defaultdict[Point, int] = defaultdict(lambda: 999999999)

    heap: list[tuple[int, Point]] = []
    heap.extend([(0, point) for point in get_adj(0, 0, 1, 0, 3)])
    heap.extend([(0, point) for point in get_adj(0, 0, 0, 1, 3)])
    heapq.heapify(heap)

    while heap:
        point_heat, point = heapq.heappop(heap)

        x, y, _, _, _ = point
        if x == n - 1 and y == m - 1:
            return point_heat + heat[(x, y)]
        if x < 0 or x >= n:
            continue
        if y < 0 or y >= m:
            continue

        point_heat += heat[(x, y)]
        if point_heat >= min_heat[point]:
            continue

        min_heat[point] = point_heat
        for point_adj in get_adj(*point):
            heapq.heappush(heap, (point_heat, point_adj))

    raise RuntimeError("did not traverse to bottom corner")


def get_adj_ultra(x: int, y: int, dx: int, dy: int, steps_taken: int) -> list[Point]:
    if steps_taken == 10:
        if dx != 0:
            return [
                (x, y + 1, 0, 1, 1),
                (x, y - 1, 0, -1, 1),
            ]
        else:
            return [
                (x + 1, y, 1, 0, 1),
                (x - 1, y, -1, 0, 1),
            ]

    adj = [(x + dx, y + dy, dx, dy, steps_taken + 1)]
    if steps_taken >= 4:
        for dx_new, dy_new in DIRECTIONS:
            if dx_new == dx and dy_new == dy:
                continue
            if dx_new == -dx and dy_new == -dy:
                continue
            adj.append((x + dx_new, y + dy_new, dx_new, dy_new, 1))
    return adj


def part_two(lines: list[str]) -> int:
    m = len(lines)
    n = len(lines[0])

    heat: dict[tuple[int, int], int] = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            heat[(x, y)] = int(char)

    min_heat: defaultdict[Point, int] = defaultdict(lambda: 999999999)

    heap: list[tuple[int, Point]] = []
    heap.extend([(0, point) for point in get_adj_ultra(0, 0, 1, 0, 0)])
    heap.extend([(0, point) for point in get_adj_ultra(0, 0, 0, 1, 0)])
    heapq.heapify(heap)

    while heap:
        point_heat, point = heapq.heappop(heap)

        x, y, _, _, steps_taken = point
        if x == n - 1 and y == m - 1:
            return point_heat + heat[(x, y)]
        if x < 0 or x >= n:
            continue
        if y < 0 or y >= m:
            continue

        point_heat += heat[(x, y)]
        if point_heat >= min_heat[point]:
            continue

        min_heat[point] = point_heat
        for point_adj in get_adj_ultra(*point):
            heapq.heappush(heap, (point_heat, point_adj))

    raise RuntimeError("did not traverse to bottom corner")


if __name__ == "__main__":
    main()
