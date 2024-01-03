import os

from get_path import telega_folder_name, telemetr_folder_name, red_line_str
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from settings import is_telemetr_check_red_line_history


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

    if folder == telemetr_folder_name:
        if is_telemetr_check_red_line_history:
            history_info_from_file = get_arr_from_txt_file(file_path=file_path, file_name=red_line_str)
            history_last_elem = history_info_from_file[-2]

            if history_last_elem != 'None':
                return f'{text_out} </br> {history_last_elem}'

    return text_out
