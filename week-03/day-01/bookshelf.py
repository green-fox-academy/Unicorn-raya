# Bookshelf
# Write a program which can store books in a bookshelf.

# There are two types of books.

# Hardcover book
# It should have the following fields: title, author, release year, page number and weight.
# The weight must be calculated from the number of pages (every page weighs 10 grams) plus the weight of the cover which is 100 grams.
# It must have a method that returns a string which contains the following information about the book: author, title and year.

# Paperback book
# It should have the following fields: title, author, release year, page number and weight.
# The weight must be calculated from the number of pages (every page weighs 10 grams) plus the weight of the cover which is 20 grams.
# It must have a method that returns a string which contains the following information about the book: author, title and year.
# You must be able to add books to the bookshelf and must have methods to answer the following problems:

# Who is the author of the lightest book?
# Which author wrote the most pages?

from library import Book
from library import Bookshelf
class Handcover(Book):
    def __init__(self,title,author,release_year,page_number):
        super().__init__(title,author,release_year)
        self.page_number = page_number
        self.weight = 10 * self.page_number + 100

    def getWeight(self):
        return self.weight

    def getPages(self):
        return self.page_number


class Paperback(Book):
    def __init__(self,title,author,release_year,page_number):
        super().__init__(title,author,release_year)
        self.page_number = page_number
        self.weight = 10 * self.page_number + 20
        self.paper_most_author = ""
        self.lightest_book_author = ""

    def getWeight(self):
        return self.weight

    def getPages(self):
        return self.page_number

class NewBookShelf(Bookshelf):
    def __init__(self,booklist = []):
        super().__init__(booklist)
        self.lightest_book_author = ""
        self.most_pages_author = ""

    def find_lightest_book_author(self):
        weight = 9999999
        for book in self.booklist:
            if book.getWeight() < weight:
                weight = book.getWeight()
                self.lightest_book_author = book.getAuthor()
   
    def find_paperMost_author(self):
        paperMost = -1
        self.most_pages_author = ""
        for book in self.booklist:
            if book.getPages() > paperMost:
                paperMost = book.getPages()
                self.most_pages_author = book.getAuthor()

    def refresh_info(self):
        self.find_lightest_book_author()
        self.find_paperMost_author()

    def __str__(self):
        return f"lightest book author is: {self.lightest_book_author} \n \
                thickest book is {self.most_pages_author}"
     
B1 = Paperback("Douglas Adams","The Hitchhiker's Guide to the Galaxy",1979,100)
B2= Handcover("bbbbbb","real_book",1900,3000)
booklist = NewBookShelf([B1,B2])
booklist.refresh_info()

print(str(booklist))
