import argparse
import re
import math


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().strip().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    modules = {}  # name: (prefix, data, destinations)
    for line in lines:
        if line[:3] == "bro":
            modules["broadcast"] = [None, None, line.split("-> ")[1].split(", ")]
            continue

        prefix, name, dest = re.findall("([%&])([a-z]+) -> (.+)", line)[0]

        if prefix == "%":
            # data boolean is False for off, True for on
            modules[name] = [prefix, False, dest.split(", ")]
        elif prefix == "&":
            # data dict is { name: bool } where bool is False for low, True for high
            modules[name] = [prefix, {}, dest.split(", ")]

    # set up conjuction module data
    for name, (prefix, data, dest) in modules.items():
        for d in dest:
            if d not in modules:
                continue

            if modules[d][0] == "&":
                modules[d][1][name] = False

    # run 1000 iterations
    low_count = 0
    high_count = 0
    for _ in range(1000):
        low_count += 1  # for the button pulse

        to_fire: list[tuple[str, bool, str]] = [
            (d, False, "broadcast") for d in modules["broadcast"][2]
        ]
        while to_fire:
            new_to_fire = []
            for name, high, sender in to_fire:
                if high:
                    high_count += 1
                else:
                    low_count += 1

                if name not in modules:
                    continue

                prefix, data, dest = modules[name]

                # flip-flop
                if prefix == "%":
                    if not high:
                        new_to_fire.extend([(d, not data, name) for d in dest])
                        modules[name][1] = not data

                # conjunction
                elif prefix == "&":
                    data[sender] = high
                    new_to_fire.extend(
                        [(d, not all(data.values()), name) for d in dest]
                    )

            to_fire = new_to_fire

    return high_count * low_count


def part_two(lines: list[str]) -> int:
    modules = {}  # name: (prefix, data, destinations)
    for line in lines:
        if line[:3] == "bro":
            modules["broadcast"] = [None, None, line.split("-> ")[1].split(", ")]
            continue

        prefix, name, dest = re.findall("([%&])([a-z]+) -> (.+)", line)[0]

        if prefix == "%":
            # data boolean is False for off, True for on
            modules[name] = [prefix, False, dest.split(", ")]
        elif prefix == "&":
            # data dict is { name: bool } where bool is False for low, True for high
            modules[name] = [prefix, {}, dest.split(", ")]

    # set up conjuction module data
    rx_prev = []
    for name, (_, _, dest) in modules.items():
        for d in dest:
            if d == "rx":
                rx_prev.append(name)

            if d not in modules:
                continue

            if modules[d][0] == "&":
                modules[d][1][name] = False

    # find the independent subgraphs
    #   note that there are 4 distinct subgraphs that connect to a conjuction node
    #   which in turn connects to rx. this structure can only (easily?) be found by
    #   inspecting the graph. see:
    #   https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Fehu8t3oy5e7c1.png
    assert len(rx_prev) == 1
    cycles: dict[str, int] = {name: 0 for name in modules[rx_prev[0]][1].keys()}

    i = 0
    while not all(cycles.values()):
        i += 1

        to_fire: list[tuple[str, bool, str]] = [
            (d, False, "broadcast") for d in modules["broadcast"][2]
        ]
        while to_fire:
            new_to_fire = []
            for name, high, sender in to_fire:
                if name in cycles and not cycles[name] and not high:
                    cycles[name] = i
                if name not in modules:
                    continue

                prefix, data, dest = modules[name]

                # flip-flop
                if prefix == "%":
                    if not high:
                        new_to_fire.extend([(d, not data, name) for d in dest])
                        modules[name][1] = not data

                # conjunction
                elif prefix == "&":
                    data[sender] = high
                    new_to_fire.extend(
                        [(d, not all(data.values()), name) for d in dest]
                    )

            to_fire = new_to_fire

    return math.lcm(*cycles.values())


if __name__ == "__main__":
    main()
