# a = input("what is your name")
# b = input("how much do you earn")
# if int(b) == 0:
#     raise ZeroDivisionError("B IS ZERO SO STOPPED THE PROGRAM")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# print(f"hello {a}")

#
# list1 = ["ujhefsduh","jerfiwef","frw"]
# for item in list1:
#     i = 4
#     if i%2==0:
#         i+=1
#     if i>3:
#         raise IndexError("index bda h ")
#
# print(item)



c = input("Enter your name")
try:
    print(a)
except Exception as e:
    if c == "shashi":
        raise ValueError("SHASHI is blocked")
    print("Exception handlled")
