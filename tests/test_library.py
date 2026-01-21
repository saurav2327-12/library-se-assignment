import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B001", "Python Basics", "Guido")

    def test_add_book_success(self):
        self.lib.add_book("B002", "DSA", "CLRS")
        self.assertIn("B002", self.lib.books)

    def test_duplicate_book_error(self):
        with self.assertRaises(ValueError):
            self.lib.add_book("B001", "Duplicate", "Author")


class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.lib.add_book("B001", "Python Basics", "Guido")

    def test_borrow_available_book(self):
        self.lib.borrow_book("B001")
        self.assertEqual(self.lib.books["B001"]["status"], "borrowed")

    def test_borrow_unavailable_book_raises_error(self):
        self.lib.borrow_book("B001")
        with self.assertRaises(ValueError):
            self.lib.borrow_book("B001")

    def test_return_book_updates_status(self):
        self.lib.borrow_book("B001")
        self.lib.return_book("B001")
        self.assertEqual(self.lib.books["B001"]["status"], "available")


if __name__ == "__main__":
    unittest.main()
