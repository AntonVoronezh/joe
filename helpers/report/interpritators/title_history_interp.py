import os

from get_path import tgstat_folder_name
from helpers.shared.check_similarity import check_similarity, check_jaccard
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def title_history_interp(folder_path, folder, text_name):
    file_path = os.path.join(folder_path, folder)
    file_name = text_name.split('.')[0]
    info_from_file = get_arr_from_txt_file(file_path=file_path, file_name=file_name)

    text_out = ''

    if len(info_from_file) == 1:
        text_out = 'Название не менялось'
        return text_out

    text_out = f'Известно {len(info_from_file)} названий <br /><br />'
    current_title = ''

    for i, elem in enumerate(info_from_file):
        splitted_elem = elem.split('***')
        title = splitted_elem[1]
        data = splitted_elem[0]

        if i == 0:
            current_title = title

        text_out += f'<p class="items">{i+1}. {title} ({data}) <p>'
        similarity = check_similarity(current_title, title)
        # jaccard = check_jaccard(current_title.split(' '), title.split(' '))
        # print(title, f'схожесть стекущим {similarity}')

    return text_out
