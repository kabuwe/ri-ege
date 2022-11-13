n = int(input())
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
print(c)
for i in range(1, n + 1):
    if n % i == 0:
        h = 0
if c > 2:
    print(i, i / 2, i / 4)
else:
    print(i, i / 2)
