s = 0
with open("input_1.txt") as a:
    for line in a.readlines():
        a, b, c = map(int, line.split())
        if a + b > c and b + c > a and c + a > b:
            s += 1
print(s)
