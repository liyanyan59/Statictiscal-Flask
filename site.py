# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import glob
import os
from flask import Flask, render_template, send_from_directory, make_response, send_file

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
    fname = filename.encode('cp936')
    return send_from_directory(MyFolder, fname, mimetype='application/octet-stream')


if __name__ == '__main__':
    app.run()
    # app.run('0.0.0.0')
