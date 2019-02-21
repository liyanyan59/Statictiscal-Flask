# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
from flask import Flask, render_template, Response, send_from_directory
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)


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


@app.route("/get/<filename>")
def get_status(filename):
    name = './static/files/%s.t' % filename
    import os.path
    if os.path.isfile(name):
        return jsonify({'status': True})  # running
    else:
        return jsonify({'status': False})


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8088)
