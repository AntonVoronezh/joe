import time
from random import choice

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from helpers.platforms.telemetr.mentioned_table.clicks.click_with_reposts import click_with_reposts
from helpers.shared.save_screen_with_sign import save_screen_with_sign
from settings import is_telemetr_save_screenshot


def get_mentioned_table(driver, result_out_path, file_name):
    click_with_reposts(driver=driver)
    time.sleep(5)

    data_tables_div = driver.find_element(By.CSS_SELECTOR, 'table#who_mentioned')
    driver.execute_script("document.getElementById('who_mentioned').scrollIntoView();")
    # driver.find_element(By.CSS_SELECTOR, 'input#checkbox_reposts_who_mentioned').click()

    out_arr = []
    last_element = None

    while True:
        rand_sleep = choice([5, 6, 7, 8, 9, 10])
        print('таблица "кто упоминал" прокрутка --sleep-- ', rand_sleep)
        time.sleep(rand_sleep)

        driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", data_tables_div)
        all_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dataTables_scrollBody > table > tbody > tr')
        html = driver.page_source

        if is_telemetr_save_screenshot:
            save_screen_with_sign(driver=driver, result_out_path=result_out_path, file_name=file_name)

        soup_for_tr = BeautifulSoup(html, 'lxml')

        data_tables_tr_arr_odd = soup_for_tr.find_all('tr', class_='odd')
        data_tables_tr_arr_even = soup_for_tr.find_all('tr', class_='even')

        for elem in data_tables_tr_arr_odd:
            out_arr.append(elem)
        for elem in data_tables_tr_arr_even:
            out_arr.append(elem)

        try:
            if all_elements[-1] == last_element:
                break
            else:
                last_element = all_elements[-1]
        except:
            break

    # for el in out_arr:
    #     print(el)
    return out_arr
