import pymorphy3

morph = pymorphy3.MorphAnalyzer(lang='ru')


def is_NOUN(morph, world):
    # https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html
    f = morph.parse(world)[0].tag
    arr = str(f).split(',')
    is_NOUN = arr[0] == 'NOUN'
    return is_NOUN


def get_words_normal_form(words):
    result = []
    for word in words:
        word_morph = is_NOUN(morph, word)

        if word_morph:
            el_normal_form = morph.parse(word)[0].normal_form

            if el_normal_form not in result:
                result.append(el_normal_form)

    return result
