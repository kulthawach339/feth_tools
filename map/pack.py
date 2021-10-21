from sys import argv
from utils.excel import parse_excel
from utils.stuff import get_entry_string_index
from utils.binary import *


def main(args):
    excel_path = args[1]
    out_path = args[2]
    entries = parse_excel(excel_path)
    for entry in entries:
        entry_path = "{}/map/{}".format(out_path, entry.file_id)
        print(entry_path)
        with open(entry_path, "wb") as f:
            lines_count = len(entry.strings)
            start_offset = (lines_count * 8) + 4
            write_int(f, lines_count)
            for i in range(lines_count):
                idx = get_entry_string_index(entry.strings[i])
                line_length = utf8_length(entry.strings[i][idx]) + 1
                write_int(f, start_offset)
                write_int(f, line_length)
                start_offset += line_length
            for i in range(lines_count):
                idx = get_entry_string_index(entry.strings[i])
                write_utf8_string_nt(f, entry.strings[i][idx])


if __name__ == '__main__':
    main(argv)
