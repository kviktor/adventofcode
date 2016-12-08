with open("input.txt") as f:
    commands = f.read().splitlines()

width = 50
height = 6
display = []
ll = lambda *a: [list(b) for b in zip(*a)]  # noqa

for i in range(height):
    display.append(["."] * width)


for c in commands:
    if c.startswith("rect"):
        w, h = int(c[c.find(" "):c.find("x")]), int(c[c.find("x") + 1:])
        for row in range(h):
            display[row][:w] = "#" * w
    else:
        if "column" in c:
            x, by = int(c[c.find("=") + 1:c.find("b")]), int(c[c.rfind(" "):])
            display = ll(*display)
            display[x] = display[x][-by:] + display[x][:-by]
            display = ll(*display)
        else:
            y, by = int(c[c.find("=") + 1:c.find("b")]), int(c[c.rfind(" "):])
            display[y] = display[y][-by:] + display[y][:-by]

for i in display:
    print("".join(i))

print(sum([l.count("#") for l in display]))
