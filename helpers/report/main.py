import os

from get_path import result_path, result_tmp_path
from helpers.report.handle_red_line import handle_red_line
from helpers.report.helpers.copy_template_files import copy_template_files
from helpers.report.helpers.handle_page_title import handle_page_title
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def make_report():
    channel_names = get_arr_from_txt_file(file_path=result_path, file_name='channel_names')

    for channel_name in channel_names:
        folder_path = os.path.join(result_tmp_path, channel_name)

        dst_template = copy_template_files(channel_name=channel_name)

        handle_page_title(dst_template=dst_template, channel_name=channel_name)
        handle_red_line(folder_path=folder_path, dst_template=dst_template, channel_name=channel_name)


make_report()