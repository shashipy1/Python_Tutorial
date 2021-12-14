# class A:
#     classvar1 = "I am a class variable of class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         # self.classvar1 = "Instance variable of class A"
#
# class B(A):
#     pass
#     classvar2 = "I am inside class B"
#     # classvar1 = "I am inside class B of first var"  # b/c first of all see the class var of A than B
#
# a = A()
# b = B()
# print(b.classvar1)



#
# class A:
#     classvar1 = "I am a class variable of class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance variable of class A"
#         self.special = "special"
#
# class B(A):
#     classvar1 = "I AM IN CLASS B"
#
#     def __init__(self):
#         super().__init__()
#         self.var1 = "I am inside class B's constructor"   # CLASS A KA ISLIYE PRINT NI KR RHA KYUKI OVER WRITE H
#         self.classvar1 = "Instance variable of class B"
#
# a = A()
# b = B()
# print(b.classvar1)
# print(b.special, b.classvar1, b.var1)


# class A:
#     classvar1 = "I am a class variable of class A"
#     def __init__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance variable of class A"
#         self.special = "special"
#
# class B(A):
#     classvar1 = "I AM IN CLASS B"
#
#     def __init__(self):
#         self.var1 = "I am inside class B's constructor"   # CLASS A KA ISLIYE PRINT NI KR RHA KYUKI OVER WRITE H
#         self.classvar1 = "Instance variable of class B"
#         super().__init__()
# a = A()
# b = B()
# print(b.classvar1)
# print(b.special, b.classvar1, b.var1)





class A:
    classvar1 = "I am a class variable of class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance variable of class A"
        self.special = "special"

class B(A):
    classvar1 = "I AM IN CLASS B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"   # CLASS A KA ISLIYE PRINT NI KR RHA KYUKI OVER WRITE H
        self.classvar1 = "Instance variable of class B"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
print(b.classvar1)
print(b.special, b.classvar1, b.var1)

