from bs4 import BeautifulSoup
import fake_useragent
import requests

from helpers.shared.words.get_morfology_word import get_words_normal_form


def get_one_assotiation_for_word(word):
    url = f'https://kartaslov.ru/ассоциации-к-слову/{word.strip()}'
    print(222, word)
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    block = soup.find('div', class_="v2-info-block")
    a_arr = block.find_all('a')

    res_out = []
    for elem in a_arr:
        el = elem.text.strip()
        if len(el) > 0:
            res_out.append(el)

    return res_out


def get_arr_assotiation_for_word(arr):
    assotiation_arr = []

    for word in arr:
        if len(word) > 0:
            word_assotiation_arr = get_one_assotiation_for_word(word=word)

            for ass in word_assotiation_arr:
                if ass not in assotiation_arr:
                    assotiation_arr.append(ass)

    return assotiation_arr
