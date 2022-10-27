a = int(input())
b = int(input())
znak = str(input())
if b==0 and znak=='/':
    print('на ноль делить нельзя!')
elif znak=='+':
    print(a+b)
elif znak=='-':
    print(a-b)
elif znak=='*':
    print(a*b)
elif znak=='/':
    print(a/b)
else:
    print('Неверная операция')