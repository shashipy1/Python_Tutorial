# class Empolyee:
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def explain(self):
#         return f"This is employee is {self.fname} {self.lname}"
#     @property
#     def email(self):
#         if self.fname == None or self.lname == None:
#              return "Email is not set. Plz set using setter "
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self, string):
#         print("setting now.........")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
# skillf = Empolyee("skill" ,"F")
# print(skillf.email)
#
# o = "shashi will best coder in python"
# print(dir(skillf))
# # print(type(skillf))  - error
#
# print(type("this is string")) # told that types about of the object
# print(id("this is string"))   # it refers to the  stored id - 2056607113840
#
# print(id("shashin is coder"))   # id - 2056607092784



class Empolyee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This is employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
             return "Email is not set. Plz set using setter "
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting now.........")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Empolyee("skill" ,"F")
o = "shashi will best coder in python"

import inspect
print(inspect.getmembers(skillf))     # PRINT ALL ATTRIBUTES