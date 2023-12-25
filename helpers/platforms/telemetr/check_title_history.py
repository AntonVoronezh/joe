import time

from bs4 import BeautifulSoup
from colorama import Fore
from selenium.webdriver.common.by import By

from get_path import check_title_str, make_platform_in_chanel_dir, telemetr_folder_name
from helpers.shared.words.check_similarity import check_similarity
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_telemetr_save_screenshot, is_telemetr_check_title_history
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file


def check_title_history(driver, result_out_path):
    if is_telemetr_check_title_history:
        print(Fore.GREEN + f'check_title_history' + Fore.RESET, flush=True)

        file_name = check_title_str
        result_platform_in_chanel_path = make_platform_in_chanel_dir(result_out_path=result_out_path,
                                                                     platform_name=telemetr_folder_name)

        driver.find_element(By.XPATH, '//a[@data-do="show_modal_title_history"]').click()
        time.sleep(2)
        modal_html = driver.find_elements(By.CSS_SELECTOR, 'div.modal-content')

        # print(len(ff))
        # for el in ff:
        #     print(el.get_attribute("outerHTML"))

        html = modal_html[2].get_attribute("outerHTML")
        soup = BeautifulSoup(html, 'lxml')

        title_history_tr = soup.find('tbody').find_all('tr')

        title_history_arr = []
        for el in title_history_tr:
            out_arr = []
            data = el.find_all('td')[0].text
            title = el.find_all('td')[1].text
            out_arr.append(data)
            out_arr.append(title)

            title_history_arr.append(out_arr)

        current_title = ''
        for i, elem in enumerate(title_history_arr):
            data = elem[0]
            title = elem[1]
            if i == 0:
                current_title = title
            similarity = check_similarity(current_title, title)
            line = f'{data}***{title}***{similarity}'

            add_more_line_in_txt_file(line=line, folder_path=result_platform_in_chanel_path, file_name=file_name)

        if is_telemetr_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_platform_in_chanel_path, file_name=file_name)

        modal_html[2].find_element(By.CSS_SELECTOR, 'button.btn.btn-secondary').click()


