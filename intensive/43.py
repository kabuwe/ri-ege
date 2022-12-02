n = int(input())
c = 0
for y in range(1, n + 1):
    for x in range(y):
        c += 1
        print(c, end=' ')
    print()