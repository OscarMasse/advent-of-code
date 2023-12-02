import re

from utils import load_input


def solve():
    input_ = load_input()

    pattern = re.compile(r"Game (\d+): (.+)")

    sum_ = 0
    for game in input_.splitlines():
        color_maxes = {"red": 0, "green": 0, "blue": 0}

        split = pattern.match(game)
        game_number = int(split.group(1))
        groups = split.group(2).split("; ")
        for group in groups:
            cubes = group.split(", ")
            for cube in cubes:
                cube_split = cube.split()
                count = int(cube_split[0])
                color = cube_split[1]
                if color_maxes[color] < count:
                    color_maxes[color] = count

        if (
            color_maxes["red"] <= 12
            and color_maxes["green"] <= 13
            and color_maxes["blue"] <= 14
        ):
            sum_ += game_number

    print(sum_)


if __name__ == "__main__":
    solve()
