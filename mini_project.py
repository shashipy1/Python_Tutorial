class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our library : {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lander-Book database has been update: you can take book now")
        else:
            print(f"Book is already used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been updated in book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    shashi = Library(['Basic  c & Cpp', 'Computer Fundamental','PYTHON', 'JAVA', 'Chemistry', 'Physics','MATHEMATICS'],
                     "RADHARAMAN INSTITUTE OF TECHNOLOGY SCIENCE(RITS)")
    while(True):
        print(f"Welcome to the {shashi.name} library. Enter the your choice to continue")
        print("1. Display the Books")
        print("2. Land the Book")
        print("3. Add the Book")
        print("4. Return Book")

        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            shashi.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            shashi.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            shashi.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            shashi.returnBook(book)

        else:
            print("Not a valid option")
        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue




