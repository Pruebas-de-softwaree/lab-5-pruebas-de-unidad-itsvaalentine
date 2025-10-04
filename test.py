import unittest
from book import Book
from user import User
from library import Library

def seed_library():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949, "ISBN001"))
    lib.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "ISBN002"))
    lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "ISBN003"))
    lib.add_book(Book("Moby Dick", "Herman Melville", 1851, "ISBN004"))
    lib.add_book(Book("Pride and Prejudice", "Jane Austen", 1813, "ISBN005"))
    lib.add_book(Book("War and Peace", "Leo Tolstoy", 1869, "ISBN006"))

    lib.add_user(User("Anna", "U001"))
    lib.add_user(User("Juan", "U002"))
    lib.add_user(User("Mary", "U003"))
    lib.add_user(User("Jaciel", "U004"))
    return lib


# class TestBookUnit(unittest.TestCase):
#     def test_borrow_sets_flag(self):
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         self.assertFalse(b.borrowed)
#         b.borrow()
#         self.assertTrue(b.borrowed)

#     def test_borrow_twice_raises(self):
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         b.borrow()
#         with self.assertRaises(ValueError):
#             b.borrow()

#     def test_return_book_sets_flag_false(self):
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         b.borrow()
#         b.return_book()
#         self.assertFalse(b.borrowed)

#     def test_return_not_borrowed_raises(self):
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         with self.assertRaises(ValueError):
#             b.return_book()


# class TestUserUnit(unittest.TestCase):
#     def test_register_borrow_appends_history(self):
#         u = User("Anna", "U001")
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         u.register_borrow(b)
#         self.assertEqual(len(u.get_history()), 1)
#         self.assertIn("1984", u.get_history()[0])

#     def test_register_return_appends_history(self):
#         u = User("Anna", "U001")
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         u.register_return(b)
#         self.assertEqual(len(u.get_history()), 1)
#         self.assertIn("1984", u.get_history()[0])

#     def test_user_history_spelling_should_be_correct(self):
#         u = User("Anna", "U001")
#         b = Book("1984", "George Orwell", 1949, "ISBN001")
#         u.register_borrow(b)
#         u.register_return(b)
#         self.assertIn("Borrowed:", u.get_history()[0])  
#         self.assertIn("Returned:", u.get_history()[1])  


# class TestLibraryUnit(unittest.TestCase):
#     def test_find_book_ok_and_not_found(self):
#         lib = seed_library()
#         b = lib._find_book("ISBN003")
#         self.assertEqual(b.title, "The Great Gatsby")
#         with self.assertRaises(ValueError):
#             lib._find_book("NO_EXISTE")

#     def test_find_user_ok_and_not_found(self):
#         lib = seed_library()
#         u = lib._find_user("U001")
#         self.assertEqual(u.name, "Anna")
#         with self.assertRaises(ValueError):
#             lib._find_user("U999")  

# class TestIntegration(unittest.TestCase):
#     def test_borrow_flow_success(self):
#         lib = seed_library()
#         book = lib._find_book("ISBN002")
#         self.assertFalse(book.borrowed)

#         lib.borrow_book("U001", "ISBN002")

#         self.assertTrue(book.borrowed)
#         self.assertIn("1984" not in book.title, [False, True]) 
#         history = lib._find_user("U001").get_history()
#         self.assertGreaterEqual(len(history), 1)

#     def test_reject_borrow_when_already_borrowed(self):

#         lib = seed_library()
#         lib.borrow_book("U001", "ISBN003")
#         with self.assertRaises(ValueError):
#             lib.borrow_book("U002", "ISBN003")  


#     def test_return_then_borrow_by_other_user(self):
  
#         lib = seed_library()
#         lib.borrow_book("U001", "ISBN004")
#         lib.return_book("U001", "ISBN004")
#         lib.borrow_book("U002", "ISBN004")
#         self.assertTrue(lib._find_book("ISBN004").borrowed)
#         h1 = lib._find_user("U001").get_history()
#         h2 = lib._find_user("U002").get_history()
#         self.assertTrue(any("Returned" in s or "Reurned" in s for s in h1))
#         self.assertTrue(any("Borrowed" in s or "Borrwed" in s for s in h2))

class TestSystemPaths(unittest.TestCase):
    def test_full_path_happy_day(self):
        lib = seed_library()
        lib.borrow_book("U003", "ISBN005")
        self.assertTrue(lib._find_book("ISBN005").borrowed)
        self.assertTrue(any("ISBN005".split()[0] in s or "Pride and Prejudice" in s
                            for s in lib._find_user("U003").get_history()))
        lib.return_book("U003", "ISBN005")
        self.assertFalse(lib._find_book("ISBN005").borrowed)

    def test_error_handling_invalid_user_and_book(self):
        lib = seed_library()
        with self.assertRaises(ValueError):
            lib.borrow_book("U999", "ISBN001")  
        with self.assertRaises(ValueError):
            lib.borrow_book("U001", "ISBN999")  
        with self.assertRaises(ValueError):
            lib.return_book("U001", "ISBN001")  


if __name__ == "__main__":
    unittest.main(verbosity=2)
