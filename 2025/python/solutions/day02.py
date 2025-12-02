import math
from functools import reduce

EXAMPLE_ANSWER = 1227775554
EXAMPLE_BONUS_ANSWER = 4174379265


def is_id_valid(num: int) -> bool:
    num_len = int(math.log10(num)) + 1

    if num_len % 2 != 0:
        return True

    num_parts = split_num(num, 2)

    left_num_str = num_parts[0]
    right_num_str = num_parts[1]

    return left_num_str != right_num_str


def get_next_invalid_id(num: int) -> int:
    left_num_str, right_num_str = split_num(num, 2)
    left_num = int(left_num_str)
    right_num = int(right_num_str)
    if right_num >= left_num:
        left_num += 1

    return int(f"{left_num}{left_num}")


def solve(input_data: str):
    # split input into range strings
    ranges = [range.strip() for range in input_data.split(",")]
    print(f"{ranges}")

    sum = 0

    for range in ranges:
        starting_value = int(range.split("-")[0])
        ending_value = int(range.split("-")[1])

        # slice starting value in half, then get to nearest value which is the same pair
        current_value = starting_value
        while current_value <= ending_value:
            current_value_len = int(math.log10(current_value)) + 1

            if current_value_len % 2 != 0:
                # get to the next power of ten
                current_value = 10**current_value_len
                continue

            if not is_id_valid(current_value):
                sum += current_value

            current_value = get_next_invalid_id(current_value)

    return sum


def is_id_really_valid(num: int) -> bool:
    num_len = int(math.log10(num)) + 1

    # get all factors of num_len
    num_factors = factors(num_len)
    for fac in num_factors:
        if fac == 1:
            continue
        if num_len % fac != 0:
            continue
        num_parts = split_num(num, fac)
        if all_equal(num_parts):
            return False

    return True


def split_num(num: int, divisor: int) -> list[str]:
    num_len = int(math.log10(num)) + 1
    if num_len % divisor != 0:
        raise Exception(f"Can't split num with {num_len} digits into {divisor} parts")
    num_str = str(num)
    part_size = num_len // divisor
    parts = []
    for i in range(0, num_len, part_size):
        part = num_str[i : i + part_size]
        parts.append(part)
    return parts


def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


def factors(n) -> set[int]:
    return set(
        reduce(
            list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if not n % i)
        )
    )


def sum_invalid_in_range(start: int, end: int) -> int:
    """Second method, way faster than the first. Inspired by some ideas from people online after solving the bonus myself through the above method. Other is a bit more brute force"""
    start_len = int(math.log10(start)) + 1
    end_len = int(math.log10(end)) + 1
    if start_len != end_len:
        return sum_invalid_in_range(start, (10**start_len) - 1) + sum_invalid_in_range(
            ((10**end_len) / 10), end
        )
    # print(f"Checking range: {start} - {end}")
    sum = 0
    numbers_used = set([])
    # generate all invalid nums for length
    # get all factors of num_len
    num_factors = factors(start_len)
    for fac in num_factors:
        if fac == 1:
            continue
        part_length = start_len // fac
        # print(f"Checking part_length: {part_length}")
        # print(f"Num of splits: {fac}")
        starting_part = 10 ** (part_length - 1)
        ending_part = 10**part_length
        for i in range(starting_part, ending_part):
            split_num: list[str] = [str(i)] * fac
            num_str = "".join(split_num)
            num = int(num_str)
            if num >= start and num <= end and num not in numbers_used:
                # print(f"Generated invalid id: {num} for range {start} - {end}")
                sum += num
                numbers_used.add(num)

    return sum


def bonus(input_data: str):
    ranges = [range.strip() for range in input_data.split(",")]
    sum = 0

    for range in ranges:
        starting_value = int(range.split("-")[0])
        ending_value = int(range.split("-")[1])
        sum += sum_invalid_in_range(starting_value, ending_value)

    return sum
    pass
