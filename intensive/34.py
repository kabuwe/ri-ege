n = int(input())
flag = True

while n > 9:
    last = n % 10
    n = n // 10
    second = n % 10
    if last > second:
        flag = False
if flag:
    print('YES')
else:
    print('NO')