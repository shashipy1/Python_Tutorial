# Setters & Property Decorators

# class Empolyee:
#
#     def __init__(self, fname, lname): # f = first name and l = last name
#         self.fname = fname
#         self.lname = lname
#         # self.printemail = f"{fname}.{lname}@gmail.com"
#
#     def explain(self):
#         return f"This is employee is {self.fname} {self.lname}"
#     @property
#     def email(self):
#        return f"{self.fname}.{self.lname}@gmail.com"
#
#
# s_k_ranjha = Empolyee("shashi", "RANJHA")
# indian_jharokha = Empolyee("RAHUL", "SKK")
#
# print(s_k_ranjha.explain())
# # print(indian_jharokha.printemail)
#
# indian_jharokha.fname = "USA"
# print(indian_jharokha.email())


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

s_k_ranjha = Empolyee("shashi", "RANJHA")
indian_jharokha = Empolyee("RAHUL", "SKK")

print(indian_jharokha.email)

indian_jharokha.fname = "USA"
print(indian_jharokha.email)
indian_jharokha.email = "this.that@gmail.com"
print(s_k_ranjha.fname)
print(indian_jharokha.lname)
print(indian_jharokha.email)

del indian_jharokha.email
print(s_k_ranjha.email)

indian_jharokha.email = "shashi.ranjha@gmail.com"
print(s_k_ranjha.email)