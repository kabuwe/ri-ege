a, b, c, s = 28, 30, 31, 365
for n in range(s // a + 1):
    for k in range(s // b + 1):
        for m in range(s // c + 1):
            if 28 * n + 30 * k + 31 * m == s:
                print(n, k, m)
