import random
import uuid

from helpers.report.helpers.css_blocks import section
from helpers.report.helpers.handle_section_yakor import handle_section_yakor
from helpers.report.helpers.open_save_template import open_save_template
from helpers.report.helpers.replace_text import replace_text


def handle_block(dst_template, section_name, tag_name, cards_arr):
    if len(cards_arr) == 0:
        return

    section_id = str(uuid.uuid4())

    handle_section_yakor(dst_template=dst_template, section_id=section_id, section_name=section_name)
    cards_out = '\n'.join(cards_arr)

    replaced_section_arr = [
        ('%section_content%', cards_out),
        ('%section_id%', section_id),
        ('%section_name%', section_name)
    ]
    section_out = replace_text(block=section, replaced_arr=replaced_section_arr)

    replaced_element_arr = [
        (tag_name, section_out)
    ]

    open_save_template(dst_template=dst_template, replaced_element_arr=replaced_element_arr)
