import argparse
from functools import cache
import time


Point = tuple[int, int]

DIRECTIONS: list[Point] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

TOTAL_STEPS = 26_501_365
PARTIAL_BUFFER = 4  # bigger is safer, smaller is faster
BINARY_SEARCH_OFFSET = 2  # bigger is safer, smaller is faster


def part_one() -> int:
    m = len(lines)
    n = len(lines[0])

    # find starting position
    start = (-1, -1)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
    assert start[0] >= 0 and start[1] >= 0

    # run bfs for 64 steps
    n_steps: dict[Point, int] = {}
    to_visit: list[Point] = [start]
    for step in range(64 + 1):
        new_to_visit = []

        for x, y in to_visit:
            if x < 0 or x >= n:
                continue
            if y < 0 or y >= m:
                continue
            if lines[x][y] == "#":
                continue
            if (x, y) in n_steps:
                continue

            n_steps[(x, y)] = step

            for dx, dy in DIRECTIONS:
                new_to_visit.append((x + dx, y + dy))

        to_visit = new_to_visit

    return sum([1 for step in n_steps.values() if step % 2 == 0])


@cache
def bfs(initial_to_visit: tuple[tuple[Point, int]]) -> dict[Point, int]:
    to_visit: list[tuple[Point, int]] = [v for v in initial_to_visit]
    n_steps: dict[Point, int] = {}
    while to_visit:
        new_to_visit = []
        for (x, y), step in to_visit:
            if x < 0 or x >= cols:
                continue
            if y < 0 or y >= rows:
                continue
            if lines[y][x] == "#":
                continue
            if (x, y) in n_steps and step >= n_steps[(x, y)]:
                continue

            n_steps[(x, y)] = step

            for dx, dy in DIRECTIONS:
                new_to_visit.append(((x + dx, y + dy), step + 1))

        to_visit = new_to_visit

    return n_steps


# returns the number of steps to access each of the four corners of map
def map_corner_steps(start: Point, map: Point) -> dict[Point, int]:
    steps_origin = bfs(((start, 0),))

    steps_map: dict[Point, int] = {}
    for ox1, oy1 in origin_corners:
        mx = ox1 + cols * map[0]
        my = oy1 + rows * map[1]

        corner_dist = []
        for ox2, oy2 in origin_corners:
            corner_dist.append(abs(mx - ox2) + abs(my - oy2) + steps_origin[(ox2, oy2)])
        steps_map[(ox1, oy1)] = min(corner_dist)

    return steps_map


def row_loop(
    row_start: int,
    step_direction: int,
    origin_start: Point,
    origin_total: int,
    offset_total: int,
    print_every: int = -1,
) -> int:
    total_steps = 0
    row_index = row_start

    next_right: Point = (0, TOTAL_STEPS)
    next_left: Point = (-TOTAL_STEPS, 0)

    start_time = time.perf_counter()
    while True:
        if print_every > 0 and row_index % print_every == 0:
            print(f"{time.perf_counter() - start_time:.1f}s -- {row_index}")

        # for each row, perform binary search to the left and right
        partial_filled: list[int] = []

        # binary search to the right
        low, high = next_right
        mid = 0
        while high > low:
            mid = (high - low) // 2 + low
            corner_steps = map_corner_steps(origin_start, (mid, row_index))
            map_steps = bfs(tuple(corner_steps.items()))
            if max(map_steps.values()) > TOTAL_STEPS:
                high = mid
            else:
                low = mid + 1
        next_right = (max([mid - BINARY_SEARCH_OFFSET, 0]), mid)

        # mid is now the col index of the first partially filled map
        partial_filled.extend([mid + i for i in range(PARTIAL_BUFFER)])

        # binary search to the left
        low, high = next_left
        while high > low:
            mid = (high - low) // 2 + low
            corner_steps = map_corner_steps(origin_start, (mid, row_index))
            map_steps = bfs(tuple(corner_steps.items()))
            if max(map_steps.values()) > TOTAL_STEPS:
                low = mid + 1
            else:
                high = mid
        next_left = (mid, min([mid + BINARY_SEARCH_OFFSET, 0]))

        # mid is now the col index of the first partially filled map
        partial_filled.extend([mid - i for i in range(PARTIAL_BUFFER)])

        # get the steps for fully filled maps
        row_steps = 0
        full_low = min(partial_filled) + PARTIAL_BUFFER
        full_high = max(partial_filled) - PARTIAL_BUFFER
        full_width = full_high - full_low + 1
        if full_width > 0:
            if full_width % 2 == 0:
                row_steps += full_width // 2 * (origin_total + offset_total)
            else:
                row_steps += (full_width - 1) // 2 * (origin_total + offset_total)
                if (full_low + row_index) % 2 == 0:
                    row_steps += origin_total
                else:
                    row_steps += offset_total

        # get the count of partial_filled
        # for col in partial_filled:
        for col in partial_filled:
            corner_steps = map_corner_steps(origin_start, (col, row_index))
            map_steps = bfs(tuple(corner_steps.items()))
            map_total = sum(
                [
                    1
                    for s in map_steps.values()
                    if s <= TOTAL_STEPS and s % 2 == TOTAL_STEPS % 2
                ]
            )
            row_steps += map_total

        total_steps += row_steps
        row_index += step_direction

        if row_steps == 0:
            break

    return total_steps


def part_two() -> int:
    origin_steps = bfs(((start, 0),))
    origin_total = sum([1 for s in origin_steps.values() if s % 2 == TOTAL_STEPS % 2])
    offset_total = sum(
        [1 for s in origin_steps.values() if s % 2 == (TOTAL_STEPS + 1) % 2]
    )

    total_up = row_loop(0, 1, start, origin_total, offset_total, 1000)
    total_down = row_loop(-1, -1, start, origin_total, offset_total, 1000)

    return total_up + total_down


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()

with open(args.input_file, "r") as file:
    lines = file.read().splitlines()

rows = len(lines)
cols = len(lines[0])

# find starting position
start = (-1, -1)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
assert start[0] >= 0 and start[1] >= 0

origin_corners: list[Point] = [
    (0, 0),
    (0, rows - 1),
    (cols - 1, 0),
    (cols - 1, rows - 1),
    (start[0], 0),
    (start[0], rows - 1),
    (0, start[1]),
    (cols - 1, start[1]),
]

print(f"part 1 solution: {part_one()}")
print(f"part 2 solution: {part_two()}")
