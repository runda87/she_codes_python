class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1 
        self.last_page = +1


    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}, Current page: {self.current_page}"

    def bookmark_page(self): 
        self.bookmark_page = self.current_page


    def turn_page(self, forward):
        if forward:
            self.current_page = self.current_page + 1
        else:
            self.current_page = self.current_page - 1     

    def got_to(self, pagenum):
        self.current_page = pagenum
    
    def specific_pn(self, spn):
        self.bookmark_page = spn

    def lp(self, lp):
        self.
   

        
book1 = Book("Great Expectation", "Charles Dickens", 340, 20)
# print(book1.title)
# print(book1.author)

book2 = Book("To Kill a Mockingbird", "Harper Lee", 298, 34 )
# print(book2.title)

print()
print(book1)
print(book2)

print(book2.current_page)
print(book2.bookmarked_page)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
book2.turn_page(True)
print(book2.current_page)
book2.bookmark_page()
print(book2.current_page)
book2.got_to(45)
print(book2.current_page)
book2.specific_pn(33)
print(book2.bookmark_page)
