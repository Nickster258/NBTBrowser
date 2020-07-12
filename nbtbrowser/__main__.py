import argparse
import os

from nbtbrowser.nbt_prompt import NbtPrompt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', metavar='file', type=str, required=True)
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"File '{args.file}' does not appear to exist")
        exit(1)

    NbtPrompt(args.file).cmdloop()


if __name__ == "__main__":
    main()
