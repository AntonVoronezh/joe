from bs4 import BeautifulSoup
from colorama import Fore

from get_path import red_line_str, telemetr_folder_name, make_platform_in_chanel_dir
from settings import is_telemetr_check_red_line_history
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line_history(driver, result_out_path):
    if is_telemetr_check_red_line_history:
        print(Fore.GREEN + f'check_red_line_history' + Fore.RESET, flush=True)

        file_name = red_line_str
        result_platform_in_chanel_path = make_platform_in_chanel_dir(result_out_path=result_out_path, platform_name=telemetr_folder_name)

        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        desc_div = soup.find('div', class_="float-right")

        if desc_div is None:
            result = f'None'
        else:
            tag_a = desc_div.find('a')
            result = tag_a['data-original-title'].strip()

        add_more_line_in_txt_file(line=result, folder_path=result_platform_in_chanel_path, file_name=file_name)


