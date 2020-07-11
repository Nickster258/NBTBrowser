from cmd import Cmd

from nbtbrowser.nbt_manager import NbtManager


class NbtPrompt(Cmd):
    def __init__(self, file):
        super().__init__()
        self.prompt = 'nbt browser > '
        self.manager = NbtManager(file)
        self.intro = f"Loaded {file}"

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

    def do_print(self, inp):
        self.manager.print(inp)
