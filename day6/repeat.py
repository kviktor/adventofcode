from collections import defaultdict, Counter


with open("input.txt") as f:
    lines = f.read().splitlines()

code = [defaultdict(int) for l in lines[0]]

for l in lines:
    for idx, c in enumerate(l):
        code[idx][c] += 1

for c in code:
    # -1 for least, 0 for most common
    print(Counter(c).most_common()[-1][0][0], end="")
