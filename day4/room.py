from collections import Counter

with open("input.txt") as f:
    data = f.read().splitlines()


def extract(d):
    return (
        d[0:d.rfind("-")].replace("-", ""),
        int(d[d.rfind("-") + 1:d.rfind("[")]),
        d[d.find("[") + 1:d.rfind("]")]
    )


def shift_char(c, n):
    return chr(((ord(c) - ord('a') + n) % (ord('z') - ord('a') + 1)) + ord('a'))


def shift_text(t, n):
    return "".join([shift_char(c, n) for c in t])


s = 0
for d in data:
    name, sector, checksum = extract(d)
    key = "".join([k for k, v in sorted(Counter(name).most_common(),
                                        key=lambda e: (-e[1], e[0]))[:5]])
    if key == checksum:
        s += sector

        # part2
        if shift_text(name, sector).startswith("northpole"):
            print(sector)

print(s)
