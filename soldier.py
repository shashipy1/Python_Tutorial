# question 
# 1st letter is captale, and jo file captalize na ho other file and jpg ko list me


import os
def solider(path, file, formate):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == formate:
            os.rename(file, f"{i} {formate}")
            i += 1

solider(r"C:\Users\shashikant\Desktop\project",
        r" E:\All Programming\project",".png")

