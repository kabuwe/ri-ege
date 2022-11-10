a = int(input())
b = int(input())
c = 0
for i in range(a, b + 1):
    k = i*i*i % 10
    if k == 4 or k == 9:
        c += 1
print(c)
