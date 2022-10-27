a, b, t = [int(i) for i in input().split()]
assert 1 <= a <= 2 * 10 ** 9 or 1 <= b <= 2 * 10 ** 9 or 0 <= t <= 2 * 10 ** 18, 'неверное число'
if a <= t:
    g = t // a
else:
    g = 1
if b <= t:
    x = t // b
else:
    x = 1
d = t - g * a
c = t - x * b
p = abs(int(d))
z = abs(int(c))
print(min(p, z))
