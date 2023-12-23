import argparse
from collections import defaultdict
from graphviz import Digraph
import sys
import heapq
from collections import deque


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ICE_DIRECTIONS = {
    "v": (0, 1),
    "^": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}

Point = tuple[int, int]
PointPair = tuple[Point, Point]


def part_one(lines: list[str]) -> int:
    rows = len(lines)
    cols = len(lines[0])

    # find start and end
    for i, char in enumerate(lines[0]):
        if char == ".":
            start = (i, 0)
            break
    else:
        assert False
    for i, char in enumerate(lines[-1]):
        if char == ".":
            end = (i, rows - 1)
            break
    else:
        assert False

    # find junctions
    junctions: list[Point] = [start, end]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                continue

            neighbor_count = 0
            for dx, dy in DIRECTIONS:
                x_new = x + dx
                y_new = y + dy
                if x_new < 0 or x_new >= cols:
                    continue
                if y_new < 0 or y_new >= rows:
                    continue
                if lines[y + dy][x + dx] != "#":
                    neighbor_count += 1

            if neighbor_count > 2:
                junctions.append((x, y))

    # get distances using bfs
    # store negative distances so we can use a min heap later
    junction_dist_neg: defaultdict[Point, dict[Point, int]] = defaultdict(dict)
    for j_start in junctions:
        seen = set()
        to_visit = [j_start]
        steps = 0
        while to_visit:
            new_to_visit = []
            for point in to_visit:
                x, y = point
                if x < 0 or x >= cols:
                    continue
                if y < 0 or y >= rows:
                    continue
                if lines[y][x] == "#":
                    continue
                if point in seen:
                    continue

                seen.add(point)

                if point != j_start and point in junctions:
                    junction_dist_neg[j_start][point] = -steps
                    continue

                if lines[y][x] in ICE_DIRECTIONS:
                    dx, dy = ICE_DIRECTIONS[lines[y][x]]
                    new_to_visit.append((x + dx, y + dy))
                else:
                    new_to_visit.extend([(x + dx, y + dy) for dx, dy in DIRECTIONS])

            to_visit = new_to_visit
            steps += 1

    # find the longest path from start to end using dijkstra's
    neg_dist: defaultdict[Point, int] = defaultdict(lambda: 1)
    heap: list[tuple[int, Point]] = [(0, start)]
    while heap:
        dist, point = heapq.heappop(heap)

        if dist >= neg_dist[point]:
            continue

        neg_dist[point] = dist

        for neighbor, neighbor_dist in junction_dist_neg[point].items():
            heapq.heappush(heap, (dist + neighbor_dist, neighbor))

    # visualize
    # for y, line in enumerate(lines):
    #     line_j = []
    #     for x, char in enumerate(line):
    #         if (x, y) in junctions:
    #             print("J", end="")
    #             line_j.append((x, y))
    #         else:
    #             print(lines[y][x], end="")
    #     print(f" {line_j}")

    # dot = Digraph(comment='Junction Graph')
    # for point in junction_dist_neg:
    #     dot.node(str(point))
    # for point, connection_list in junction_dist_neg.items():
    #     for connection, distance in connection_list.items():
    #         dot.edge(str(point), str(connection), label=str(-distance))
    # dot.render(f"{sys.argv[1].split('.')[0]}_junctions.gv", view=True)

    return -neg_dist[end]


def part_two(lines: list[str]) -> int:
    rows = len(lines)
    cols = len(lines[0])

    # find start and end
    for i, char in enumerate(lines[0]):
        if char == ".":
            start = (i, 0)
            break
    else:
        assert False
    for i, char in enumerate(lines[-1]):
        if char == ".":
            end = (i, rows - 1)
            break
    else:
        assert False

    # find junctions
    junctions: list[Point] = [start, end]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                continue

            neighbor_count = 0
            for dx, dy in DIRECTIONS:
                x_new = x + dx
                y_new = y + dy
                if x_new < 0 or x_new >= cols:
                    continue
                if y_new < 0 or y_new >= rows:
                    continue
                if lines[y + dy][x + dx] != "#":
                    neighbor_count += 1

            if neighbor_count > 2:
                junctions.append((x, y))

    # get distances using bfs
    # store negative distances so we can use a min heap later
    junction_dist: defaultdict[Point, dict[Point, int]] = defaultdict(dict)
    for j_start in junctions:
        seen = set()
        visit_iter: list[Point] = [j_start]
        steps = 0
        while visit_iter:
            new_visit_iter = []
            for point in visit_iter:
                x, y = point
                if x < 0 or x >= cols:
                    continue
                if y < 0 or y >= rows:
                    continue
                if lines[y][x] == "#":
                    continue
                if point in seen:
                    continue

                seen.add(point)

                if point != j_start and point in junctions:
                    junction_dist[j_start][point] = steps
                    continue

                new_visit_iter.extend([(x + dx, y + dy) for dx, dy in DIRECTIONS])

            visit_iter = new_visit_iter
            steps += 1

    # find the longest path from start to end using dfs with backtracking
    to_visit: deque[tuple[Point, int, list[Point], Point]] = deque(
        [(start, 0, [], to_try) for to_try in junction_dist[start].keys()]
    )
    max_end_dist = -1
    while to_visit:
        # for t in to_visit:
        #     print(t)
        # print()

        point, dist, visited, to_try = to_visit.pop()

        if point == end and dist > max_end_dist:
            max_end_dist = dist

        for to_try_next in junction_dist[to_try].keys():
            if to_try in visited:
                continue

            to_visit.append(
                (
                    to_try,
                    dist + junction_dist[point][to_try],
                    visited + [point],
                    to_try_next,
                )
            )

    return max_end_dist


if __name__ == "__main__":
    main()
