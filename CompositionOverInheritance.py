class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    def display_info(self):
        return f"{self.name} ({self.nationality})"

class Book:
    def __init__(self, title, author_name, author_nationality, genre):
        self.title = title
        self.genre = genre
        self.author = Author(author_name, author_nationality)
    
    def display_info(self):
        return f"'{self.title}' by {self.author.display_info()} - {self.genre}"

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "American", "Novel")
print(book.display_info())