import argparse
import re


COLOR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
args = parser.parse_args()

with open(args.input_file, "r") as file:
    lines = file.readlines()

part1_total = 0
part2_total = 0
for line in lines:
    game_num_match = re.match("Game (\\d+):", line)
    if not game_num_match or len(game_num_match.groups()) == 0:
        raise ValueError()
    game_num = int(game_num_match.groups()[0])

    valid_game = True
    color_product = 1
    for color, limit in COLOR_LIMITS.items():
        color_counts = re.findall(f"(\\d+) {color}", line)

        max_count = max([int(c) for c in color_counts])
        if max_count > limit:
            valid_game = False

        color_product *= max_count

    if valid_game:
        part1_total += game_num

    part2_total += color_product

print(f"part 1 solution: {part1_total}")
print(f"part 2 solution: {part2_total}")
