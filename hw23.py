import os


def get_files_info(*args):
    for root, dirs, files in os.walk(dir_name):
        for file_name in files:
            abs_name = os.path.join(root, file_name)
            file_info = os.stat(abs_name)
            yield abs_name, file_info


dir_name = r'.'
files_sorted_by_size = sorted(get_files_info(dir_name), reverse=True, key=lambda x: x[1].st_size)
print('\n'.join(str(value) for value in files_sorted_by_size[:10]))
