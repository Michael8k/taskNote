
class Notes:
    def __init__(self, serializer):
        self.serializer = serializer
        self.note = self.serializer.load().copy()

    def create(self, name, number):
        """ create/update contact """
        if name not in self.note:
            self.note[name] = number
            self.serializer.save(self.note)
        else:
            raise ValueError('Contact already exist')

    def read_all(self):
        """ read all contacts """
        res = self.serializer.load()
        return res

    def read_one(self, name=None):
        """ read one contact """
        contacts = self.read_all()
        if name in contacts:
            return self.note[name]
        else:
            self.note()

    def update_note(self, name, number):
        """ func for update data """
        result = self.read_all()
        if name in result:
            self.note[name] = number
            self.serializer.save(self.note)
        else:
            raise ValueError('Contact doesn\'t exist')

    def delete_contact(self, name):
        """ for delete contact """
        try:
            del self.note[name]
            self.serializer.save(self.note)
        except KeyError:
            raise ValueError('Contact already exist')

