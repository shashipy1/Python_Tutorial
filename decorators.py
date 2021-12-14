# def function1():
#     print("shashi aaj tumko 60 ya 70 videos complete krna h-19.09.2021")
# func2 = function1
# # del means delete the function than it aslo print b/c other copy is ready
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funcret(1)
# print(a)

# def executor(func):
#     func("abhi me 6:00 jga to baitha hu coding krne")
# executor(print)


def dec1(func1):
    def nowexec():
        print("or kpda laye")
        func1()
        print("phir padhne baith gye")
        return nowexec
@dec1
def shashi():
    print("shashi bhai acha se python kro")
# shashi = dec1(shashi) ye or function name (@dec1)same h
shashi()










