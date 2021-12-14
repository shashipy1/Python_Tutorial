# fibonacci number=0,1,1,2,3,5,8,13...................

def fabonicci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonicci(n-1)+fabonicci(n-2)
num = int(input("enter the number"))
print(fabonicci(num))
