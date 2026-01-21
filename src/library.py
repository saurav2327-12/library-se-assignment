class Library:
    def __init__(self):
        # book_id -> {title, author, status}
        self.books = {}

    # ---------- Sprint 1 ----------
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "available"
        }

    # ---------- Sprint 2 ----------
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book does not exist")

        if self.books[book_id]["status"] == "borrowed":
            raise ValueError("Book already borrowed")

        self.books[book_id]["status"] = "borrowed"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book does not exist")

        self.books[book_id]["status"] = "available"
