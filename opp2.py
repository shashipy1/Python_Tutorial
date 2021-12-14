class Employee:
    no_of_leaves = 10

    def printdetail(self):
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"
shashi = Employee()
rahul =  Employee()

shashi.name = "SHASHI"
shashi.salary = 20000
shashi.role = "Software Eng"

rahul.name = "RAHUL"
rahul.salary = 50000
rahul.role = "coder"

print(shashi.printdetail())

print(rahul.printdetail())

shashi.no_of_leaves = 132

print(shashi.no_of_leaves)
