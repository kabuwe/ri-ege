n = int(input())
t = True
while n > 9:
    x = n % 10
    n = n // 10
    c = n % 10
    if x != c:
        t = False
if t:
    print('YES')
else:
    print('NO')
