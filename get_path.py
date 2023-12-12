import os
import shutil

result_folder_name = '1results'
tmp_folder_name = 'tmp'
telemetr_folder_name = 'telemetr'
tgstat_folder_name = 'tgstat'
telega_folder_name = 'telega'

realpath = os.path.dirname(os.path.realpath(__file__))
result_path = os.path.join(realpath, result_folder_name)
result_tmp_path = os.path.join(result_path, tmp_folder_name)

def make_current_dir():
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    if not os.path.isdir(result_tmp_path):
        os.mkdir(result_tmp_path)


def clear_tmp_dir():
    if os.path.isdir(result_tmp_path):
        shutil.rmtree(result_tmp_path)
        os.mkdir(result_tmp_path)


def make_chanel_dir(chanel_name):
    result_out_path = os.path.join(result_tmp_path, chanel_name)

    if not os.path.isdir(result_out_path):
        os.mkdir(result_out_path)

    return result_out_path
