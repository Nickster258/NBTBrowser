import argparse
import cmd
import os

import nbtlib

from nbtbrowser.nbt_manager import NbtManager, NavigationError, AdditionError, SetError


class NbtPrompt(cmd.Cmd):
    def __init__(self, file):
        super().__init__()
        self.prompt = 'nbt_browser > '
        self.manager = NbtManager(file)
        self.intro = f"Loaded {file}"

    def onecmd(self, line):
        try:
            return super().onecmd(line)
        except NavigationError as navigation_error:
            print(navigation_error)
        except nbtlib.OutOfRange as out_of_range:
            print(out_of_range)
        except nbtlib.EndInstantiation as end_instantiation:
            print(end_instantiation)
        except nbtlib.IncompatibleItemType as incompatible_item_type:
            print(incompatible_item_type)
        except nbtlib.CastError as cast_error:
            print(cast_error)
        except AdditionError as addition_error:
            print(addition_error)
        except SetError as set_error:
            print(set_error)
        except ValueError as value_error:
            print(f"{value_error} - Invalid value provided")
        except KeyError as key_error:
            print(f"{key_error} - Invalid key provided")
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
        return False

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_pwd(self, inp):
        self.manager.print_loc()

    def do_cd(self, inp):
        self.manager.change_directory(inp)

    def do_ll(self, inp):
        self.manager.list(True)

    def do_ls(self, inp):
        self.manager.list()

    def do_rm(self, inp):
        self.manager.remove(inp)

    def do_cat(self, inp):
        self.manager.cat(inp)

    def do_save(self, inp):
        self.manager.save()

    def do_add(self, inp):
        self.manager.add(inp)

    def do_set(self, inp):
        self.manager.set(inp)

    def do_sizes(self, inp):
        print(self.manager.sizes())

    def do_size(self, inp):
        print(self.manager.size(inp))

    def do_tree(self, inp):
        key = "Root"
        if len(self.manager.placement) > 0:
            key = self.manager.placement[-1]
        self.manager.tree(self.manager.current_node(), key, "")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', metavar='file', type=str, required=True)
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File '{args.file}' does not appear to exist")
        exit(1)

    NbtPrompt(args.file).cmdloop()
