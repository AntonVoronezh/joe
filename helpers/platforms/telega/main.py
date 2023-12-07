from helpers.platforms.telega.check_red_line import check_exist
from settings import is_telega_check


def check_channel_in_telega(driver, channel_name):
    if is_telega_check:
        replaced_name = channel_name.replace('@','')
        current_link = f'https://telega.in/channels/{replaced_name}/card'
        driver.get(current_link)

        # проверка на красную метку
        check_exist(driver=driver, channel_name=channel_name)

