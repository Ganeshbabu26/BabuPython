class Library:
    def __init__(self,books):
        self.books = books
    
    def list_books(self):
        print("Available Books")
        for book in self.books:
            print(book)
    
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get your book now")
            self.books.remove(borrow_book)
        else:
            print("Book not available")
    
    def recieve_book(self,recieve_book):
        print("You have returned the book")
        self.books.append(recieve_book)

books = ['C','C++','JAVA','HTML','CSS','JAVASCRIPT','REACT','PYTHON','PHP','PERL']
o = Library(books)
msg = """
        1. Display book
        2. Borrow book
        3. Return book
    """
while True:
    print(msg)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter book name to borrow: ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter book name to return: ")
        o.recieve_book(book)
    else:
        print("Thank you come again")
        quit()