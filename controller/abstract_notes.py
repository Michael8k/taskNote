from abc import abstractmethod, ABCMeta


class AbstractNotes(metaclass=ABCMeta):
    def __init__(self, serializer):
        pass

    @abstractmethod
    def create_note(self, name, description):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_one(self, name):
        pass

    @abstractmethod
    def update_note(self, name, description):
        pass

    @abstractmethod
    def delete_note(self, name):
        pass
