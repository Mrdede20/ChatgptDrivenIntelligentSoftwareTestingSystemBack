import shutil
from zipfile import ZipFile

from flask import Flask, request, send_from_directory, url_for
import os
from datetime import datetime
from flask_cors import CORS
from werkzeug.utils import secure_filename
from Utils.BaseChatgpt.exec import exec_basechatgpt
from Utils.DfPrompting.exec import exec_dfprompting
from Utils.Pynguin.exec import exec_pynguin
import threading
from threading import Lock
app = Flask(__name__)
CORS(app)  # 这行代码配置 CORS 为全局接受任何来源的请求
UPLOAD_FOLDER = "" # 文件上传后的保存路径
# 初始化一个锁对象
directory_lock = Lock()


def ensure_directory_exists(path):
    with directory_lock:
        if not os.path.exists(path):
            os.makedirs(path)


# Pynguin
@app.route('/Pynguin')
def Pynguin():
    exec_pynguin(get_current_time(UPLOAD_FOLDER))
    """处理上传的文件并返回指定xlsx文件的下载链接给前端下载"""
    try:
        current_time = get_current_time(UPLOAD_FOLDER)  # 获取当前时间字符串
        file_path = f'./Utils/Pynguin/data/{current_time}/pynguin-report/statistics.csv'
        if os.path.isfile(file_path):
            # 生成的下载链接应该是一个列表，即使只有一个链接
            download_link = request.host_url.rstrip('/') + url_for('download_file', processing_method='Pynguin')
            return {'files': [download_link]}  # 返回的是一个字典，键为'files'，值为下载链接的列表
        else:
            return {'message': 'File not found'}, 404  # 文件未找到
    except Exception as e:
        return {'message': str(e)}, 500

# DfPrompting
@app.route('/DfPrompting')
def DfPrompting():
    exec_dfprompting(get_current_time(UPLOAD_FOLDER))
    """处理上传的文件并返回指定xlsx文件的下载链接给前端下载"""
    try:
        current_time = get_current_time(UPLOAD_FOLDER)  # 获取当前时间字符串
        file_path = f'./Utils/DfPrompting/data/{current_time}/results.xlsx'
        if os.path.isfile(file_path):
            # 生成的下载链接应该是一个列表，即使只有一个链接
            download_link = request.host_url.rstrip('/') + url_for('download_file', processing_method='DfPrompting')
            return {'files': [download_link]}  # 返回的是一个字典，键为'files'，值为下载链接的列表
        else:
            return {'message': 'File not found'}, 404  # 文件未找到
    except Exception as e:
        return {'message': str(e)}, 500


@app.route('/BaseChatgpt')
def BaseChatgpt():
    exec_basechatgpt(get_current_time(UPLOAD_FOLDER))
    """处理上传的文件并返回指定xlsx文件的下载链接给前端下载"""
    try:
        current_time = get_current_time(UPLOAD_FOLDER)  # 获取当前时间字符串
        file_path = f'./Utils/BaseChatgpt/data/{current_time}/analyzeResults.xlsx'
        if os.path.isfile(file_path):
            # 生成的下载链接应该是一个列表，即使只有一个链接
            download_link = request.host_url.rstrip('/') + url_for('download_file', processing_method='BaseChatgpt')
            return {'files': [download_link]}  # 返回的是一个字典，键为'files'，值为下载链接的列表
        else:
            return {'message': 'File not found'}, 404  # 文件未找到
    except Exception as e:
        return {'message': str(e)}, 500


@app.route('/download/<processing_method>', methods=['GET'])
def download_file(processing_method):
    """提供文件下载"""
    try:
        if processing_method == "pynguin":#pynguin
            return send_from_directory(f'./Utils/Pynguin/data/{get_current_time(UPLOAD_FOLDER)}/pynguin-report', "statistics.csv",
                                       as_attachment=True)
        elif processing_method == "basechatgpt":#basechatgpt
            return send_from_directory(f'./Utils/BaseChatgpt/data/{get_current_time(UPLOAD_FOLDER)}/', "analyzeResults.xlsx",
                                       as_attachment=True)
        elif processing_method == "DfPrompting":#DfPrompting
            return send_from_directory(f'./Utils/DfPrompting/data/{get_current_time(UPLOAD_FOLDER)}/', "results.xlsx",
                                       as_attachment=True)
        else:
            return {'message': 'File not found'}, 404

    except FileNotFoundError:
        return {'message': 'File not found'}, 404


# 下载测试代码压缩包
@app.route('/download/testcodezip')
def download_folder():
    # 你想下载的文件夹路径
    current_time = get_current_time(UPLOAD_FOLDER)
    folder_path = './ProgramTobeTested/' + current_time
    # 压缩文件的路径
    zip_path = './ProgramFolderZip/' + current_time + '.zip'

    # 创建一个 ZipFile 对象
    with ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 写入文件
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(folder_path, '..')))

    # 发送文件
    return send_from_directory(directory=os.path.dirname(zip_path),
                               path=os.path.basename(zip_path),
                               as_attachment=True)


# 保存前端上传的源代码
@app.route('/upload/<program_type>', methods=['POST'])
def upload_files(program_type):
    global UPLOAD_FOLDER  # 声明UPLOAD_FOLDER为全局变量
    # 这里 `program_type` 将会接收 URL 中的路径参数值，例如 "buggy"
    if program_type == "buggy" :
        # 获取当前时间并格式化为 "yyyy-mm-dd-hh-ss" 形式
        current_time = datetime.now().strftime('%Y_%m_%d_%H_%M')
        new_dirname = "python_" + current_time
        # 设置文件上传后的保存路径
        UPLOAD_FOLDER = f'./ProgramTobeTested/{new_dirname}/'
    ensure_directory_exists(UPLOAD_FOLDER + program_type)  # 使用封装的函数来创建目录
    """接收前端上传的文件并保存到指定目录"""
    uploaded_files = request.files.getlist("files")
    threads = []
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER + program_type, filename)
        thread = threading.Thread(target=save_file, args=(file, file_path))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    return {'message': '所有文件上传处理完成'}, 200


def save_file(file, save_path):
    try:
        file.save(save_path)
        print(f"文件 {file.filename} 保存成功")
    except Exception as e:
        print(f"保存文件 {file.filename} 失败: {e}")


def get_current_time(upload_folder):
    # 以'/'分割字符串，并取最后一个元素作为new_dirname
    parts = upload_folder.split('/')
    current_time = parts[-2] if len(parts) > 1 else None
    return current_time


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)