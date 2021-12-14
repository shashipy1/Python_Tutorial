class student():
    no_of_students = 140
    def __init__(self,aname,aroleno,acollege,abranch):
        self.name = aname
        self.roleno = aroleno
        self.college = acollege
        self.branch = abranch

    def printdetail(self):
        return f"name is {self.name}, roleno is {self.roleno},name of {self.college}, name of{self.branch}"

    @classmethod
    def change_students(cls, newstudents):
        cls.no_of_students = newstudents
    @classmethod
    def from_dash(cls, string):

        # harry = string.split("-")
        # # print(harry) - print list of harry
        # return cls(harry[0], harry[1], harry[2],harry[3])

        return cls(*string.split("-"))  # in one line
shashi = student("rahul", 124, "RITS", "cse")
rahul = student("SHASHI", 152,"REC","EX")

rohan = student.from_dash("rohan-123-rcp-cse")

print(rohan.name)
print(rohan.college)
print(rohan.roleno)
print(rohan.branch)
print(rohan.name, rohan.college, rohan.roleno, rohan.branch)
