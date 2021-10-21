from sys import argv
from utils.binary import *
from utils.stuff import escape_strings
import codecs
import json


class Table:
    def __init__(self):
        self.magic = None
        self.table_size = None
        self.unk = None
        self.num_of_msg = None
        self.ptr_size = None
        self.header_size = None
        self.unk2 = None
        self.unk3 = None
        self.unk4 = None
        self.pointers = []
        self.relative_pos = None


def main(args):
    file_path = args[1]
    out_path = args[2]

    out_file_path = "{}/tutorials.json".format(out_path)
    strings = []
    with open(file_path, "rb") as f:
        language_count = read_uint(f)
        language_pointers = []
        for _ in range(language_count):
            language_pointers.append((read_uint(f), read_uint(f)))
        for language_idx in range(language_count):
            f.seek(language_pointers[language_idx][0])
            language_relative_offset = f.tell()
            num_of_tables = read_uint(f)
            table_pointers = []
            for _ in range(num_of_tables):
                table_pointers.append((read_uint(f), read_uint(f)))
            first_table = Table()
            first_table.relative_pos = f.tell()
            first_table.magic = read_uint(f)
            first_table.table_size = read_ushort(f)
            first_table.unk = read_ushort(f)
            first_table.num_of_msg = read_ushort(f)
            first_table.ptr_size = read_ushort(f)
            first_table.header_size = read_ushort(f)
            first_table.unk2 = read_ushort(f)
            first_table.unk3 = read_uint(f)
            first_table.unk4 = read_uint(f)
            for _ in range(first_table.num_of_msg):
                first_table.pointers.append(read_uint(f))
                skip(f, 16)
            for i in range(first_table.num_of_msg):
                f.seek(first_table.relative_pos + first_table.header_size + first_table.pointers[i])
                strings.append(read_utf8_string_nt(f))
            f.seek(language_relative_offset + table_pointers[1][0])
            strings.append("<<DELIM_TABLE>>")
            second_table = Table()
            second_table.relative_pos = f.tell()
            second_table.magic = read_uint(f)
            second_table.table_size = read_ushort(f)
            second_table.unk = read_ushort(f)
            second_table.num_of_msg = read_ushort(f)
            second_table.ptr_size = read_ushort(f)
            second_table.header_size = read_ushort(f)
            second_table.unk2 = read_ushort(f)
            second_table.unk3 = read_uint(f)
            for _ in range(second_table.num_of_msg):
                second_table.pointers.append(read_uint(f))
            for i in range(second_table.num_of_msg):
                f.seek(second_table.relative_pos + second_table.header_size + second_table.pointers[i])
                strings.append(read_utf8_string_nt(f))
            strings.append("<<DELIM_LANGUAGE>>")
    with codecs.open(out_file_path, "w", "utf-8") as f:
        f.write(json.dumps(escape_strings(strings), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main(argv)
