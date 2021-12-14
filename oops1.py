class student:
    no_of_leaves = 10 #class ki property se object means shashi ke name exces kr diya, it,s same to all
    pass
shashi = student()
rahul = student()

shashi.name = "shashi"
shashi.std = "B.tech"
shashi.sec = "A"
shashi.college = "RITS"
shashi.roll_no = 124
rahul.name = "shashi"
rahul.coll = 12
rahul.sub = ["math","hindi"]
print(shashi.roll_no, rahul.sub)
print(shashi.no_of_leaves)
print(rahul.no_of_leaves)
print(student.no_of_leaves)

print(rahul.__dict__)
print(shashi.__dict__)
shashi.no_of_leaves = 12 # ye apni property hai, new Instance of var
student.no_of_leaves = 12
print(shashi.__dict__) #isme no_of _leaves ko print krega kyuki apni property ho gya
print(student.no_of_leaves)
