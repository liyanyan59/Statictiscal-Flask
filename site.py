# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import glob
import os
from flask import Flask, render_template, send_from_directory, make_response, send_file, Response

app = Flask(__name__)

MyFolder = '/static/files/'
pattern = '*.zip'

os.chdir(MyFolder)
for fname in glob.glob(pattern):
    if os.path.isfile(fname):
        key = fname.decode('cp936')


@app.route('/')
def hello_world():
    return render_template('ddd.html')


@app.route("/download/files/<filename>", methods=['GET'])
def download_file(filename):
    def send_chunk():  # 流式读取
        store_path = './static/files/%s' % filename
        with open(store_path, 'rb') as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)  # 每次读取20M
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type='application/octet-stream')


if __name__ == '__main__':
    # app.run()
    app.run('0.0.0.0')
