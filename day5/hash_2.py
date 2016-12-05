from hashlib import md5

initial = "abc"
password = [None] * 8
idx = 0

while None in password:
    h = md5(("%s%d" % (initial, idx)).encode()).hexdigest()
    position = h[5]
    if h[:5] == "0" * 5 and position.isdigit() and position < "8":
            position = int(position)
            password[position] = password[position] or h[6]
            print(h, password)

    idx += 1

print("".join(password))
