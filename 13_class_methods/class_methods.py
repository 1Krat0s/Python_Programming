# Create a Book Class

class Book:
    total_books = 0
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    @classmethod
    def from_dict(cls, data):
        """Create a Book object from a dictionary"""
        return cls(data["title"], data["author"], data["year"])
    
    @classmethod
    def reset_total_books(cls):
        cls.total_books = 0
    

# Usage
data = {"title": "Learning Python", "author" : "M. Smith", "year" : 2023}
book1 = Book("Python 101", "J. Doe", 2024)
book2 = Book.from_dict(data)

print(book1)
print(book2)