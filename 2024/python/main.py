import argparse
from solutions.day01 import solve as day01solve, bonus as day01bonus
from solutions.day06 import solve as day06solve, bonus as day06bonus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("--bonus", action="store_true", help="Run the bonus solution")

    args = parser.parse_args()

    match args.day:
        case 1:
            if args.bonus:
                day01bonus()
            else:
                day01solve()
        case 6:
            if args.bonus:
                day06bonus()
            else:
                day06solve()


if __name__ == "__main__":
    main()
