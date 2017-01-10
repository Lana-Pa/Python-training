from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # function to get a key for sorting groups by id
    def id_or_max(self):
        if self.id:  # если у группы есть id
            return int(self.id)  # возвращается id
        else:  # если id нет (как в случае с добавленной вручную группой)
            return maxsize  # использовать в качестве id максимально возможное число, которое может использоваться в индексах в списках





