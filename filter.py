#!/usr/bin/python3

import re
import sys

# 'vim-tiny': newly installed as '2:7.4.963-4deepin' (from 'universe'):

#test = "'vim-tiny': newly installed as '2:7.4.963-4deepin' (from 'universe'):"
r = re.compile("'(.+)':.+'(.+)' \(from '(.+)'\)")

max_item_size = 55

def get_formatted_item(item, size):
    delta = size - (len(item) * 2)
    if delta < 1:
        delta = 1
    return "%s%s" %(item, " " * delta)


def filter_output(file_path):
    with open(file_path) as fp:
        while True:
            line = fp.readline()
            if not len(line):
                break
            if not line.startswith("'"):
                continue

            l = r.findall(line)
            filter_tuple = l[0]
            if len(filter_tuple) != 3:
                print(">>>W: Ah oh, length of filter tumple incorrect")

            name = filter_tuple[0]
            version = filter_tuple[1]
            repo = filter_tuple[2]

            _name = get_formatted_item(name, max_item_size)
            _version = get_formatted_item(version, max_item_size)
            _repo = get_formatted_item(repo, max_item_size)

            print("%s%s%s" %(_name, _version, _repo))


if __name__ == "__main__":
    print("Package                  version                    repo")
    file_path = sys.argv[1]
    filter_output(file_path)
