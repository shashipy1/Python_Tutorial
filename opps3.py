class Employee:
    no_of_leaves = 10
#constructor
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetail(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"
shashi = Employee("Shashi", 435, "coder")

rahul =  Employee("varidra",100000,"seo")
# shashi.name = "SHASHI"
# shashi.salary = 20000
# shashi.role = "Software Eng"

# rahul.name = "RAHUL"
# rahul.salary = 50000
# rahul.role = "coder"
print(shashi.role)

print(shashi.name,shashi.salary,shashi.role)

print(rahul.name,rahul.salary,rahul.role)