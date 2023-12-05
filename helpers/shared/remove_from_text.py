def remove_all_except_numbers(text, dop):
    en = set('0123456789')
    for el in dop:
        en.add(el)
    conv_text = lambda mas_in: [''.join([j for j in i if j.lower() in en]) for i in mas_in]
    conv_text_el = conv_text(text)
    out = ''.join(conv_text_el)
    return out