class Author:
    def __init__(self, name, country, birthday, books:list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Book:
    count_books = 0

    def __init__(self, name, year, author:Author):
        self.name = name
        self.year = year
        self.author = author
        Book.count_books += 1


    def get_count_all_books(self):
        return self.count_books

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def new_book(self, name, year, author):
        self.books.append(Book(name, year, author))
        if author not in self.authors:
            self.authors.append(author)

    @staticmethod
    def group_by_author(author):
        return author.books

    def group_by_year(self, year):
        return [book for book in self.books if year == book.year]


library = Library("Korolenko")
kipling = Author("Joseph Rudyard Kipling", "England", "30.12.1865", ["The Jungle Book", "Rikki-Tikki-Tavi"])
fitzgerald = Author("Joseph Francis Fitzgerald", "USA", "10.10.1904", ["The Great Gatsby", "The Last Tycoon"])
stephen_king = Author("Stephen King", 'USA', '21.09.1947',
                      ["The Shining", 'It', 'The Green Mile', 'Dreamcatcher'])
library.new_book("The Jungle Book", 1890, "Joseph Rudyard Kipling")
library.new_book("The Great Gatsby", 1935, "Joseph Francis Fitzgerald")
library.new_book("The Shining", 1935, "Stephen King")
print(library.books)
print(library.group_by_author(stephen_king))
print(library.group_by_year(1935))
print(Book.count_books)


