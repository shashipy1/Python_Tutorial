
# def a_first(a):
#     return a[1]
#
# a = [[3,5], [6,1], [2,6],[6,2]]
# a.sort(key=a_first)
# print(a)
#
# def sot(a):
#     return(sort)


a = [[3,5], [0,1], [1,6],[3,2]]
a.sort(key=lambda x:x[1])
print(a)