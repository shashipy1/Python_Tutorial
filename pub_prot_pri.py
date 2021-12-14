class student():
    no_of_students = 140
    var = 18 # pubic variable
    _protec = 12
    __private = 14
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

        return cls(*string.split("-"))
std = student("name", 123, "RITS", "CSE")
print(std._protec)
print(std._student__private)