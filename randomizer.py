import sys
import random


def get_random_line(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        if not lines:
            print("The file is empty.")
            return

        print(random.choice(lines))

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    if len(sys.argv) < 2:
        filename = "names.txt"
    else:
        filename = sys.argv[1]

    get_random_line(filename)


if __name__ == "__main__":
    main()
