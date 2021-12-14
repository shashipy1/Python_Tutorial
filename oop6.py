class student():
    no_of_students = 140
    var = 5
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
class player:
    no_of_games = 4
    var = 6
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return  f"name is {self.name}, name of game {self.game}"

# class coder(student, player):
    # var = 10
class coder(player, student):
    language= "C++"
    def printlanguage(self):
        print(self.language)


shashi = student("rahul", 124, "RITS", "cse")
rahul = student("SHASHI", 152, "REC", "EX")

vinay = player("SHASHI KANT KUMAR", ["chess"])

# varinder = coder("RAVI", 120, "JLN", "MCA")
varinder = coder("RAVI", ["CRICKET"])
# det = varider.printdetail()
# varider.printlanguage()
# print(det)

print(varinder.var)
