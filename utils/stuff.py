def find_entry_by_id(entries, file_id):
    for entry in entries:
        if entry.file_id == file_id:
            return entry


def get_entry_string_index(tuples):
    if tuples[2] != '':
        return 2
    elif tuples[1] != '':
        return 1
    return 0


def escape_strings(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].replace("\n", "<<NL>>")
        strings[i] = strings[i].replace("\u001b", "<<ESC>>")
    return strings
