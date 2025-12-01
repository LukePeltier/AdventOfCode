import argparse
import importlib
import time
from pathlib import Path


def format_duration(seconds: float) -> str:
    """Format duration in a human-readable way."""
    if seconds < 0.001:  # Less than 1ms
        return f"{seconds * 1_000_000:.1f}µs"
    elif seconds < 1.0:  # Less than 1s
        return f"{seconds * 1000:.2f}ms"
    else:  # 1s or more
        return f"{seconds:.2f}s"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("--bonus", action="store_true", help="Run the bonus solution")
    parser.add_argument("--example", "-e", action="store_true", help="Use example input instead of regular input")

    args = parser.parse_args()

    # Determine input file path
    if args.example:
        input_file = Path(__file__).parent / f"../inputs/examples/day{args.day:02d}.example"
    else:
        input_file = Path(__file__).parent / f"../inputs/inputs/day{args.day:02d}.input"

    input_file = input_file.resolve()

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return

    # Read input
    with open(input_file) as f:
        input_data = f.read()

    # Import and run solution
    try:
        solution = importlib.import_module(f"solutions.day{args.day:02d}")

        # Run solution with timing
        if args.bonus:
            start = time.perf_counter()
            result = solution.bonus(input_data)
            duration = time.perf_counter() - start
            label = f"Day {args.day} Bonus"
            expected_attr = "EXAMPLE_BONUS_ANSWER"
        else:
            start = time.perf_counter()
            result = solution.solve(input_data)
            duration = time.perf_counter() - start
            label = f"Day {args.day}"
            expected_attr = "EXAMPLE_ANSWER"

        timing_str = f"took {format_duration(duration)}"

        # Validate against expected answer if in example mode
        if args.example and hasattr(solution, expected_attr):
            expected = getattr(solution, expected_attr)
            if str(result) == str(expected):
                print(f"✓ {label}: {result}")
                print(f"  Status: PASSED | Time: {timing_str}")
            else:
                print(f"✗ {label}: FAILED")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")
                print(f"  Time:     {timing_str}")
        else:
            if args.example:
                print(f"{label}: {result}")
                print(f"  Time: {timing_str} (no validation)")
            else:
                print(f"{label}: {result}")
                print(f"  Time: {timing_str}")
    except ModuleNotFoundError:
        print(f"Solution for day {args.day} not found")


if __name__ == "__main__":
    main()
