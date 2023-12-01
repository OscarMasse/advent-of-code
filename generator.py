import os
import shutil
import sys

import requests as requests

from utils import load_session_cookie


def generate(year: int, session_cookie=load_session_cookie()):
    for number in range(1, 26):
        print(f"Generating Day {number:02}")
        dir_name = f"day{number:02}"

        response = None
        if not os.path.isfile(f"{year}/{dir_name}/input.txt"):
            response = requests.get(f"https://adventofcode.com/{year}/day/{number}/input",
                                    headers={"cookie": f"session={session_cookie}"})
            if not response.status_code == 200:
                continue

        # Directory
        if not os.path.isdir(f"{year}/{dir_name}"):
            print(f"• Creating directory")
            os.makedirs(f"{year}/{dir_name}", exist_ok=True)

        # Input file
        if response:
            print(f"• Creating input.txt")
            with open(f"{year}/{dir_name}/input.txt", "wb") as file:
                file.write(response.content)

        # Python files
        for file_name in ["part_one.py", "part_two.py"]:
            if not os.path.isfile(f"{dir_name}/{file_name}"):
                print(f"• Copying {file_name}")
                shutil.copy(f"templates/{file_name}", f"{year}/{dir_name}/{file_name}")


if __name__ == "__main__":
    generate(int(sys.argv[1]))
