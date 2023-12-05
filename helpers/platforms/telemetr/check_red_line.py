from bs4 import BeautifulSoup

from get_path import result_tmp_telemetr_path
from helpers.shared.remove_from_text import remove_all_except_numbers
from settings import is_telemetr_check_red_line
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line(driver, channel_name):
    line_name = 'red_line'

    if is_telemetr_check_red_line:
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('div', class_='alert')

        if alert_div is None:
            result = f'{line_name}|None'
        else:
            text = alert_div.text.strip().replace('\n', '').replace('\t', '').replace(' - ', '')
            text_out = remove_all_except_numbers(text, [':', '-', ' ']).strip()
            result = f'{line_name}|{text_out}'

        add_more_line_in_txt_file(line=result, folder_path=result_tmp_telemetr_path, file_name=channel_name)
