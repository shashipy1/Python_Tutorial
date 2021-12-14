# n! = n*(n-1)!

def factorial_itrative(n):
    '''
    n parameter:integer
    :return n*(n-1)*(n-2)...................1
    '''
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac
num = int(input("enter the number\n"))
print("factorial using itrative method",factorial_itrative(num))

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
#       n=5: 5*factorial_recursive(4)
num = int(input("enter the number\n"))
print("factorial using recursive method",factorial_itrative(num))
