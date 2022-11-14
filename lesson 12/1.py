n = int(input())
chislo1 = 0
chislo2 = 1
for i in range(n+1):
    chislo2 = chislo2 + chislo1
    chislo1 = chislo2 - chislo1
    print(chislo1, end=' ')
