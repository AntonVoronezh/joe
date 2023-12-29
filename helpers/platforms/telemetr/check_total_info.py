import re
import time

from bs4 import BeautifulSoup
from colorama import Fore

from get_path import telemetr_folder_name, make_platform_in_chanel_dir, total_info_str
from helpers.shared.remove_from_text import  remove_all_in_title, remove_all_except_ru_text
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
        div_content = soup.find('div', class_='kt-widget__content')
        opis = soup.find('div', class_='kt-widget__info')
        title = div_content.find('a', class_='kt-widget__username')
        category_all = soup.find_all('option', {'data-n': "1"})

        ffff = str(opis).split('<br')[0]
        opis_re = re.sub(r"<[^>]+>", " ", ffff, flags=re.S).strip().lower()

        opis_removed = remove_all_in_title(text=opis_re, dop=[])
        title_removed = remove_all_in_title(text=title.text.lower(), dop=[])

        result = opis_removed.split(' ')
        result.append(title_removed)

        for elem in category_all:
            elem_str = elem.text.lower()

            if '#' in elem_str:
                d = remove_all_except_ru_text(text=elem_str, dop=[])
                result.append(d)


        line = ' '.join(result)

        add_more_line_in_txt_file(line=line, folder_path=result_platform_in_chanel_path, file_name=file_name)
