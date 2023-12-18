from helpers.report.helpers.replace_text import replace_text


def open_save_template(dst_template, replaced_element_arr):
    template_for_replaced = open(dst_template, "r", encoding='utf-8')
    template = template_for_replaced.read()
    template_for_replaced.close()

    replaced_text = replace_text(block=template, replaced_arr=replaced_element_arr)

    template_out = open(dst_template, "w", encoding='utf-8')
    template_out.write(replaced_text)
    template_out.close()
