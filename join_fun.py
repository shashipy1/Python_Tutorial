# lis = ["john", "vijay", "kahli", "jindar mahal", "Randy"]
# for item in lis:
#     print(item,"and", end="")
# print("all are the palyers of wwe ")

# same thing are print through the joinfunction

lis = ["john", "cena", "kahli", "jindar mahal", "Randy"]

a = " and ".join(lis) #join with and

a1 = " , ".join(lis) # join with comma

a3 = "  ".join(lis) # join with space

print(a, "all are the palyers of wwe ")
print(a1, "all are the palyers of wwe ")
print(a3, "all are the palyers of wwe ")
