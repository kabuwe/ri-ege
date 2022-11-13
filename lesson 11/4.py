m = int(input())
p = int(input())
n = int(input())
c = m
for i in range(1, n + 1):
    c *= (1 + p / 100)
    print(c)
