from loguru import logger

EXAMPLE_ANSWER = 3
# EXAMPLE_BONUS_ANSWER = 6


class Range:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max


def solve(input_data: str):
    sum = 0
    raw_split = input_data.split("\n\n")
    raw_ranges = raw_split[0].split()
    raw_vals = raw_split[1].split()
    ids = [int(val) for val in raw_vals]
    for line in raw_ranges:
        vals = line.split("-", 1)
        min_val = int(vals[0])
        max_val = int(vals[1])
        for id in ids.copy():
            if id >= min_val and id <= max_val:
                sum += 1
                ids.remove(id)

    return sum


def bonus(input_data: str):
    pass
