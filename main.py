import configparser
import sys


def configure():
    config = configparser.ConfigParser()
    config.read('settings.conf')
    serializer_module = __import__(config['Serializer']['name'])
    serializer = serializer_module.Serializer()
    view_module = __import__(config['View']['name'])
    view = view_module.View()
    model_module = __import__(config['Model']['name'])
    notes = model_module.Notes(serializer)
    result = [notes, view]

    return result


class NoteBase:
    def __init__(self, notes, view):
        self.notes = notes
        self.view = view
        self.act = {
            "c": self.create,
            "u": self.update,
            "r": self.read_note,
            "a": self.read_all,
            "d": self.delete,
            "h": self.help,
            "e": self.exit,
        }

    def create(self):
        """ create note """
        data = ['enter note: ', 'enter description: ']
        exist = self.view.input(data[0])
        try:
            self.notes.create_note(exist)
            note = self.view.input(data[1])
            self.notes.create_note(exist, note)
        except ValueError as v:
            self.view.error_(v)

    def read_all(self):
        """ read notes """
        for i in self.notes.read_all():
            self.view.print(i)

    def read_note(self):
        """ read one note """
        name = self.view.input('enter note: ')
        try:
            self.view.print(self.notes.read_one(name))
        except KeyError as v:
            self.view.error_(v)

    def update(self):
        """ update note """
        exist = self.view.input('enter note for search: ')
        try:
            self.notes.read_one(exist)
            note = self.view.input('enter description of note for update: ')
            self.view.print(self.notes.update_note(exist, note))
        except (ValueError, KeyError) as k:
            self.view.error_(k)

    def delete(self):
        """ delete note """
        notes = self.view.input('note to del: ')
        try:
            self.notes.delete_note(notes)
        except ValueError as e:
            self.view.error_(e)

    def help(self):
        result = (
            "use 'c' for {}".format(self.create.__doc__),
            "use 'u' for {}".format(self.update.__doc__),
            "use 'r' for {}".format(self.read_note.__doc__),
            "use 'a' for {}".format(self.read_all.__doc__),
            "use 'd' for {}".format(self.delete.__doc__),
            "use 'e' for {}".format(self.exit.__doc__),
        )
        for i in result:
            self.view.print_help(i)

    def exit(self):
        """ exit.. """
        sys.exit('Bye..')


def main():
    while 1:
        try:
            base = NoteBase(configure()[0], configure()[1])
            input_data = input('enter some or (h)elp: ')
            base.act[input_data]()
        except KeyError as v:
            print('error', v)


if __name__ == '__main__':
    main()
