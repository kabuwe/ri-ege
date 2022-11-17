n = int(input())
for i in range(1, n + 1):
    a = int(input())
    if a % 2 == 1 and len(str(a)) == 3:
        a+=a
        c = a / len(a)
print(c)
