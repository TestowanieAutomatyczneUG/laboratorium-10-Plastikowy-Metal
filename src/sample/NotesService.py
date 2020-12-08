from src.sample.NotesStorage import NotesStorage


def avg(all_grades, res=0):
    print(all_grades)
    for grade in all_grades:
        res += grade

    return round(res / len(all_grades), 2)


class NotesService:
    def __init__(self):
        self.notes_storage = NotesStorage()

    def add(self, note):
        self.notes_storage.add(note)

    def average_of(self, name):
        all_grades = self.notes_storage.get_all_notes_of(name)

        return avg(all_grades)

    def clear(self):
        self.notes_storage.clear()
