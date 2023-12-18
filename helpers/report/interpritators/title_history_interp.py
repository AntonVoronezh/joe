import os

from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def title_history_interp(folder_path, folder, text_name):
    file_path = os.path.join(folder_path, folder)
    file_name = text_name.split('.')[0]
    info_from_file = get_arr_from_txt_file(file_path=file_path, file_name=file_name)

    text_out = ''

    for elem in info_from_file:
        text_out = text_out + elem

    return text_out
