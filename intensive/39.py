с = 0
for i in range(25, 36):
    c=i
    while c!=1:
        if c%2==1:
            c=c*3+1
        else:
            c=c/2
        print(c)