# Lambda or anonymous function

a=int(input("enter a"))
b=int(input("enter b"))

# def add(a,b):
#     return (a+b)

plus = lambda a, b: a+b

print(plus(a,b))

def minus(x,y):
    return x-y
print(minus(9,4))
