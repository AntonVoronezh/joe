import os

from get_path import result_path, result_tmp_path, red_line_str, red_line_tag, check_title_str, title_history_tag, \
    mentioned_table_str, mentioned_table_tag
from helpers.report.handle_block import handle_block
from helpers.report.helpers.copy_template_files import copy_template_files
from helpers.report.helpers.get_cards import get_cards
from helpers.report.helpers.handle_page_title import handle_page_title
from helpers.report.helpers.section_names import section_name_red_line, section_name_title_history, \
    section_name_mentioned_table
from helpers.report.interpritators.mentioned_table_interp import mentioned_table_interp
from helpers.report.interpritators.red_line_interp import red_line_interp
from helpers.report.interpritators.title_history_interp import title_history_interp
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def make_report():
    channel_names = get_arr_from_txt_file(file_path=result_path, file_name='channel_names')

    for channel_name in channel_names:
        folder_path = os.path.join(result_tmp_path, channel_name)

        dst_template = copy_template_files(channel_name=channel_name)

        handle_page_title(dst_template=dst_template, channel_name=channel_name)

        # red_line
        cards_red_line_arr = get_cards(folder_path=folder_path, channel_name=channel_name, block_name=red_line_str,
                              section_name=section_name_red_line, interp=red_line_interp)
        handle_block(dst_template=dst_template, section_name=section_name_red_line, tag_name=red_line_tag, cards_arr=cards_red_line_arr)


        # title_history
        cards_title_history_arr = get_cards(folder_path=folder_path, channel_name=channel_name, block_name=check_title_str,
                                       section_name=section_name_title_history, interp=title_history_interp)
        handle_block(dst_template=dst_template, section_name=section_name_title_history, tag_name=title_history_tag,
                     cards_arr=cards_title_history_arr)


        # mentioned_table
        cards_mentioned_table_arr = get_cards(folder_path=folder_path, channel_name=channel_name, block_name=mentioned_table_str,
                                       section_name=section_name_mentioned_table, interp=mentioned_table_interp)
        handle_block(dst_template=dst_template, section_name=section_name_mentioned_table, tag_name=mentioned_table_tag,
                     cards_arr=cards_mentioned_table_arr)


make_report()
