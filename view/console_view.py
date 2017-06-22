import pprint


class View:
    def input(self, data):
        return input(data)

    def print(self, data):
        print(data[0], " - ", data[1])

    def print_help(self, data):
        print(data)

    # def print(self, data):
    #     print(data['name'], " - ", data['note'])

    def error_(self, val):
        print(val)
