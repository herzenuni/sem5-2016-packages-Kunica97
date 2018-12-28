import unittest
import guestBook
import os


class TestCase(unittest.TestCase):

    # существует ли файл
    def test_guest_book_file_exists(self):
        self.assertTrue(os.path.isfile("./book.json"))
    
    # верный ли тип данных
    def test_guest_book_guests_type(self):
        self.assertTrue(isinstance(guestBook.GuestBook().guests, list))
    
    def test_guest_book_type(self):
        self.assertTrue(isinstance(guestBook.GuestBook(), guestBook.GuestBook))

    # работает ли удаление и добавление
    def test_guest_book_guests_add_remove(self):
        book = guestBook.GuestBook()
        book.add("Test1")
        book.add("Test2")
        book.add("Test3")
        book.add("Test4")
        book.remove("Test4")

        lst = list([
            {"Guest_name": "Test1"},
            {"Guest_name": "Test2"},
            {"Guest_name": "Test3"}
        ])

        self.assertEqual(book.guests, lst)


if __name__ == "__main__":
    unittest.main()
