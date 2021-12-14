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
        return cls(*string.split("-"))  # in one line

    @staticmethod
    def printshashi(string):
        print("BHAI SAHEB APNE TO KAMAL KR DIYA " + string)
        # return "jefusnqn" b/c i want do print return val


shashi = student("rahul", 124, "RITS", "cse")
rahul = student("SHASHI", 152, "REC", "EX")

rohan = student.from_dash("rohan-123-rcp-cse")

# print(rohan.printshashi("WOHHHHHH!")) #print dete h or return ni dete h to value 0(null) degi

rohan.printshashi("WOHHHHHH!")