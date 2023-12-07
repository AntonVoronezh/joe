from get_path import result_tmp_path
from helpers.shared.make_img_sign import make_image_sign


def save_screen_with_sign(driver, result_out_path, file_name):
    driver.save_screenshot(f'{result_tmp_path}/img.png')
    make_image_sign(path_out=f'{result_out_path}/{file_name}')