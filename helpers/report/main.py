import os
import uuid

from get_path import result_path, result_tmp_path, red_line_str, red_line_tag, check_title_str, title_history_tag, \
    mentioned_table_str, mentioned_table_tag, result_out_path, index_links_block_tag
from helpers.report.handle_block import handle_block
from helpers.report.helpers.copy_template_files import copy_template_files
from helpers.report.helpers.get_cards import get_cards
from helpers.report.helpers.handle_page_title import handle_page_title
from helpers.report.helpers.open_save_template import open_save_template
from helpers.report.helpers.section_names import section_name_red_line, section_name_title_history, \
    section_name_mentioned_table
from helpers.report.interpritators.mentioned_table_interp import mentioned_table_interp
from helpers.report.interpritators.red_line_interp import red_line_interp
from helpers.report.interpritators.title_history_interp import title_history_interp
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file

# random_id = 'str(uuid.uuid4())'
random_id = 'psychology'
channel_names = get_arr_from_txt_file(file_path=result_path, file_name='channel_names')
def make_report():
    for channel_name in channel_names:
        folder_path = os.path.join(result_tmp_path, channel_name)

        dst_template = copy_template_files(channel_name=channel_name, random_id=random_id)

        handle_page_title(dst_template=dst_template, channel_name=channel_name)

        # red_line
        cards_red_line_arr = get_cards(random_id=random_id, folder_path=folder_path, channel_name=channel_name, block_name=red_line_str,
                              section_name=section_name_red_line, interp=red_line_interp)
        handle_block(dst_template=dst_template, section_name=section_name_red_line, tag_name=red_line_tag, cards_arr=cards_red_line_arr)


        # title_history
        cards_title_history_arr = get_cards(random_id=random_id, folder_path=folder_path, channel_name=channel_name, block_name=check_title_str,
                                       section_name=section_name_title_history, interp=title_history_interp)
        handle_block(dst_template=dst_template, section_name=section_name_title_history, tag_name=title_history_tag,
                     cards_arr=cards_title_history_arr)


        # mentioned_table
        cards_mentioned_table_arr = get_cards(random_id=random_id, folder_path=folder_path, channel_name=channel_name, block_name=mentioned_table_str,
                                       section_name=section_name_mentioned_table, interp=mentioned_table_interp)
        handle_block(dst_template=dst_template, section_name=section_name_mentioned_table, tag_name=mentioned_table_tag,
                     cards_arr=cards_mentioned_table_arr)



def make_index():
    dst_path_random_id = os.path.join(result_out_path, random_id)
    dst_index_template = os.path.join(dst_path_random_id, 'index.html')

    a_href_arr = []

    for channel_name in channel_names:
        a_href = f'<a href="{channel_name}/index.html">{channel_name}</a><br>'
        a_href_arr.append(a_href)
        a_href_out = '\n'.join(a_href_arr)

    replaced_element_arr = [
        (index_links_block_tag, a_href_out)
    ]
    open_save_template(dst_template=dst_index_template, replaced_element_arr=replaced_element_arr)



# make_report()
# make_index()
