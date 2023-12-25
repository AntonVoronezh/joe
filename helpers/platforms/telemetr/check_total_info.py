import re
import time

from bs4 import BeautifulSoup
from colorama import Fore

from get_path import telemetr_folder_name, make_platform_in_chanel_dir, total_info_str
from helpers.shared.remove_from_text import remove_all_except_numbers, remove_all_in_title
from settings import is_telemetr_check_total_info
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_total_info(driver, result_out_path):
    if is_telemetr_check_total_info:
        print(Fore.GREEN + f'check_total_info' + Fore.RESET, flush=True)

        file_name = total_info_str
        result_platform_in_chanel_path = make_platform_in_chanel_dir(result_out_path=result_out_path,
                                                                     platform_name=telemetr_folder_name)

        html = driver.page_source
        time.sleep(1)

        soup = BeautifulSoup(html, 'lxml')
        opis = soup.find('div', id='rmjs-1')
        title = soup.find('a', class_='kt-widget__username')

        decode_div = opis.decode_contents(formatter="minimal")
        m_ = re.sub(r"<a.*?</a>", " ", decode_div, flags=re.S)
        m = re.sub(r"<[^>]+>", " ", m_, flags=re.S).strip()
        m_plus_title = f'{title.text} {m}'.lower()
        m_arr = m_plus_title.split(' ')

        m_plus_title_arr = []

        for elem in m_arr:
            if 'адми' not in elem:
                if 'купит' not in elem:
                    if 'рекл' not in elem:
                        if '//' not in elem:
                            if len(elem) > 0:
                                elem_removed = remove_all_in_title(text=elem, dop=[])
                                m_plus_title_arr.append(elem_removed)
                                # print(elem_removed)

        result = ' '.join(m_plus_title_arr)

        add_more_line_in_txt_file(line=result, folder_path=result_platform_in_chanel_path, file_name=file_name)
