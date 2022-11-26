n = int(input())
e = n
c= 0
while(n > 0):
    v = n % 10
    c = c * 10 + v
    n = n // 10
if e == c:
    print('YES')
else:
    print("NO")