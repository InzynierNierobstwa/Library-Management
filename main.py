import time


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Catalog:
    def __init__(self, catalog_name, category='unknown'):
        self.catalog_name = catalog_name
        self.category = category

    all_books = []
    def add_book(self, book):
        self.all_books.append(book)

    def remove_book(self, book):
        self.all_books.remove(book) #how to remove book by its title

    def check_books(self):
        for book in Catalog.all_books:
            print(book.title)

book1 = Book('diuna', 'frank herbert')
book2 = Book('zagadka kuby rozpruwacza', 'andrzej pilipiuk')
book3 = Book('Straz, straz', 'Terry Prachet')

catalog1 = Catalog('glowny')
catalog1.add_book(book1)
catalog1.add_book(book2)
catalog1.add_book(book3)
# catalog1.check_books()

catalog1.remove_book(book1)
catalog1.check_books()

print(book1)





