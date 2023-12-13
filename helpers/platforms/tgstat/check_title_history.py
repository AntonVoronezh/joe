import time

from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from helpers.shared.check_similarity import check_similarity
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_tgstat_check_title_history, is_tgstat_save_screenshot
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_title_history(driver, result_out_path, channel_name):
    file_name = '2_title_history'
    current_link = f'https://tgstat.ru/channel/{channel_name}/history'

    if is_tgstat_check_title_history:
        print(Fore.GREEN + f'check_title_history' + Fore.RESET, flush=True)
        driver.get(current_link)
        driver.find_element(By.XPATH, '//a[@href="#h-title"]').click()
        time.sleep(1)
        modal_html = driver.find_element(By.CSS_SELECTOR, 'div#h-title')
        html = modal_html.get_attribute("outerHTML")
        soup = BeautifulSoup(html, 'lxml')

        title_history_li = soup.find_all('li')

        current_title = ''
        for i, elem in enumerate(title_history_li):
            div_arr = elem.find_all('div', class_='col')
            data = div_arr[0].text.strip()
            title = div_arr[1].text.strip()
            if i == 0:
                current_title = title
            similarity = check_similarity(current_title, title)
            line = f'{data}***{title}***{similarity}'

            add_more_line_in_txt_file(line=line, folder_path=result_out_path, file_name=file_name)

        if is_tgstat_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_out_path, file_name=file_name)

        # modal_html.find_element(By.CSS_SELECTOR, 'button.custom-close-button-top').click()



