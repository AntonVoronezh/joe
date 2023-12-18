from get_path import h1_title_tag
from helpers.report.helpers.css_blocks import h_1_title
from helpers.report.helpers.open_save_template import open_save_template
from helpers.report.helpers.replace_text import replace_text
from helpers.shared.get_today import get_today


def handle_page_title(dst_template, channel_name):
    data = get_today()

    replace_title_arr = [
        (' %channel_name%', channel_name),
        ('%data%', data)
    ]
    h_1_title_out = replace_text(block=h_1_title, replaced_arr=replace_title_arr)

    replaced_element_arr = [(h1_title_tag, h_1_title_out)]
    open_save_template(dst_template=dst_template, replaced_element_arr=replaced_element_arr)
