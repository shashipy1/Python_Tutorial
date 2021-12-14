class student():
    no_of_students = 140
    def __init__(self,aname,aroleno,acollege,abranch):
        self.name = aname
        self.roleno = aroleno
        self.college = acollege
        self.branch = abranch

    def printdetail(self):
        return f"name is {self.name}, roleno is {self.roleno},name of {self.college}, name of {self.branch}"

    @classmethod
    def change_students(cls, newstudents):
        cls.no_of_students = newstudents

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))  # in one line

    @staticmethod
    def printshashi(string):
        print("BHAI SAHEB APNE TO KAMAL KR DIYA " + string)

# inheritance
class programmer(student):
    def __init__(self,  aname, aroleno, acollege, abranch, languages):
        self.name = aname
        self.roleno = aroleno
        self.college = acollege
        self.branch = abranch
        self.languages = languages

    def printprog(self):
        return f"The programmer's name is {self.name}, roleno is {self.roleno},name of college {self.college}," \
               f" name of branch {self.branch}, The languages are {self.languages}"

shashi = student("rahul", 124, "RITS", "cse")
rahul = student("SHASHI", 152, "REC", "EX")

#  single inheritance

varinder = programmer("VARINDER", 141, "RITS", "CSE", ["python"])
shashi1 = programmer("SHASHI", 124, "RITS", "CSE",  ["c", "cpp"])
print(shashi1.printprog())

print(varinder.printprog())