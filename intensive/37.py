n = input()
flag = 'true'
c = n[-1]
b = n[-2]
v = int(n)
while v > 0:
    if int(c) % 2 == 1 and int(b) % 2 == 0:
        flag = 1
    else:
        flag = 2
    if int(c) % 2 == 0 and int(b) % 2 == 1:
        flag = 1
    else:
        flag = 2
    v //= 10
if flag == 1:
    print('YES')
else:
    print('NO')
