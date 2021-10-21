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
