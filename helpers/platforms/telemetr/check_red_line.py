from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.remove_from_text import remove_all_except_numbers
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_telemetr_check_red_line, is_telemetr_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line(driver, result_out_path):
    file_name = '1_red_line'

    if is_telemetr_check_red_line:
        print(Fore.GREEN + f'check_red_line' + Fore.RESET, flush=True)
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('div', class_='alert')

        if alert_div is None:
            result = f'None'
        else:
            text = alert_div.text.strip().replace('\n', '').replace('\t', '').replace(' - ', '')
            text_out = remove_all_except_numbers(text, [':', '-', ' ']).strip()
            result = f'{text_out}'

        add_more_line_in_txt_file(line=result, folder_path=result_out_path, file_name=file_name)

        if is_telemetr_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_out_path, file_name=file_name)

