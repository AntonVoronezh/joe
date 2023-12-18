import os
import random
import shutil

from get_path import result_out_path, check_title_str
from helpers.report.helpers.css_blocks import section, card, yakor, img
from helpers.report.helpers.open_save_template import open_save_template
from helpers.report.helpers.search_files import search_files
from helpers.report.helpers.section_names import section_name_title_history
from helpers.report.interpritators.title_history_interp import title_history_interp


def handle_title_history(folder_path, dst_template, channel_name):
    folders = os.listdir(folder_path)
    section_name = section_name_title_history
    section_id = str(random.randint(1, 1000000000000000))

    if len(folders):
        yakor_out = yakor.replace('%section_id%', section_id).replace('%section_name%', section_name)
        replace_arr = ['<!--yakor-->', f'{yakor_out} </br> \n <!--yakor-->']
        open_save_template(dst_template=dst_template, replace_arr=replace_arr)

    section_arr = []

    for folder in folders:
        result_names = search_files(folder_path=folder_path, folder=folder, name=check_title_str)

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
            dst = os.path.join(result_out_path, channel_name, f'{folder}_{img_name}')
            shutil.copyfile(src, dst)

            img_out = img.replace('%img%', f'{folder}_{img_name}')

        if text_name is not None:
            title_out = folder

            interp_content = title_history_interp(folder_path=folder_path, folder=folder, text_name=text_name)

            card_out_img = card.replace('<!--img-->', img_out)
            card_out_img_2 = card_out_img.replace('%img%', f'{folder}_{img_name}')
            card_out_title = card_out_img_2.replace('%title%', title_out)
            card_out_modal_id = card_out_title.replace('%modal_id%', f'{folder}_{text_name}')
            card_out_section_name = card_out_modal_id.replace('%section_name%', section_name)

            text_for_template = card_out_section_name.replace('%content%', interp_content)
            section_element = text_for_template.replace('%section_content%', f'{card_out_section_name}')

        section_arr.append(section_element)

    cards_out = '\n'.join(section_arr)

    cards_out_1 = cards_out.replace('%section_content%', cards_out)
    cards_out_2 = cards_out_1.replace('%section_name%', section_name)
    cards_out_3 = cards_out_2.replace('%section_id%', section_id)

    section_out_1 = section.replace('%section_content%', cards_out_3)
    section_out_2 = section_out_1.replace('%section_id%', section_id)
    section_out_3 = section_out_2.replace('%section_name%', section_name)

    replace_arr = ['<!--title_history-->', section_out_3]
    open_save_template(dst_template=dst_template, replace_arr=replace_arr)
