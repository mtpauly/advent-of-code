import argparse
import re
import random
import graphviz
import copy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")


def part_one(lines: list[str]) -> int:
    edges_orig: list[tuple[str, str]] = []
    nodes_set: set[str] = set()
    for line in lines:
        components = re.findall("([a-z]{3})", line)
        edges_orig.extend([(components[0], conn) for conn in components[1:]])
        for node in components:
            nodes_set.add(node)
    nodes_orig: list[str] = list(nodes_set)

    # https://en.wikipedia.org/wiki/Karger%27s_algorithm
    while True:
        nodes = nodes_orig.copy()
        edges = copy.deepcopy(edges_orig)
        random.shuffle(edges)

        maps_to: dict[str, str] = {node: node for node in nodes}
        node_count: dict[str, int] = {node: 1 for node in nodes}

        for _ in range(len(nodes) - 2):
            # draw an edge, repeating until valid
            while True:
                edge = edges.pop()
                node = maps_to[edge[0]]
                node_remove = maps_to[edge[1]]

                if node != node_remove:
                    break

            # contract nodes
            nodes.remove(node_remove)
            maps_to[node_remove] = node
            maps_to = {n: maps_to[maps_to[n]] for n in maps_to}
            node_count[node] += node_count[node_remove]

        cut = 0
        for edge in edges:
            node1 = maps_to[edge[0]]
            node2 = maps_to[edge[1]]
            if node1 != node2:
                cut += 1

        if cut == 3:
            return node_count[nodes.pop()] * node_count[nodes.pop()]


if __name__ == "__main__":
    main()
