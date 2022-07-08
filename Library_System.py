class Library :

    def __init__(self, books):
        self.books = books

    def display(self) :
        print("List of Books present in the Library are :")
        for item in self.books :
            print(" * " + item)
        print("\n")
    
    def borrow(self, b):
        if b in self.books :
            print(f"You have been issued the book : {b}.\nKindly keep it safe and return it after 30 days.\n")
            self.books.remove(b)
        else : print("This book is not currently present in the Library. Please wait until its available!!\n")
    
    def return_book(self, b):
        print("Thanks for adding/returning this book. Have a great day ahead :)\n")
        self.books.append(b)
    
    def fine(self, days) :
        if(days > 30) :
            print(f"Your fine for late submission of book is : Rs.{(days-30)*2}")
        else :
            print("You have not beeen imposed any fine till now !!\n")
    
class student :

    @staticmethod
    def take_book() :
        a = input("Enter the name of the book you want to borrow : ")
        return(a)

    @staticmethod
    def give_book() :
        a = input("Enter the name of the book you want to return/add : ")
        return(a)
    
list_of_books = ['Harry Potter', 'Basic Engineering Mechanics','Basic Python Programming', 'Cindrella', 'Bymokhesh']
central = Library(list_of_books)
s = student()

while(True) :
    msg = '''\n***** Welcome to entral Library *****
    1. Display available books.
    2. Borrow a book
    3. Return/add a book
    4. Display fine
    5. Exit the Library\n'''
    print(msg)
    ch = int(input(" Enter Your Choice : "))
    if(ch == 1) :
        central.display()
    elif (ch == 2):
        central.borrow(student.take_book())
    elif (ch == 3):
        central.return_book(student.give_book())
    elif (ch == 4):
        central.fine(44)
    elif (ch == 5):
        print("Thanks for visiting Central Library !! Please visit again later :) ")
        exit()
    else : print("Invalid Choice :(")


