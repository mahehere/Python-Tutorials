# Proj 1. Library Management System
# Create a Library class
# Should have 4 functions
# 1. Display books
# 2. Lend book
# 3. Add book
# 4. Return Book

class Library:
    book_list = ["Java", "Python", "DB", "Control-M"]

    def __init__(self, listofbooks, libname,username):
        self.books = listofbooks
        self.libname = libname
        self.user = username

    @staticmethod
    def display():
        #book_list = ["Java", "Python", "DB", "Control-M"]
        print("The below are the books currently available in our library\n", Library.book_list)

    def lend(self):
        b = str(input("Which book do you want from the list :"))
        if b not in Library.book_list:
            print("This book is not already lent to :", self.user)
        else:
            print("This book is lent to  lend function")

    def add_book(self):
        new_book = str(input("Type the name of the book to add in library"))
        Library.book_list.append(str(new_book))
        print("The below are the books currently available in our library\n", Library.book_list)
        print("This is display function")

    def return_book(self):

        print("This is return function")



lib = Library("Maths", "Noombal Library","Mahesh")
#ab = Library.add_book()
# lib.printdtls()
#lib.display()
# lib.Print_dtls()
# print(Library.__dict__)
# print(lib.__dict__)
# lib.display1(listofbooks, libname)


def display():
    pass


def lend():
    pass


def add_book():
    pass


def return_book():
    pass


if __name__ == '__main__':
    print("Welcome to Noombal Library")

    while True:
        print("Which option do you want\n 1.Display Books\n 2.Lend Book\n 3.Add Books\n 4.Return Book\n 5.Exit")
        a = int(input("Enter your number from the above:"))
        if a == 1:
            lib.display()
        elif a == 2:
            lib.lend()
        elif a == 3:
            lib.add_book()
        elif a == 4:
            return_book()
        elif a == 5:
            print("Thanks for coming to", lib.libname)
            break

        else:
            print("Please enter a valid input")
