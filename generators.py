# def gen(n):
#     for i in range(n):
#         yield i
# g = gen(5)
# # print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__()) - StopIteration


# def gen(n):
#     for i in range(n):
#         yield i
# g = gen(5)
# for i in g:
#     print(i)



S = "Shashi"

har = iter(S)
# print(har.__next__())
# print(har.__next__())
# print(har.__next__())
for h in S:
    print(h)