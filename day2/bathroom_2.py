# flake8: noqa
instructions = ["ULL", "RRDDD", "LURDL", "UUUUD", ]

idx = 11
commands = {
    "U": -5, "D": 5,
    "R": 1, "L": -1,
}
translate = {
    3: 1, 7: 2, 8: 3, 9: 4, 11: 5, 12: 6, 13: 7, 14: 8, 15: 9,
    17: 10, 18: 11, 19: 12, 23: 13
}

for instruction in instructions:
    for i in instruction:
        step = commands.get(i)
        if translate.get(idx + step):
            idx += step

    print("%x".upper() % translate.get(idx), end="")
