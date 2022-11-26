x = int(input())
chet = 0
nechet = 0
while x > 0:
    ld = x % 10
    if ld % 2 == 0:
        chet += 1
    if ld % 2 == 1:
        nechet += 1
    x = x // 10
if chet > nechet:
    print('больше четный', chet)
else:
    print('больше нечетных', nechet)
