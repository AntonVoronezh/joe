from bs4 import BeautifulSoup

from helpers.shared.make_ru_data import make_ru_data


def extract_data_from_who_mentioned(mentioned_table):
    # soup = BeautifulSoup(mentioned_table, 'lxml')
    # tr_arr = soup.find_all('tr')

    result_arr = []

    for i, elem in enumerate(mentioned_table):
        # soup = BeautifulSoup(elem, 'lxml')
        all_td = elem.find_all('td')

        first = all_td[0]
        a_first = first.find('a', class_="who_title")
        span_first = first.find('span')

        if a_first is not None:
            chanel_name = a_first.get("href").replace('/', '')
            chanel_title = a_first.text.strip()
            count_pdp = span_first.text.replace('\'', '')

            second = all_td[1]
            span_second = second.find('span')
            count_rekl = span_second.text.strip()

            third = all_td[2]
            a_third = third.find('a')
            date = make_ru_data(a_third.text)

            is_danger = False
            if 'table-danger' in str(elem):
                is_danger = True

            result = f'{is_danger}***{chanel_name}***{chanel_title}***{count_pdp}***{count_rekl}***{date}'

            if result not in result_arr:
                result_arr.append(result)

    return result_arr
