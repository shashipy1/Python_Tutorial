class rgpv_students:
    no_of_students = 5000

    def __init__(self, name, college, branch, ro_no):
        self.name = name
        self.college = college
        self.branch = n=branch
        self.ro_no = ro_no


    def printdetails(self):
        return f"name of student {self.name}, name of college {self.college}, name of branch {self.branch}, roll no {self.ro_no} "

    @classmethod
    def change_students(cls, newstudent):
        cls.no_of_students = newstudent

    @classmethod
    def from_res(cls, string):
        return cls(*string.split("-"))


shashi = rgpv_students("SHASHI", "RADHARAMAN","CSE", 124 )
rahul = rgpv_students("RAHUL","RADHARAMAN","CSE", 124  )
varinder = rgpv_students("VARINDRA","RADHARAMAN", "CSE", 141 )

vinay = rgpv_students.from_res("VINAY-RITS-CSE-142")

# shashi.name = "SHASHI"
# shashi.college = "RADHARAMAN"
# shashi.branch = "CSE"
# shashi.ro_no = 124
#
# rahul.name = "RAHUL"
# rahul.college = "RADHARAMAN"
# rahul.branch = "EX"
# rahul.ro_no = 132

# varinder.name = "VARINDDRA"
# varinder.college = "RADHARAMAN"
# varinder.branch = "CSE"
# varinder.ro_no = 141

print(shashi.printdetails())
print(varinder.printdetails())
print(rahul.printdetails())

print(shashi.ro_no, varinder.name, rahul.college)

rgpv_students.change_students(365)
print(shashi.no_of_students)

print(vinay.name, vinay.college, vinay.branch, vinay.ro_no)





