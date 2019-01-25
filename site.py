# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import os
from flask import Flask, render_template, send_from_directory, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('ddd.html')


# @app.route("/download/<filepath>", methods=['GET'])
# def download_file(filepath):
#     # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
#     return app.send_static_file(filepath)
# @app.route("/download/<filename>")
# def downloader(filename):
#     dirpath = os.path.join(app.root_path, 'static/files')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
#     return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载
@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    # directory = os.getcwd()  # 假设在当前目录
    dirpath = '/root/flask/static/files'
    response = make_response(send_from_directory(dirpath, filename, as_attachment=True)) # 把当前数据封装成一个response
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode('utf-8').decode('utf-8')) # 自定义headers
    return response

if __name__ == '__main__':
    # app.run()
    app.run('0.0.0.0')
