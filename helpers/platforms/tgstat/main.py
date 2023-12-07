from colorama import Fore

from helpers.platforms.tgstat.check_red_line import check_red_line
from settings import is_tgstat_check


def check_channel_in_tgstat(driver, channel_name):
    if is_tgstat_check:
        current_link = f'https://tgstat.ru/channel/{channel_name}'
        driver.get(current_link)

        # проверка на красную метку
        check_red_line(driver=driver, channel_name=channel_name)

