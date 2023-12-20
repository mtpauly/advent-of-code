import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().strip()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: str) -> int:
    rules, parts = lines.split("\n\n")

    rule_map: dict[str, list] = {}  # name: list of conditons
    for rule in rules.splitlines():
        name, conditions = re.findall("([a-z]+)\\{(.+)\\}", rule)[0]

        cond_str_list = conditions.split(",")
        cond_list = []
        for cond in cond_str_list[:-1]:
            cat, comp, num, maps_to = re.findall(
                "([xmas])([<>])(\\d+)\\:([a-zAR]+)", cond
            )[0]
            cond_list.append((cat, comp, int(num), maps_to))
        cond_list.append(cond_str_list[-1])

        rule_map[name] = cond_list

    rule_map["R"] = ["R"]
    rule_map["A"] = ["A"]

    total = 0
    for part in parts.splitlines():
        x, m, a, s = re.findall("\\{x=(\\d+),m=(\\d+),a=(\\d+),s=(\\d+)\\}", part)[0]
        part_dict = {
            "x": int(x),
            "m": int(m),
            "a": int(a),
            "s": int(s),
        }

        workflow = rule_map["in"]
        while True:
            for cat, comp, num, maps_to in workflow[:-1]:
                if comp == "<" and part_dict[cat] < num:
                    workflow = rule_map[maps_to]
                    break
                if comp == ">" and part_dict[cat] > num:
                    workflow = rule_map[maps_to]
                    break
            else:
                if workflow[-1] in ("R", "A"):
                    if workflow[-1] == "A":
                        total += sum(list(part_dict.values()))
                    break
                else:
                    workflow = rule_map[workflow[-1]]

    return total


def part_two(lines: str) -> int:
    rules, _ = lines.split("\n\n")

    rule_map: dict[str, list] = {}  # name: list of conditons
    for rule in rules.splitlines():
        name, conditions = re.findall("([a-z]+)\\{(.+)\\}", rule)[0]

        cond_str_list = conditions.split(",")
        cond_list = []
        for cond in cond_str_list[:-1]:
            cat, comp, num, maps_to = re.findall(
                "([xmas])([<>])(\\d+)\\:([a-zAR]+)", cond
            )[0]
            cond_list.append((cat, comp, int(num), maps_to))
        cond_list.append(cond_str_list[-1])

        rule_map[name] = cond_list

    rule_map["R"] = ["R"]
    rule_map["A"] = ["A"]

    n_accepted = 0

    ranges = [
        (
            rule_map["in"],  # workflow to process
            {
                "x": (1, 4001),  # min, max (not inclusive)
                "m": (1, 4001),
                "a": (1, 4001),
                "s": (1, 4001),
            },
        )
    ]
    while ranges:
        workflow, range_dict = ranges.pop()

        if len(workflow) == 1:
            if workflow[0] == "R":
                continue
            if workflow[0] == "A":
                range_total = 1
                for rmin, rmax in range_dict.values():
                    range_total *= rmax - rmin
                n_accepted += range_total
                continue

            ranges.append((rule_map[workflow[0]], range_dict))
            continue

        cat, comp, num, maps_to = workflow[0]
        cat_min = range_dict[cat][0]
        cat_max = range_dict[cat][1]

        if comp == "<":
            # range above
            if cat_min >= num:
                ranges.append((workflow[1:], range_dict))
                continue
            # range below
            elif cat_max <= num:
                ranges.append((rule_map[maps_to], range_dict))
                continue
            # range split
            else:
                range_dict_above = range_dict.copy()
                range_dict_above[cat] = (num, cat_max)
                ranges.append((workflow[1:], range_dict_above))
                range_dict_below = range_dict.copy()
                range_dict_below[cat] = (cat_min, num)
                ranges.append((rule_map[maps_to], range_dict_below))
                continue
        if comp == ">":
            # range above
            if cat_min >= num + 1:
                ranges.append((rule_map[maps_to], range_dict))
                continue
            # range below
            elif cat_max <= num + 1:
                ranges.append((workflow[1:], range_dict))
                continue
            # range split
            else:
                range_dict_above = range_dict.copy()
                range_dict_above[cat] = (num + 1, cat_max)
                ranges.append((rule_map[maps_to], range_dict_above))
                range_dict_below = range_dict.copy()
                range_dict_below[cat] = (cat_min, num + 1)
                ranges.append((workflow[1:], range_dict_below))
                continue

    return n_accepted


if __name__ == "__main__":
    main()
