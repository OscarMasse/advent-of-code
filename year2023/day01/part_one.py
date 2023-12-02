from utils import load_input


def solve():
    input_ = load_input()

    numbers = []
    for line in input_.splitlines():
        digits = [digit for digit in line if digit.isdigit()]
        numbers.append(int(digits[0] + digits[-1]))

    print(sum(numbers))


if __name__ == "__main__":
    solve()
