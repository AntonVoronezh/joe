import time

from bs4 import BeautifulSoup

from get_path import result_tmp_path
from helpers.shared.make_img_sign import get_image
from settings import is_telega_check_exist, is_telega_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_exist(driver, result_out_path):
    file_name = 'is_exist'

    if is_telega_check_exist:
        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')
        alert_div = soup.find('div', class_='channel-name')

        if alert_div is None:
            result = f'None'
        else:
            result = f'Yes'

        add_more_line_in_txt_file(line=result, folder_path=result_out_path, file_name=file_name)

        if is_telega_save_screenshot:
            time.sleep(1)
            driver.save_screenshot(f'{result_tmp_path}/img.png')
            get_image(path_out=f'{result_out_path}/{file_name}')