class Software_devloper:
    no_of_workers = 200

    def __init__(self, name, salery, position):
        self.name = name
        self.salery = salery
        self.pos = position

    def printdetails(self):
        return f"name of Software dep {self.name}, salery of S/D {self.salery}, position {self.pos}"

    @classmethod
    def change_Software_devloper(cls, new):
        cls.no_of_workers = new

    def from_dash(cls, string):
        return cls(*string.split("-"))  # in one line

    @staticmethod
    def printshashi(string):
        print("srf4n sfdngik rjfnfikmfiwe ijmeifmkm nfksansk" + string)

    # def __add__(self, other):
    #     return self.salery + other.salery
    #
    # def __truediv__(self, other):
    #     return self.salery / other.salery

#     def __repr__(self):
#         return f"Software devloper {self.name}, {self.salery}, {self.pos}"
#
#     def __str__(self):
#         return f"THE s/d name is {self.name} ,selaey is {self.salery}, position is {self.pos}"


class worker(Software_devloper):
    def __init__(self, name, salery, position):
        self.name = name
        self.salery = salery
        self.pos = position
    def printdev(self):
        return f"name of woker {self.name}, salery {self.salery}, position is {self.pos}"



shashi = worker("SHASHI", 23483, "S/D")
varindar = worker("VARINDRA", 23423, "B/D")

print(shashi.printdev())
# vinay = Software_devloper.from_dash("VINAY-7435789-s/d")
# print(shashi+vinay)
# print(shashi / varindar)
# print(repr(shashi))
#
# print(shashi)
# print(str(shashi))



# class A:
#     classvar1 = "this is variable of class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance variable of class A"
#         self.specail = "special"

# class B(A):
#     classvar1 = "I AM CLAAS B"
#     def __init__(self):
#         # super().__init__()
#         self.var1 = "I am inside class B"
#         self.classvar1 = "I am inside class B of first var"
#         super().__init__()
#         print(super().classvar1)

# a = A()
# b = B()
# print(b.classvar1)
# print(b.specail, a.specail, b.classvar1, b.var1)
# print(b.classvar1)


# lambda
#
# print("sum of two nos")
# a = int(input())
# b = int(input())
#
# sum = lambda x, y : x+y
# print(sum(a,b))