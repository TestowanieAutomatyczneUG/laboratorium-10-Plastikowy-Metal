import unittest
from unittest.mock import *
from src.sample.NotesService import *
from src.sample.NotesStorage import NotesStorage
from src.sample.Note import Note

class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.temp = NotesService()

    def test_add_note(self):
        self.temp.get_all_notes = Mock(name='get_all_notes')
        self.temp.get_all_notes.return_value = [3.0, 4.0]

        self.temp.add(Note('Janush', 3.0))
        self.temp.add(Note('Janush', 4.0))

        result = self.temp.average_of('Janush')
        self.assertEqual(self.temp.average_of('Janush'), result, 'return value from public_method incorrect')

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()