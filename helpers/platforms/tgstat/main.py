from colorama import Fore

from helpers.platforms.tgstat.check_red_line import check_red_line
from helpers.platforms.tgstat.check_title_history import check_title_history
from settings import is_tgstat_check


def check_channel_in_tgstat(driver, channel_name, result_out_path):
    if is_tgstat_check:
        current_link = f'https://tgstat.ru/channel/{channel_name}'
        driver.get(current_link)

        # проверка на красную метку
        check_red_line(driver=driver, result_out_path=result_out_path)
        # проверка истории названий
        check_title_history(driver=driver, result_out_path=result_out_path, channel_name=channel_name)

