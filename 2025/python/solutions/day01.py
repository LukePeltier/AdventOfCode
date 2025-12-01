import re

EXAMPLE_ANSWER = 3
EXAMPLE_BONUS_ANSWER = 6


def solve(input_data: str):
    dial_point = 50
    zero_counter = 0
    for line in input_data.splitlines():
        regex_matches = re.search(r"^([LR])(\d+)$", line)

        assert regex_matches is not None

        direction = regex_matches.group(1)
        distance = int(regex_matches.group(2))

        true_offset = distance % 100

        match direction:
            case "L":
                dial_point = dial_point - true_offset
                if dial_point < 0:
                    dial_point = 100 + dial_point
            case "R":
                dial_point = dial_point + true_offset
                if dial_point > 100:
                    dial_point = 0 + (dial_point - 100)
                elif dial_point == 100:
                    dial_point = 0

            case _:
                raise ValueError("Invalid Direction")

        if dial_point == 0:
            zero_counter += 1

    return zero_counter


def bonus(input_data: str):
    dial_point = 50
    zero_counter = 0
    for line in input_data.splitlines():
        regex_matches = re.search(r"^([LR])(\d+)$", line)

        assert regex_matches is not None

        direction = regex_matches.group(1)
        distance = int(regex_matches.group(2))

        full_rotations = distance // 100
        true_offset = distance % 100

        zero_counter += full_rotations

        starting_dial_point = dial_point

        match direction:
            case "L":
                dial_point = dial_point - true_offset
                if dial_point < 0:
                    dial_point = 100 + dial_point
                    if starting_dial_point != 0:
                        zero_counter += 1
            case "R":
                dial_point = dial_point + true_offset
                if dial_point > 100:
                    dial_point = 0 + (dial_point - 100)
                    zero_counter += 1
                elif dial_point == 100:
                    dial_point = 0

            case _:
                raise ValueError("Invalid Direction")

        if dial_point == 0:
            zero_counter += 1

    return zero_counter
