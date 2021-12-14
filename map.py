# numbers = ["34","66","23","86","26"]
# numbers = list(map(int,numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i]) it can do one line so itna likhne ki jarurt ni

# numbers[3] = numbers[3] + 5
# print(numbers[3])
# def sq(a):
#     return a*a
# # def cub(b):
# #     return b*b*b
# num = [3,5,7,2,9,11,2]
# squr = list(map(sq,num))
# print(squr)


# use the map fn with lamda

# num = [3,5,7,2,9,11,2]
# squr = list(map(lambda x:x*x,num))
# print(squr)

def square (a):
    return a*a
def cube(a):
    return a*a*a
function = [square,cube]
num = [3,5,7,2,9,11,2]
for i in range (11):
    val = list(map(lambda x:x(i),function))

    print(val)