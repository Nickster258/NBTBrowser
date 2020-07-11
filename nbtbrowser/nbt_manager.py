import nbtlib
from tabulate import tabulate

from nbtbrowser.util import items


class NbtManager:
    def __init__(self, file):
        self.file = file
        self.nbtdata = nbtlib.load(file)
        self.placement = []

    def current_node(self):
        current = self.nbtdata.root
        for directive in self.placement:
            current = current[directive]
        return current

    def get_keys(self, node):
        if isinstance(self.current_node(), list):
            return list(range(len(self.current_node())))
        else:
            return self.current_node().keys()

    def list(self, full=False):
        if full:
            entries = [[key, type(value).__name__] for key, value in items(self.current_node())]
            print(tabulate(entries, headers=['Key', 'Type']))
        else:
            print(" ".join(str(x) for x in self.get_keys(self.current_node())))

    # TODO Changing directories to non-compound and non-list shouldn't still be a thing
    def change_directory(self, key):
        if key == "..":
            if self.placement:
                self.placement.pop()
        elif key in self.get_keys(self.current_node()):
            self.placement.append(key)
        elif isinstance(self.current_node(), list):
            self.placement.append(int(key))
        self.print_loc()

    def print_loc(self):
        print("/" + "/".join(str(x) for x in self.placement))

    def save(self):
        self.nbtdata.save()

    # TODO Removing list/compounds go oof (sometimes ?????)
    def remove(self, directive):
        self.current_node().__delitem__(directive)

    # TODO Add key existence check
    def cat(self, key):
        print(self.current_node()[key])

    def print(self, key):
        pass
