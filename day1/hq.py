route = "R8, R4, R4, R8".split(", ")


""" 0
    |
 3__.__1
    |
    2
"""
face = 0
visited = [(0, 0)]


def extract(p):
    return 1 if p[0] == "R" else -1, int(p[1:])


for r in route:
    c, steps = extract(r)
    face = (face + c) % 4
    for i in range(steps):
        x, y = visited[-1]
        xn, yn = {0: lambda x, y: (x, y + 1),
                  1: lambda x, y: (x + 1, y),
                  2: lambda x, y: (x, y - 1),
                  3: lambda x, y: (x - 1, y)}.get(face)(x, y)

        if (xn, yn) in visited:
            print(abs(xn) + abs(yn))
            1 / 0  # ¯\(ツ)/¯
        visited.append((xn, yn))
