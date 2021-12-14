# l1 = ["Aloo", "Orange", "Banana","Grapes","Chocklate"]
# i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(item)
#     i += 1

# Using enumerate - gives both items and indexes

l1 = ["Aloo", "Orange", "Banana","Grapes","Chocklate"]
for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Only buy item as mom say {item}")
