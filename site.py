# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('ddd.html')


@app.route("/download/<filepath>", methods=['GET'])
def download_file(filepath):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file(filepath)


if __name__ == '__main__':
    app.run()
    # app.run('0.0.0.0')
