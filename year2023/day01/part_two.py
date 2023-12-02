import re

from utils import load_input

STR_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

NUMBERS_PATTERN = r"one|two|three|four|five|six|seven|eight|nine"


def solve():
    input_ = load_input()

    numbers = []
    for line in input_.splitlines():
        first_digit = re.search(r"\d|" + NUMBERS_PATTERN, line).group()
        last_digit = re.search(r"\d|" + NUMBERS_PATTERN[::-1], line[::-1]).group()
        numbers.append(
            int(
                (first_digit if first_digit.isdigit() else STR_TO_DIGIT[first_digit])
                + (
                    last_digit
                    if last_digit.isdigit()
                    else STR_TO_DIGIT[last_digit[::-1]]
                )
            )
        )

    print(sum(numbers))


if __name__ == "__main__":
    solve()
