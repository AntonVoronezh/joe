from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from get_path import make_current_dir, make_chanel_dir
from helpers.platforms.telega.main import check_channel_in_telega
from helpers.platforms.telemetr.main import check_channel_in_telemetr
from helpers.platforms.tgstat.main import check_channel_in_tgstat
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from helpers.shared.time_lambda import time_lambda

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# service = Service(executable_path="C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)

service = Service(executable_path="C:\webdrivers\geckodriver.exe", service_args=['--marionette-port', '2828', '--connect-existing'])
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

make_current_dir()


start_time = datetime.now()
channel_names = get_arr_from_txt_file(file_name='channel_names')

for i, channel_name in enumerate(channel_names):
    print(i, channel_name)

    result_out_path = make_chanel_dir(channel_name)

    check_channel_in_telemetr(driver=driver, channel_name=channel_name, result_out_path=result_out_path)
    check_channel_in_tgstat(driver=driver, channel_name=channel_name, result_out_path=result_out_path)
    check_channel_in_telega(driver=driver, channel_name=channel_name, result_out_path=result_out_path)

time_lambda(start_time=start_time)