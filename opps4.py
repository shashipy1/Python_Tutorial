# # CLASS METHOD
#
# class student():
#     no_of_students = 140
#     def __init__(self,aname,aroleno,acollege,abranch):
#         self.name = aname
#         self.roleno = aroleno
#         self.college = acollege
#         self.branch = abranch
#
#     def printdetail(self):
#         return f"name is {self.name}, roleno is {self.roleno},name of {self.college}, name of{self.branch}"
#
# shashi = student("rahul", 124,"RITS","cse")
# rahul = student("SHASHI", 152,"REC","EX")
# print(shashi.name,shashi.college,shashi.roleno,shashi.branch)
#
# student.no_of_students = 450 directly set the value
# print(shashi.no_of_students)



# CLASS METHOD

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


shashi = student("rahul", 124,"RITS","cse")
rahul = student("SHASHI", 152,"REC","EX")

print(shashi.name,shashi.college,shashi.roleno,shashi.branch)

# rahul.change_students(480)threes gives same valuse
# shashi.change_students(480)
student.change_students(480)

print(shashi.no_of_students)
