n = int(input())
c = 1
b = 0
for i in range(1, n + 1):
    a = int(input())
    if a % 2 == 1:
        c *= a
    else:
        b += a
if c > b:
    print(c / b)
else:
    print(b / c)
