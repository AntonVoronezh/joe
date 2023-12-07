from bs4 import BeautifulSoup

from get_path import result_tmp_telega_path
from settings import is_telega_check_exist
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_exist(driver, channel_name):
    line_name = 'is_exist'

    if is_telega_check_exist:
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('div', class_='channel-name')

        if alert_div is None:
            result = f'{line_name}|None'
        else:
            result = f'{line_name}|Yes'

        add_more_line_in_txt_file(line=result, folder_path=result_tmp_telega_path, file_name=channel_name)
