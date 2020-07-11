import nbtlib


def items(entries):
    if isinstance(entries, list):
        return [[i, entries[i]] for i in range(len(entries))]
    if isinstance(entries, nbtlib.Compound):
        return entries.items()
