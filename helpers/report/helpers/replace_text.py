def replace_text(block, replaced_arr):
    text = block

    for search, replacement in replaced_arr:
        text = text.replace(search, replacement)

    return text
