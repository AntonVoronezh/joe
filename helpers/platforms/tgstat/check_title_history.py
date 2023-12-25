import time

from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from get_path import check_title_str, make_platform_in_chanel_dir, tgstat_folder_name
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_tgstat_check_title_history, is_tgstat_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_title_history(driver, result_out_path, channel_name):
    current_link = f'https://tgstat.ru/channel/{channel_name}/history'

    if is_tgstat_check_title_history:
        print(Fore.GREEN + f'check_title_history' + Fore.RESET, flush=True)

        file_name = check_title_str
        result_platform_in_chanel_path = make_platform_in_chanel_dir(result_out_path=result_out_path,
                                                                     platform_name=tgstat_folder_name)

        driver.get(current_link)
        driver.find_element(By.XPATH, '//a[@href="#h-title"]').click()
        time.sleep(1)
        modal_html = driver.find_element(By.CSS_SELECTOR, 'div#h-title')
        html = modal_html.get_attribute("outerHTML")
        soup = BeautifulSoup(html, 'lxml')

        title_history_li = soup.find_all('li')

        for i, elem in enumerate(title_history_li):
            div_arr = elem.find_all('div', class_='col')
            data = div_arr[0].text.strip()
            title = div_arr[1].text.strip()
            line = f'{data}***{title}'

            add_more_line_in_txt_file(line=line, folder_path=result_platform_in_chanel_path, file_name=file_name)

        if is_tgstat_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_platform_in_chanel_path, file_name=file_name)




