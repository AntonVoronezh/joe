from bs4 import BeautifulSoup

from get_path import result_tmp_tgstat_path
from settings import is_tgstat_check_red_line
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line(driver, channel_name):
    line_name = 'red_line'

    if is_tgstat_check_red_line:
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('img', {'data-original-title': "Канал заподозрен в использовании методов нечестного продвижения"})

        if alert_div is None:
            result = f'{line_name}|None'
        else:
            text = alert_div.get('data-original-title')
            text_out = text.strip()
            result = f'{line_name}|{text_out}'

        add_more_line_in_txt_file(line=result, folder_path=result_tmp_tgstat_path, file_name=channel_name)
