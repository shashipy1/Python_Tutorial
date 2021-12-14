list_1 = [2,5,4,7,5,8,9,1,23,12]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5,list_1))
print(gr_than_5)