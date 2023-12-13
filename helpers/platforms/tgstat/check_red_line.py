from bs4 import BeautifulSoup
from colorama import Fore

from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_tgstat_check_red_line, is_tgstat_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line(driver, result_out_path):
    file_name = '2_red_line'

    if is_tgstat_check_red_line:
        print(Fore.GREEN + f'check_red_line' + Fore.RESET, flush=True)
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('img', {'data-original-title': "Канал заподозрен в использовании методов нечестного продвижения"})

        if alert_div is None:
            result = f'None'
        else:
            text = alert_div.get('data-original-title')
            text_out = text.strip()
            result = f'{text_out}'

        add_more_line_in_txt_file(line=result, folder_path=result_out_path, file_name=file_name)

        if is_tgstat_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_out_path, file_name=file_name)