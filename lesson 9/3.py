a = input()
b = input()
c = input()
m = len(a)
v = len(b)
k = len(c)
if m == v or m == k or v == k or m == v == k:
    print('Не соответствует условию задачи')
else:
    print(max([a, b, c], key=len))
    print(min([a, b, c], key=len))
