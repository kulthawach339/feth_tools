from sys import argv
from utils.excel import parse_excel
from utils.binary import *
from utils.stuff import get_entry_string_index


def main(args):
    entries = parse_excel(args[1])
    out_path = args[2]

    for entry in entries:
        entry_path = "{}/supports/{}".format(out_path, entry.file_id)
        print(entry_path)
        with open(entry_path, "wb") as f:
            lines_count = len(entry.strings)
            write_int(f, 1)
            write_int(f, 1)
            write_int(f, 0x14)
            write_int(f, (4 * lines_count) + 4)
            write_int(f, lines_count)

            pointer = 0
            write_int(f, pointer)
            for i in range(lines_count):
                idx = get_entry_string_index(entry.strings[i])
                pointer += utf8_length(entry.strings[i][idx]) + 1
                write_int(f, pointer)
            for i in range(lines_count):
                idx = get_entry_string_index(entry.strings[i])
                write_utf8_string_nt(f, entry.strings[i][idx])


if __name__ == '__main__':
    main(argv)
