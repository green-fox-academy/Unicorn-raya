# Library
# You are going to create a simple library where you can store books in a bookshelf.

# Book
# Book has an author, a title and a release year
# Book should have an toString method that returns a string in this format:
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
# Bookshelf
# Bookshelf has a list of books in it
# It must be able to add books to the bookshelf
# It must be able to remove books from the bookshelf
# It must have a favouriteAuthor method which must be able to return who has written the most books 
# in the shelf

# It must have a earliestPublished method which must be able to return the earliest published book.
# It must have a latestPublished method which must be able to return the latest published book.

# It must have a toString method which give us information about the number of books, 
# the earliest and the latest released books, and the favourite author.

class Book:
    def __init__(self,author = "",title= "",release_year= -1):
        self.author = author
        self.title = title
        self.release_year = release_year

    def __str__(self):
        return (f"{self.author} : {self.title} ({self.release_year})")

    def getAuthor(self):
        return self.author
    def getTitle(self):
        return self.title
    def getRelYear(self):
        return self.release_year


# B = Book("Douglas Adams","The Hitchhiker's Guide to the Galaxy","1979")
# print(str(B))

class Bookshelf:
    def __init__(self,booklist = []):
        self.booklist = booklist
        self.count_author = {}
        self.fav_author = ""
        self.book_num = len(self.booklist)
        self.earliestBook = ""
        self.latestBook = ""


    def add_book(self,book):
        self.booklist.append(book)

    def remove_book(self,book_name):
        self.booklist = [x for x in self.booklist if x.getTitle() != book_name]
    
    def favouriteAuthor(self):
        for book in self.booklist:
            if book.getAuthor() in self.count_author.keys():
                self.count_author[book.getAuthor()] += 1
            else:
                self.count_author[book.getAuthor()] = 1
        max_number = -1
        self.fav_author = ""
        for key in self.count_author.keys():
            if self.count_author[key] > max_number:
                max_number = self.count_author[key]
                self.fav_author = key
            
    
    def earliestPublished(self):
        self.booklist = sorted(self.booklist,key = lambda x: x.getRelYear())
        self.earliestBook = self.booklist[0]

    def latestPublished(self):
        self.latestBook = self.booklist[len(self.booklist) - 1]
    
    def book_count(self):
        self.book_num = len(self.booklist)
    
    def refresh_info(self):
        self.favouriteAuthor()
        self.earliestPublished()
        self.latestPublished()
        self.book_count()

    def __str__(self):
        return f"In bookshelf we have: {self.book_num},\n \
                 the earliest book is: {self.earliestBook},\n \
                 the latest book is: {self.latestBook},\n \
                 favorite author is: {self.fav_author}"


# B1 = Book("Douglas Adams","The Hitchhiker's Guide to the Galaxy",1979)
# B2 = Book("Douglas Adams","The Hitchhiker's Guide to the Galaxy",1979)
# B3 = Book("ummmm","this is a book",6699)

# BLIST = [B1,B2]

# BS = Bookshelf(BLIST)
# BS.refresh_info()
# print(str(BS))
# BS.add_book(B3)     
# BS.refresh_info()
# print(str(BS))
# BS.remove_book("The Hitchhiker's Guide to the Galaxy")
# BS.refresh_info()
# print(str(BS))