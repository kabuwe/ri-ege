firststr = input()
secondstr = input()
thirststr = input()
a = len(firststr)
b = len(secondstr)
c = len(thirststr)
if b - a == c - b or b - c == a - b or a - c == b - a or a - b == c - a or c - a == b - c or c - b == a - c:
    print('YES')
else:
    print('NO')
