import os

from get_path import total_info_str
from helpers.shared.make_union_arr import make_union_arr
from helpers.shared.words.check_similarity import check_similarity, check_jaccard
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from helpers.shared.words.get_assotiation_for_word import get_arr_assotiation_for_word
from helpers.shared.words.get_morfology_word import get_words_normal_form
from helpers.shared.remove_from_text import remove_all_in_title
from helpers.shared.words.prepare_words import prepare_words


def mentioned_table_interp(folder_path, folder, text_name):
    file_path = os.path.join(folder_path, folder)
    file_name = text_name.split('.')[0]
    info_from_file = get_arr_from_txt_file(file_path=file_path, file_name=file_name)

    text_out = ''
    text_out_bot = ''
    text_out_pdp_count = ''
    text_out_not_tema = ''
    text_out_tema = ''

    is_banned, name, title, pdp_count, raz, data = tuple(info_from_file[0].split('***'))

    text_out = f'''
    <u>Известно <b>{len(info_from_file)}</b> размещений</u> 
    <br /><br />
    <u>Последнее размешение</u>
     <br />
     <p class="items">{name} - {title} ({data}) <p>
    '''

    #  на ботоводы
    bot_arr = []

    for elem in info_from_file:
        is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))

        if is_banned == 'True':
            bot_arr.append(elem)

    if len(bot_arr) == 0:
        text_out_bot = '<br /><u>В ботоводных каналах не размещался</u><br />'
    else:
        text_out_bot += f'<br /><u>Размещался в <b>{len(bot_arr)}</b> ботоводных каналах </u><br />'

        for i, elem in enumerate(bot_arr):
            is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))
            text_out_bot = text_out_bot + f'<p class="items">{i + 1}. {name} - {title} ({data}) <p>'

    #  на количество подписчиков
    count_for_prov = 1000
    pdp_count_arr = []

    for elem in info_from_file:
        is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))

        if int(pdp_count) < count_for_prov:
            pdp_count_arr.append(elem)

    if len(pdp_count_arr) == 0:
        text_out_pdp_count = f'<br /><u>В маленьких каналах (меньше {count_for_prov} пдп) не размещался</u><br />'
    else:
        text_out_pdp_count += f'<br /><u>Размещался в <b>{len(pdp_count_arr)}</b> маленьких каналах (меньше {count_for_prov} пдп)</u><br />'

    for i, elem in enumerate(pdp_count_arr):
        is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))
        text_out_pdp_count = text_out_pdp_count + f'<p class="items">{i + 1}. [{raz} раз, {pdp_count} пдп] {name} - {title} ({data})<p>'

    #  на нетематические каналы
    not_tema_arr = []
    tema_arr = []

    opis_plus_title_from_file_arr = get_arr_from_txt_file(file_path=file_path, file_name=total_info_str)
    opis_plus_title_from_file = opis_plus_title_from_file_arr[0].split(' ')
    assotiation_for_opis_plus_title_prepare = prepare_words(words=opis_plus_title_from_file)
    opis_plus_title_normal_forms = get_words_normal_form(words=assotiation_for_opis_plus_title_prepare)
    assotiation_for_opis_plus_title = get_arr_assotiation_for_word(arr=opis_plus_title_normal_forms)

    for elem in info_from_file:
        is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))

        title_removed = remove_all_in_title(text=title, dop=[])
        title_removed_arr = title_removed.lower().split(' ')
        title_prepare = prepare_words(words=title_removed_arr)
        title_normal_forms = get_words_normal_form(words=title_prepare)

        union = make_union_arr(arr_1=assotiation_for_opis_plus_title, arr_2=title_normal_forms)


        if len(union) == 0:
            not_tema_arr.append(elem)
        else:
            tema_arr.append(elem)

    if len(not_tema_arr) == 0:
        text_out_tema = f'<br /><u>Размещадся только в тематических каналах</u><br />'
    else:
        text_out_tema += f'<br /><u>Размещался в <b>{len(tema_arr)}</b> тематических каналах из {len(info_from_file)} размещений</u><br />'

        for i, elem in enumerate(tema_arr):
            is_banned, name, title, pdp_count, raz, data = tuple(elem.split('***'))
            text_out_tema = text_out_tema + f'<p class="items">{i + 1}. {name} - {title} ({data})<p>'

    return text_out + text_out_bot + text_out_pdp_count + text_out_tema
# https://docs.python.org/3/library/difflib.html
