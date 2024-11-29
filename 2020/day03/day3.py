import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = file.read().splitlines()

    print(f"part 1 solution: {part_one(lines)}")
    print(f"part 2 solution: {part_two(lines)}")


def part_one(lines: list[str]) -> int:
    def c(off, skip):
        out = 0
        l = len(lines[0])

        index = 0
        for line in lines[::2] if skip else lines:
            box = line[index % l]
            index += off
            out += box == '#'

        return out

    total = 1
    total *= c(1, False)
    total *= c(3, False)
    total *= c(5, False)
    total *= c(7, False)
    total *= c(1, True)

    return total



def part_two(lines: list[str]) -> int:

    return 0


if __name__ == "__main__":
    main()
