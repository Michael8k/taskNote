from controller.abstract_notes import AbstractNotes


class Notes(AbstractNotes):
    def __init__(self, serializer):
        self.serializer = serializer
        self.notes = self.serializer.load().copy()

    def create_note(self, name, description=None):
        if name != '':
            if name not in self.notes.keys():
                self.notes[name] = description
                self.serializer.save(self.notes)
            else:
                raise ValueError('Note already exists')
        else:
            raise ValueError('note is empty')

    def read_all(self):
        return self.notes.items()

    def read_one(self, name):
        if name in self.notes.keys():
            return self.notes[name]
        else:
            raise KeyError("Note doesn't exist")

    def update_note(self, name, description):
        self.notes[name] = description
        self.serializer.save(self.notes)

    def delete_note(self, name):
        try:
            del self.notes[name]
            self.serializer.save(self.notes)
        except KeyError:
            raise ValueError("Note doesn't exist")
