class A:
    def met(self):
        print("THIS IS METHOD FROM CLASS A")

class B(A):
    def met(self):
        print("THIS IS METHOD FROM CLASS B")

class C(A):
    def met(self):
        print("THIS IS METHOD FROM CLASS C")

class D(C,B): #(B,C) IT PRINT SAME OF B B/C B IS FIRST AND AFTER CHANGING (C,B) PRINT C
    def met(self):
        print("THIS IS METHOD FROM CLASS D")


a = A()
b = B()
c = C()
d = D()

d.met()