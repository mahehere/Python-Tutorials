import time
class Library:
    def __init__(self,books,name):
        self.Books=books
        self.Name=name
        self.Lend={}

    def display_books(self):
        for i in self.Books:
            print(i)
        time.sleep(2)

    def lend_books(self):
        cust_name=input("Please Enter your Userid\n")
        print("Select Book You wish to lend")

        for index,data in enumerate(self.Books,1):
            print(f"{index}: {data}")

        no=int(input("Enter Book Number\n"))
        b=self.Books[no-1]
        if b in self.Lend:
            print(f"Book Already Lend By {self.Lend[b]}")
        else:
            self.Lend[b]=cust_name

    def add_book(self):
        new_book=input("Please Enter the Name of the book\n")
        self.Books.append(new_book)

    def return_book(self):
        if not bool(self.Lend):
            print("No books for return\n")
        else:
            bn=input("Name of the Book\n")
            if bn in self.Lend.keys():
                self.Lend.pop(bn)
                print("Your Book is Successfully returned")

            else:
                print("No. Book is lent of Entered Name")

if __name__ == "__main__":
    AvnishLibrary=Library(["C++","Python","Java","English Grammer","Maths"],"Avnish")
    print("WELCOME TO CENTRAL LIBRARY JALANDHAR!!")
    while True:
        a="""Please Choose Options From Below:
 1. Display Books  2. Lend Book   3. Add Book   4. Return Book   5.Exit
 """
        i=int(input(a))
        if i==1:
            AvnishLibrary.display_books()
        elif i==2:
            AvnishLibrary.lend_books()
        elif i==3:
            AvnishLibrary.add_book()
        elif i==4:
            AvnishLibrary.return_book()
        elif i==5:
            print("Hope 2 see u soon")
            break
        else:
            print("Inavlid Input!! Please Enter Again")