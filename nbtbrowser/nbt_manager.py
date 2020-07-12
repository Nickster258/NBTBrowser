import nbtlib
from tabulate import tabulate

from nbtbrowser.util import items


class NavigationError(Exception):
    """Raised upon error in `cd`"""


class AdditionError(Exception):
    """Raised upon error in `add`"""


class SetError(Exception):
    """Raised upon error in `set`"""


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

    def change_directory(self, key):
        current_node = self.current_node()
        if key == "..":
            if len(self.placement) == 0:
                raise NavigationError(f"Already in root")
            if self.placement:
                self.placement.pop()
        elif key in self.get_keys(current_node):
            if isinstance(current_node[key], (nbtlib.Compound, list)):
                self.placement.append(key)
            else:
                raise NavigationError(f"{key} - Unable to navigate to tag")
        elif isinstance(current_node, list):
            try:
                if int(key) not in range(len(current_node)):
                    raise NavigationError(f"{key} - Invalid index provided")
                self.placement.append(int(key))
            except ValueError:
                raise NavigationError(f"{key} - Unable to navigate to tag")
        else:
            raise NavigationError(f"{key} - No such tag or index")
        self.print_loc()

    def print_loc(self):
        print("/" + "/".join(str(x) for x in self.placement))

    def save(self):
        self.nbtdata.save()

    def remove(self, directive):
        if isinstance(self.current_node(), list):
            del self.current_node()[int(directive)]
        else:
            del self.current_node()[directive]

    def cat(self, key):
        if key == ".":
            print(self.current_node())
        elif isinstance(self.current_node(), list):
            try:
                print(self.current_node()[int(key)])
            except ValueError:
                raise ValueError(f"'{key}'")
        else:
            print(self.current_node()[key])

    def add(self, inp):
        if isinstance(self.current_node(), list):
            self.current_node().append(nbtlib.parse_nbt(inp))
        else:
            args = inp.split()
            if len(args) < 2:
                raise AdditionError("Invalid number of arguments passed - Expected 2")
            if args[0] in self.current_node():
                raise AdditionError(f"{args[0]} - Key already exists in directive")
            nbt = ''.join(args[1:])
            self.current_node()[args[0]] = nbtlib.parse_nbt(nbt)

    def set(self, inp):
        args = inp.split()
        if len(args) < 2:
            raise SetError("Invalid number of arguments passed - Expected 2")
        nbt = ''.join(args[1:])
        current_node = self.current_node()
        if isinstance(current_node, list):
            index = int(args[0])
            if index not in range(len(current_node)):
                raise SetError(f"{index} - Index outside of list range")
            current_node[index] = nbtlib.parse_nbt(nbt)
        else:
            current_node[args[0]] = nbtlib.parse_nbt(nbt)

    def tree(self, node, key, spacing):
        spacing = f"  {spacing}"
        if isinstance(node, nbtlib.Compound):
            keys = node.keys()
            if len(keys) == 0:
                print(f"{spacing}{key} - Compound: {{}}")
            else:
                print(f"{spacing}{key} - Compound:")
                for subkey in keys:
                    self.tree(node[subkey], subkey, spacing)
        elif isinstance(node, nbtlib.List):
            length = len(node)
            if length == 0:
                print(f"{spacing}{key} - List[{node.subtype.__name__}]: {{}}")
            else:
                print(f"{spacing}{key} - List[{node.subtype.__name__}]:")
                for subkey in range(len(node)):
                    self.tree(node[subkey], subkey, spacing)
        else:
            print(f"{spacing}{key} - {type(node).__name__}")
