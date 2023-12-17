import os
import shutil

from get_path import report_path, result_out_path


def copy_template_files(channel_name):
    src_template = os.path.join(report_path, 'template/template.html')
    src_modal_js = os.path.join(report_path, 'template/modal.js')
    src_top_js = os.path.join(report_path, 'template/top.js')
    src_style_css = os.path.join(report_path, 'template/style.css')
    dst_path = os.path.join(result_out_path, channel_name)

    if not os.path.isdir(dst_path):
        os.mkdir(dst_path)
    dst_template = os.path.join(dst_path, 'index.html')
    dst_modal_js = os.path.join(dst_path, 'modal.js')
    dst_top_js = os.path.join(dst_path, 'top.js')
    dst_style_css = os.path.join(dst_path, 'style.css')

    shutil.copyfile(src_template, dst_template)
    shutil.copyfile(src_modal_js, dst_modal_js)
    shutil.copyfile(src_top_js, dst_top_js)
    shutil.copyfile(src_style_css, dst_style_css)

    return dst_template