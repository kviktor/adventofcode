s = 0

with open("input_1.txt") as a:
    numbers = zip(*[
        map(int, l.split())
        for l in a.readlines()
    ])
    for t in numbers:
        for a, b, c in zip(t[0::3], t[1::3], t[2::3]):
            if a + b > c and b + c > a and c + a > b:
                s += 1

print(s)
