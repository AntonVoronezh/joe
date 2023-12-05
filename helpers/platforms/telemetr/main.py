from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from helpers.platforms.telemetr.check_red_line import check_red_line
from settings import is_telemetr_check

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
service = Service(executable_path="C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


def check_channel_in_telemetr(channel_name):
    if is_telemetr_check:
        current_link = f'https://telemetr.me/{channel_name}'
        driver.get(current_link)

        # проверка на красную метку
        check_red_line(driver=driver, channel_name=channel_name)

