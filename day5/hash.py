from hashlib import md5

initial = "abc"
password = ""
idx = 0

while len(password) < 8:
    h = md5(("%s%d" % (initial, idx)).encode()).hexdigest()
    if h[:5] == "0" * 5:
        password += h[5]
        print(h, password)

    idx += 1
