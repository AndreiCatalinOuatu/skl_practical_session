import os

dirpath = os.getcwd()


def get_subdir_size(path):
    size = 0
    for entry in os.scandir(path):
        if entry.is_file():
            size = size + os.path.getsize(entry)
        elif entry.is_dir():
            size = size + get_subdir_size(entry)
    return size


total_size = 0
for entry in os.scandir(dirpath):
    if entry.is_dir():
        total_size += get_subdir_size(entry)

print(total_size)