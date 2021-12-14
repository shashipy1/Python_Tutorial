list = [23, 34, 24, 4]
print(4 in list)
print(45 not in list)
if 45 not in list:
    print("no")



# list to dict
l = [["harry",1], ["shashi",2], ["fruits",3], ["other name",4]]
# print(l[0],l[3])
dict1 = dict(l)
# print(dict1)
# for item, lollypop in l:
for item, lollypop in dict1.items():




    print(item,"and loll is",lollypop)
# loop ir=tems
list=[24, "jfhs", "jnfd",4 ,3,5,45,235,7,6,37,49,46,59]
for item in list:
    if str(item).isnumeric() and item >=6:
        print(item)
 



#  dict

dict = {"shashi" : "b.tech",
        "rahul"  : {"A":"coder","B":"dj","C":"dhuwen"}}
dict["varindra"]="ujrfdg9v"
dict[384]="ierr93jf9"
print(dict.get("shashi"))