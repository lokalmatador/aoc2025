import os
import re

base_link = "https://github.com/lokalmatador/aoc2024/blob/master/src/"


def parse(e):
    name = e.replace(".py", "")
    match = re.match(r"([a-zA-Z]+)(\d+)", name)
    day, number = match.groups()
    day = day.capitalize()
    return f"[{day} {number}]({base_link}{e})"


solutions = filter(lambda x: ".py" in x and "init" not in x and "runner" not in x, os.listdir("src"))

readme_content = "# Advent of code\nProblems list:\n"
tmp = [f"{i + 1}. {parse(e)}" for i, e in enumerate(sorted(solutions))]

readme_content += "\n".join(tmp)

with open("README.md", "w") as f:
    f.write(
        readme_content
    )
