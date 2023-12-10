import argparse
from typing import List


PIPE_CONNECTIONS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "F": [(0, 1), (1, 0)],
    "7": [(0, -1), (1, 0)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: List[str]) -> int:
    n_row = len(lines)
    n_col = len(lines[0])

    # parse graph
    graph = {}  # (row, col): [(row, col),]
    start_ix = None
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                start_ix = (row, col)
                continue

            if char in PIPE_CONNECTIONS:
                connects_to = []
                for drow, dcol in PIPE_CONNECTIONS[char]:
                    conn_row = row + drow
                    conn_col = col + dcol
                    if conn_row < 0 or conn_row >= n_row:
                        continue
                    if conn_col < 0 or conn_col >= n_col:
                        continue

                    connects_to.append((conn_row, conn_col))
                graph[(row, col)] = connects_to

    # adding start
    assert start_ix
    connects_to = []
    row, col = start_ix
    for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        conn_row = row + drow
        conn_col = col + dcol
        if conn_row < 0 or conn_row >= n_row:
            continue
        if conn_col < 0 or conn_col >= n_col:
            continue
        connects_to.append((conn_row, conn_col))
    graph[start_ix] = connects_to

    # prune graph
    for ix in list(graph.keys()):
        connects_to: List = graph[ix]
        for cix in connects_to[:]:
            if cix not in graph:
                connects_to.remove(cix)
            elif ix not in graph[cix]:
                connects_to.remove(cix)
        if not connects_to:
            del graph[ix]

    # run bfs
    steps = 0
    seen = set()
    to_visit = [start_ix]
    while True:
        new_to_visit = []
        for next_ix in to_visit:
            for conn_ix in graph[next_ix]:
                if conn_ix not in seen:
                    new_to_visit.append(conn_ix)

            seen.add(next_ix)

        if not new_to_visit:
            break

        to_visit = new_to_visit
        steps += 1

    return steps


def part_two(lines: List[str]) -> int:
    n_row = len(lines)
    n_col = len(lines[0])

    # parse graph
    graph = {}  # (row, col): [(row, col),]
    start_ix = None
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                start_ix = (row, col)
                continue

            if char in PIPE_CONNECTIONS:
                connects_to = []
                for drow, dcol in PIPE_CONNECTIONS[char]:
                    conn_row = row + drow
                    conn_col = col + dcol
                    if conn_row < 0 or conn_row >= n_row:
                        continue
                    if conn_col < 0 or conn_col >= n_col:
                        continue

                    connects_to.append((conn_row, conn_col))
                graph[(row, col)] = connects_to

    # adding start
    assert start_ix
    connects_to = []
    row, col = start_ix
    for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        conn_row = row + drow
        conn_col = col + dcol
        if conn_row < 0 or conn_row >= n_row:
            continue
        if conn_col < 0 or conn_col >= n_col:
            continue
        connects_to.append((conn_row, conn_col))
    graph[start_ix] = connects_to

    # prune graph
    for ix in list(graph.keys()):
        connects_to: List = graph[ix]
        for cix in connects_to[:]:
            if cix not in graph:
                connects_to.remove(cix)
            elif ix not in graph[cix]:
                connects_to.remove(cix)
        if not connects_to:
            del graph[ix]

    # run bfs
    bfs_seen = set()
    to_visit = [start_ix]
    while True:
        new_to_visit = []
        for next_ix in to_visit:
            for conn_ix in graph[next_ix]:
                if conn_ix not in bfs_seen:
                    new_to_visit.append(conn_ix)

            bfs_seen.add(next_ix)

        if not new_to_visit:
            break

        to_visit = new_to_visit

    # create a padded graph
    loop_pad = set()  # list of indices that are in the loop
    for (row, col), connects_to in graph.items():
        if (row, col) not in bfs_seen:
            continue
        for crow, ccol in connects_to:
            drow = crow - row
            dcol = ccol - col
            loop_pad.add((3 * row + drow, 3 * col + dcol))

        loop_pad.add((3 * row, 3 * col))

    # find interior points
    def dfs(ix):
        to_visit = [ix]
        seen = set()

        contained = True
        while to_visit:
            row, col = to_visit.pop()

            if (row, col) in loop_pad:
                continue
            if (row, col) in seen:
                continue

            seen.add((row, col))

            for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                row_new = row + drow
                col_new = col + dcol

                if row_new < 0 or row_new >= 3 * n_row:
                    contained = False
                    continue
                if col_new < 0 or col_new >= 3 * n_col:
                    contained = False
                    continue

                to_visit.append((row_new, col_new))

        return seen, contained

    all_points = set()
    for row in range(n_row * 3):
        for col in range(n_col * 3):
            if (row, col) not in loop_pad:
                all_points.add((row, col))

    interior = set()
    while all_points:
        ix = all_points.pop()
        seen, contained = dfs(ix)

        all_points -= seen
        if contained:
            interior = interior.union(seen)

    # filter points for centers
    count = 0
    for row, col in interior:
        if row % 3 == 0 and col % 3 == 0:
            count += 1

    return count


if __name__ == "__main__":
    main()
