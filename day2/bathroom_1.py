# flake8: noqa
instructions = ["ULL", "RRDDD", "LURDL", "UUUUD", ]

idx = 5
commands = {
    "U": -3,
    "R": 1,
    "L": -1,
    "D": 3,
}


def can_step(idx, step):
    return not (
        (idx in [3, 6, 9] and step == 1) or
        (idx in [1, 4, 7] and step == -1) or
        (idx in [1, 2, 3] and step == -3) or
        (idx in [7, 8, 9] and step == 3)
    )


for instruction in instructions:
    for i in instruction:
        step = commands.get(i)
        if can_step(idx, step):
            idx += step

    print(idx, end="")
