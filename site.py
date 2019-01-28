# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
from flask import Flask, render_template, Response, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('ddd.html')


@app.route("/download/files/<filename>", methods=['GET'])
def download_file(filename):
    # with open('./static/files/%s' % filename, 'rb') as target_file:  # 读取文件内容
    #     data = target_file.read()
    # response = Response(data, content_type='application/octet-stream')  # 响应指明类型，写入内容
    # return response
    directory = './static/files'
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':
    # app.run()
    app.run('0.0.0.0')
