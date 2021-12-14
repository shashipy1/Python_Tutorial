print("printing star")
num = int(input("enter the row: "))
bool_val = input("1 for true and 0 for false: ")
if bool_val == "1":
    for i in range(0, num+1):
        print("* " *i)

if bool_val == "0":
    for i in range(num,0,-1):
        print("* " * i) 