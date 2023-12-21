from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from get_path import make_current_dir, make_chanel_dir, result_path, result_tmp_path, clear_tmp_dir
from helpers.platforms.telega.main import check_channel_in_telega
from helpers.platforms.telemetr.main import check_channel_in_telemetr
from helpers.platforms.tgstat.main import check_channel_in_tgstat
from helpers.report.main import make_report, make_index
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from helpers.shared.save_in_txt_file import add_more_line_in_txt_file
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
channel_names = get_arr_from_txt_file(file_path=result_path, file_name='channel_names')
done_channel_names = get_arr_from_txt_file(file_path=result_tmp_path, file_name='done')

print(Fore.RED + f'START' + Fore.RESET)

for i, channel_name in enumerate(channel_names):
    if channel_name in done_channel_names:
        print(Fore.YELLOW + f'Данные {channel_name} уже есть' + Fore.RESET)
        continue

    result_out_path = make_chanel_dir(channel_name)

    check_channel_in_telemetr(driver=driver, channel_name=channel_name, result_out_path=result_out_path)
    check_channel_in_tgstat(driver=driver, channel_name=channel_name, result_out_path=result_out_path)
    check_channel_in_telega(driver=driver, channel_name=channel_name, result_out_path=result_out_path)

    add_more_line_in_txt_file(line=channel_name, folder_path=result_tmp_path, file_name='done')

    print(Fore.RED + f'{i}, {channel_name}' + Fore.RESET, flush=True)

make_report()
make_index()

time_lambda(start_time=start_time)