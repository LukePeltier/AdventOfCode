import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("--bonus", action="store_true", help="Run the bonus solution")

    args = parser.parse_args()

    match args.day:
        case _:
            print("Day not found")


if __name__ == "__main__":
    main()
