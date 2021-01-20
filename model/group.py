from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.group_id = group_id

    def __repr__(self):
        return "{0}: {1}, {2}, {3}".format(self.group_id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.group_id == other.group_id or self.group_id is None or other.group_id is None)\
               and self.name == other.name

    def __hash__(self):
        return hash((self.group_id, self.name))

    def id_or_max(self):
        return int(self.group_id) if self.group_id else maxsize
