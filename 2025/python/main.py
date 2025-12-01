import argparse
import importlib
from pathlib import Path


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

        if args.bonus:
            result = solution.bonus(input_data)
            print(f"Day {args.day} Bonus: {result}")
        else:
            result = solution.solve(input_data)
            print(f"Day {args.day}: {result}")
    except ModuleNotFoundError:
        print(f"Solution for day {args.day} not found")


if __name__ == "__main__":
    main()
