import codecs


def open_save_template(dst_template, replace_arr):
    template_for_replaced = open(dst_template, "r", encoding='utf-8')
    template = template_for_replaced.read()
    template_for_replaced.close()

    replaced_text = template.replace(replace_arr[0], replace_arr[1])

    template_out = open(dst_template, "w", encoding='utf-8')
    template_out.write(replaced_text)
    template_out.close()
