c = 0
for i in range(1, 11):
    a = int(input())
    if a % 2 == 0:
        c += 1
if c == 10:
    print('YES')
else:
    print('NO')