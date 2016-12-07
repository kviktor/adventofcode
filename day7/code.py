with open("input.txt") as f:
    lines = f.read().splitlines()


def abba(text):
    a, b, c, d = list(text)
    return a == d and b == c and a != b


s = 0
for l in lines:
    bracket = have = False
    for i in range(len(l) - 3):
        if l[i] in ("[", "]"):
            bracket = l[i] == "["

        is_abba = abba(l[i:i+4])
        if is_abba and bracket:
            have = False
            break
        elif is_abba:
            have = True

    s += have

print(s)
