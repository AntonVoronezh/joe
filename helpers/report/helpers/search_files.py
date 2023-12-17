import os


def search_files(folder_path, folder, name):
    folder_path_2 = os.path.join(folder_path, folder)
    files = os.listdir(folder_path_2)

    res_arr = []
    for file_name in files:
        if name in file_name:
            res_arr.append(file_name)

    return res_arr

