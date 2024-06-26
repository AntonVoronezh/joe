from colorama import Fore

from helpers.platforms.telega.check_red_line import check_exist
from settings import is_telega_check


def check_channel_in_telega(driver, channel_name, result_out_path):
    if is_telega_check:
        print(Fore.BLUE + f'telega' + Fore.RESET)
        replaced_name = channel_name.replace('@','')
        current_link = f'https://telega.in/channels/{replaced_name}/card'
        driver.get(current_link)

        # проверка на красную метку
        check_exist(driver=driver,  result_out_path=result_out_path)

