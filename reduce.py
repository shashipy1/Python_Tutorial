from functools import reduce

list1 = [2,3,1,4,7,8,]
# num = 0
# for i in list1:
#     num = num + i
# print(num)

# same o/p a/c to reduce fn

num = reduce(lambda x,y:x+y,list1)
print(num)

num = reduce(lambda x,y:x*y,list1)
print(num)

num = reduce(lambda x,y:x/y,list1)
print(num)

num = reduce(lambda x,y:x-y,list1)
print(num)

