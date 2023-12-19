import os

from get_path import telega_folder_name
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def red_line_interp(folder_path, folder, text_name):
    file_path = os.path.join(folder_path, folder)
    file_name = text_name.split('.')[0]
    info_from_file = get_arr_from_txt_file(file_path=file_path, file_name=file_name)

    last_elem = info_from_file[-1]
    text_out = last_elem

    if folder == telega_folder_name:
        if last_elem == 'None':
            text_out = 'Канал не представлен на платформе'
        if last_elem == 'Yes':
            text_out = 'Канал представлен на платформе'
    else:
        if last_elem == 'None':
            text_out = 'Отметки от платформы нет'

    return text_out
