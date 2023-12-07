from typing import List
import argparse
from collections import Counter


JACK = "J"
JOKER = "j"
CARD_VALUES = {
    "j": 1,  # joker has the lowest value
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
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
    hands = []  # (ordering, bid)
    for line in lines:
        hand, bid = line.split()

        hand_values = [CARD_VALUES[card] for card in hand]
        hand_counts = sorted([hand.count(card) for card in hand], reverse=True)

        hands.append((hand_counts + hand_values, int(bid)))

    hands.sort()

    total = [i * bid for i, (_, bid) in enumerate(hands, start=1)]
    return sum(total)


def part_two(lines: List[str]) -> int:
    hands = []  # (ordering, bid)
    for line in lines:
        hand, bid = line.split()
        hand = hand.replace(JACK, JOKER)
        hand_values = [CARD_VALUES[card] for card in hand]

        counter = Counter(hand.replace(JOKER, ""))
        max_card = counter.most_common(1)[0][0] if counter else JOKER
        hand = hand.replace(JOKER, max_card)
        hand_counts = sorted([hand.count(card) for card in hand], reverse=True)

        hands.append((hand_counts + hand_values, int(bid)))

    hands.sort()

    total = [i * bid for i, (_, bid) in enumerate(hands, start=1)]
    return sum(total)


if __name__ == "__main__":
    main()
