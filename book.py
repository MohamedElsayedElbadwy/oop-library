class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"{self.title} - {self.author}")


book = Book("Clean Code", "Robert C. Martin")
book.display_info()