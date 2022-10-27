a, b, c = float(input()), float(input()), float(input())
if a == b == c:
    print('Равносторонний')
elif b == c or a == c or a == b:
    print('Равнобедренный')
else:
    print('Разносторонний')
