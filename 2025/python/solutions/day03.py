from loguru import logger

EXAMPLE_ANSWER = 357
EXAMPLE_BONUS_ANSWER = 3121910778619


def find_largest_digit(batteries: list[str], place: int) -> tuple[int, int]:
    batteries = batteries[: len(batteries) - place]
    val_batteries = [int(batt) for batt in batteries]
    largest_battery = max(val_batteries)

    # logger.debug(f"Found largest battery: [{largest_battery}]")

    return (
        largest_battery,
        val_batteries.index(largest_battery),
    )


def solve(input_data: str):
    sum = 0
    for bank in input_data.split():
        batteries = list(bank)
        left_battery_val, left_battery_index = find_largest_digit(batteries, 1)
        batteries = batteries[left_battery_index + 1 :]
        right_battery_val, _ = find_largest_digit(batteries, 0)

        jolts = int(f"{left_battery_val}{right_battery_val}")

        sum += jolts

    return sum


def bonus(input_data: str):
    sum = 0
    for bank in input_data.split():
        str_batteries = list(bank)
        batteries = [int(batt) for batt in str_batteries]
        logger.debug(f"Bank: {batteries}")
        used_batteries = []
        skipped_batteries = 0
        i = 0
        while len(used_batteries) < 12:
            batteries_to_remove = len(batteries) - 12 - skipped_batteries
            logger.debug(f"Batteries left that i need to remove: {batteries_to_remove}")
            # whats the biggest num we can get on the left with max removals
            batt_slice = batteries[i : i + batteries_to_remove + 1]
            logger.debug(f"Checking {batt_slice}")
            left_digit = max(batt_slice)
            left_digit_index = batt_slice.index(left_digit)

            used_batteries.append(left_digit)
            skipped_batteries += left_digit_index

            i += left_digit_index + 1
            continue

        logger.debug(f"Using: {used_batteries}")
        jolts = int("".join(map(str, used_batteries)))

        sum += jolts

    return sum
