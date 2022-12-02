b, k, t, s = 10, 5, 0.5, 100
for i in range(1, s // b + 1):
    for x in range(1, s // k + 1):
        for y in range(1, int(s // t + 1)):
            if 10 * i + 5 * x + 0.5 * y == 100 and i + x + y == 100:
                print(i, x, y)
