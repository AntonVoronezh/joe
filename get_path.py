import os
import shutil

from settings import is_telemetr_check, is_tgstat_check, is_telega_check

result_folder_name = '1results'
tmp_folder_name = 'tmp'
telemetr_folder_name = 'telemetr'
tgstat_folder_name = 'tgstat'
telega_folder_name = 'telega'

realpath = os.path.dirname(os.path.realpath(__file__))
result_path = os.path.join(realpath, result_folder_name)
result_tmp_path = os.path.join(result_path, tmp_folder_name)
result_tmp_telemetr_path = os.path.join(result_tmp_path, telemetr_folder_name)
result_tmp_tgstat_path = os.path.join(result_tmp_path, tgstat_folder_name)
result_tmp_telega_path = os.path.join(result_tmp_path, telega_folder_name)


def make_current_dir():
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    if not os.path.isdir(result_tmp_path):
        os.mkdir(result_tmp_path)
    if is_telemetr_check:
        if not os.path.isdir(result_tmp_telemetr_path):
            os.mkdir(result_tmp_telemetr_path)
    if is_tgstat_check:
        if not os.path.isdir(result_tmp_tgstat_path):
            os.mkdir(result_tmp_tgstat_path)
    if is_telega_check:
        if not os.path.isdir(result_tmp_telega_path):
            os.mkdir(result_tmp_telega_path)


def clear_tmp_dir():
    if os.path.isdir(result_tmp_path):
        shutil.rmtree(result_tmp_path)
        os.mkdir(result_tmp_path)