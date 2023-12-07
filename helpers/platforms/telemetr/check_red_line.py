from bs4 import BeautifulSoup

from get_path import result_tmp_path
from helpers.shared.make_img_sign import get_image
from helpers.shared.remove_from_text import remove_all_except_numbers
from settings import is_telemetr_check_red_line, is_telemetr_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_red_line(driver, result_out_path):
    file_name = '1_red_line'

    if is_telemetr_check_red_line:
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
            driver.save_screenshot(f'{result_tmp_path}/img.png')
            get_image(path_out=f'{result_out_path}/{file_name}')
