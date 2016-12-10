with open("input.txt") as f:
    data = f.read().strip()


i = 0
t = ""
while i < len(data):
    if data[i] == "(":
        par = i + data[i:].find(")")
        x, y = map(int, data[i + 1:par].split("x"))
        t += data[par + 1: par + 1 + x] * y
        i += x + (par - i + 1)
    else:
        t += data[i]
        i += 1

print(len(t))
