from helpers.platforms.telemetr.check_red_line import check_red_line
from helpers.platforms.telemetr.check_title_history import check_title_history
from settings import is_telemetr_check

def check_channel_in_telemetr(driver, channel_name, result_out_path):
    if is_telemetr_check:
        current_link = f'https://telemetr.me/{channel_name}'
        driver.get(current_link)

        # проверка на красную метку
        check_red_line(driver=driver, result_out_path=result_out_path)
        # проверка истории названий
        check_title_history(driver=driver, result_out_path=result_out_path)

