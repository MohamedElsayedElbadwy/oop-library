class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book: {self.title} - {self.author}")

    def borrow_book(self):
        print(f"{self.title} has been borrowed.")
    def return_book(self):
        print(f"Book '{self.title}' has beenn returned successfully.")
    def get_details(self):
        return f"{self.title} by {self.author}"

book = Book("Clean Code", "Robert C. Martin")
book.display_info()
