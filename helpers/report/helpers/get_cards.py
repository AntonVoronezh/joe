import os
import shutil

from get_path import result_out_path
from helpers.report.helpers.css_blocks import card, img
from helpers.report.helpers.replace_text import replace_text
from helpers.report.helpers.search_files import search_files
from helpers.report.interpritators.red_line_interp import red_line_interp


def get_cards(random_id, folder_path, channel_name, block_name, section_name, interp):
    folders = os.listdir(folder_path)

    section_arr = []

    for folder in folders:
        result_names = search_files(folder_path=folder_path, folder=folder, name=block_name)

        if len(result_names) == 0:
            continue

        text_name = None
        img_name = None

        for elem in result_names:
            if '.txt' in elem:
                text_name = elem
            if '.png' in elem:
                img_name = elem

        img_out = ''

        if img_name is not None:
            src = os.path.join(folder_path, folder, img_name)
            dst = os.path.join(result_out_path, random_id, channel_name, f'{folder}_{img_name}')
            shutil.copyfile(src, dst)

            replaced_img_arr = [
                ('%img%', f'{folder}_{img_name}')
            ]
            img_out = replace_text(block=img, replaced_arr=replaced_img_arr)

        if text_name is not None:
            interp_content = interp(folder_path=folder_path, folder=folder, text_name=text_name)
            replaced_arr = [
                ('<!--img-->', img_out),
                ('%img%', f'{folder}_{img_name}'),
                ('%title%', folder),
                ('%modal_id%', f'{folder}_{text_name}'),
                ('%section_name%', section_name),
                ('%content%', interp_content)
            ]
        section_element = replace_text(block=card, replaced_arr=replaced_arr)
        section_arr.append(section_element)

    return section_arr
