from helpers.report.helpers.css_blocks import h_1_title
from helpers.report.helpers.open_save_template import open_save_template
from helpers.shared.get_today import get_today


def handle_page_title(dst_template, channel_name):
    data = get_today()
    h_1_title_out = h_1_title.replace(' %channel_name%', channel_name).replace('%data%', data)
    replace_arr = ['<!--h_1_title-->', h_1_title_out]

    open_save_template(dst_template=dst_template, replace_arr=replace_arr)
