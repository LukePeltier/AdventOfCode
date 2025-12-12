from loguru import logger

EXAMPLE_ANSWER = 3
EXAMPLE_BONUS_ANSWER = 14


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
    count = 0
    raw_split = input_data.split("\n\n")
    raw_ranges = raw_split[0].split()
    raw_ranges = [tup.split("-", 1) for tup in raw_ranges]
    raw_ranges = [(int(tup[0]), int(tup[1])) for tup in raw_ranges]

    reduction_happened = True
    final_ranges: list[tuple[int, int]] = []

    while reduction_happened:
        for line in raw_ranges:
            min_val = line[0]
            max_val = line[1]
            needs_new_range = True
            for i, seen_range in enumerate(final_ranges):
                # Encapsulated in range
                if min_val >= seen_range[0] and max_val <= seen_range[1]:
                    needs_new_range = False
                    break
                # Encompasses range
                elif min_val <= seen_range[0] and max_val >= seen_range[1]:
                    final_ranges[i] = (min_val, max_val)
                    needs_new_range = False
                    break
                # Left intersect
                elif min_val <= seen_range[0] and max_val >= seen_range[0]:
                    final_ranges[i] = (min_val, seen_range[1])
                    needs_new_range = False
                    break
                # Right intersect
                elif max_val >= seen_range[1] and min_val <= seen_range[1]:
                    final_ranges[i] = (seen_range[0], max_val)
                    needs_new_range = False
                    break
            if needs_new_range:
                new_range = (min_val, max_val)
                final_ranges.append(new_range)
        if len(final_ranges) == len(raw_ranges):
            reduction_happened = False
        else:
            raw_ranges = final_ranges
            final_ranges = []

    for final_range in final_ranges:
        count += final_range[1] - final_range[0] + 1
    return count
