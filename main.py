# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
from flask import Flask, render_template, Response, send_from_directory, request
from werkzeug.contrib.fixers import ProxyFix
import json

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


@app.route("/get", methods=['POST'])
def get_status():
    filename = request.form['res']
    name = './static/files/%s' % filename
    import os
    if os.path.isfile(name):
        return Response(json.dumps({'status': True}), mimetype='application/json')
        # running
    else:
        return Response(json.dumps({'status': False}), mimetype='application/json')


@app.route("/download-xlsx/files/<filename>")
def download_xlsx(filename):

    directory = './static/files/%s' % filename.split(".")[0]
    return send_from_directory(directory, filename, as_attachment=True)


@app.route("/xlsx")
def xlsx():
    return render_template('abc.html')


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8088, debug=True)
