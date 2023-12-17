import time

from bs4 import BeautifulSoup
from colorama import Fore

from get_path import red_line_str, telega_folder_name, make_platform_in_chanel_dir
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_telega_check_exist, is_telega_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_exist(driver, result_out_path):
    if is_telega_check_exist:
        print(Fore.GREEN + f'check_exist' + Fore.RESET, flush=True)

        file_name = red_line_str
        result_platform_in_chanel_path = make_platform_in_chanel_dir(result_out_path=result_out_path, platform_name=telega_folder_name)


        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('div', class_='channel-name')

        if alert_div is None:
            result = f'None'
        else:
            result = f'Yes'

        add_more_line_in_txt_file(line=result, folder_path=result_platform_in_chanel_path, file_name=file_name)

        if is_telega_save_screenshot:
            time.sleep(1)
            save_screen_with_sign(driver=driver, result_out_path=result_platform_in_chanel_path, file_name=file_name)