import os

from get_path import result_path


def get_arr_from_txt_file(file_name):
    file_path = os.path.join(result_path, f'{file_name}.txt')
    links_arr = []

    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as file:
            for el in file:
                links_arr.append(el.strip())

    return links_arr
