# Operator Overloading & Dunder Methods

class student():
    no_of_students = 140
    def __init__(self,aname,aroleno,acollege,abranch):
        self.name = aname
        self.roleno = aroleno
        self.college = acollege
        self.branch = abranch

    def printdetail(self):
        return f"name is {self.name}, roleno is {self.roleno},name of {self.college}, name of branch {self.branch}"

    @classmethod
    def change_students(cls, newstudents):
        cls.no_of_students = newstudents

    def __add__(self, other):
        return  self.roleno + other.roleno

    def __truediv__(self, other):
        return  self.roleno / other.roleno

    def __repr__(self):
        # return f"name is {self.name}, roleno is {self.roleno},name of {self.college}, name of branch {self.branch}"
        # return self.printdetail()
        return f"student('{self.name}', {self.roleno}, '{self.college}', '{self.branch}')"

    def __str__(self):
        return f"The name is {self.name} roleno is {self.roleno},name of {self.college}, name of branch {self.branch} "

stud1 = student("shashi", 124, "rits", "cse")
stud2 = student("vinay", 141, "rits", "cse")

print(stud1+stud2)

print(stud1 / stud2)

print(stud1)
print(str(stud1)) # str khe kr cll kru to v print krega jo stud1 ko krega it meams both are same (stud1) and str(stud1)
print(repr(stud1))
