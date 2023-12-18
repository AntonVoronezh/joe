import os

from get_path import yakor_tag
from helpers.report.helpers.css_blocks import yakor
from helpers.report.helpers.open_save_template import open_save_template
from helpers.report.helpers.replace_text import replace_text


def handle_section_yakor(dst_template, section_id, section_name):
    replaced_arr = [
        ('%section_id%', section_id),
        ('%section_name%', section_name)
    ]
    yakor_out = replace_text(block=yakor, replaced_arr=replaced_arr)

    replaced_element_arr = [(yakor_tag, f'{yakor_out} \n {yakor_tag}')]
    open_save_template(dst_template=dst_template, replaced_element_arr=replaced_element_arr)
