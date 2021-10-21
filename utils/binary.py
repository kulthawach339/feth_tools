from struct import pack, unpack


def utf8_length(string):
    return len(string.encode('utf-8'))


def write_utf8_string(f, string):
    buf = string.encode('utf-8')
    f.write(buf)


def write_utf8_string_nt(f, string):
    buf = string.encode('utf-8')
    f.write(buf)
    write_byte(f, 0)


def read_utf8_string_nt(f):
    temp = f.tell()
    length = 0
    while read_byte(f) != 0:
        length += 1
    f.seek(temp)
    line = f.read(length).decode('utf-8')
    skip(f, 1)
    return line


def read_byte(f):
    buf = f.read(1)
    return unpack("b", buf)[0]


def write_byte(f, num):
    f.write(pack("b", num))


def write_int(f, num):
    f.write(pack("i", num))


def read_int(f):
    buf = f.read(4)
    return unpack("i", buf)[0]


def read_uint(f):
    buf = f.read(4)
    return unpack("I", buf)[0]


def read_ushort(f):
    buf = f.read(2)
    return unpack("H", buf)[0]


def skip(f, count):
    f.seek(f.tell() + count)
