# lis = []
# for i in range(100):
#     if i%3 == 0:
#         lis.append(i)
# print(lis)


# ls = [i  for i in range(200) if i%5==0]
# print(ls)


# dict1 = {0: "item0", 1: "item1".......................................100} -1st method

# dict2 = {i:f"item{i}" for i in range(1,1000)}
# print(dict2)


# dict2 = {i:f"item{i}" for i in range(1,1000) if i%100==0}
# print(dict2)



# dict3 = {i:f"item{i}" for i in range(10)}
# dict4 = {value:key for key, value in dict3.items()}
# print(dict3, "\n",dict4)
#
#
# # How to make set comprehesion
#
# dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
# print(dresses)
# print(type(dresses))


evens = (i for i in range(200) if i%2==0)
# print(evens)  --><generator object <genexpr> at 0x00000261D02BEC10>
for item in evens:
    print(item)

