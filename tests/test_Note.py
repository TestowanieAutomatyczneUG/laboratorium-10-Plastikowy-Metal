import unittest

from sample.Note import Note


class TestNote(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(Note("As", 3.14).get_name(), "As")

    def test_get_note(self):
        self.assertEqual(Note("As", 3.14).get_note(), 3.14)

    def test_note_wrong_name1(self):
        self.assertRaises(Exception, Note, None, 3.14)

    def test_note_wrong_name2(self):
        self.assertRaises(Exception, Note, 123, 3.14)

    def test_note_wrong_name3(self):
        self.assertRaises(Exception, Note, "", 3.14)

    def test_note_wrong_note1(self):
        self.assertRaises(Exception, Note, "Strign", 3)

    def test_note_wrong_note2(self):
        self.assertRaises(Exception, Note, "String", 1.12)

    def test_note_wrong_note3(self):
        self.assertRaises(Exception, Note, "String", "String")

    def test_note_wrong_note3(self):
        self.assertRaises(Exception, Note, "String", None)

if __name__ == '__main__':
    unittest.main()
