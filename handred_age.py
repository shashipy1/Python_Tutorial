yearAge = int(input("what is your age/year of birth:\n"))
isAge = False
isYear = False
if len(str(yearAge)) == 4:
    isAge = True
else:
    isAge = True
if (yearAge < 1900 and isYear):
    print("You seem to be the oldest person alive ")
    exit()
if yearAge > 2021  :
    print("you are not yet born ")
    exit()

if isAge:
    yearAge = 2021 - yearAge
print(f"you will be 100 year old in {100 + yearAge}")

# interestedYear = int(input("Enter the year you want to know your age in\n"))
#
# print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")