# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:18
# @Author  : LY
# @FileName: site
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import os

import time
from flask import Flask, render_template, Response, send_from_directory, request, jsonify
from werkzeug.contrib.fixers import ProxyFix
import json

# from model import db
from utils import url_parser


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
    if os.path.isfile(name):
        return Response(json.dumps({'status': True}), mimetype='application/json')
        # running
    else:
        return Response(json.dumps({'status': False}), mimetype='application/json')


@app.route("/download-xlsx/files/<filename>")
def download_xlsx(filename):
    status = True
    name = './static/files/%s.t' % filename.split(".")[0]

    while status:
        if os.path.isfile(name):
            status = True
        else:
            status = False
        time.sleep(10)
    directory = './static/files/%s' % filename.split(".")[0]
    return send_from_directory(directory, filename, as_attachment=True)


@app.route("/xlsx")
def xlsx():
    return render_template('abc.html')


@app.route('/urls')
def urls():
    return render_template('www.html')


@app.route('/abc/<keywords>')
def get_infos(keywords):
    infos = {}
    print('开始辽')
    if ";" in keywords:
        keywords = keywords.split(";")
    elif "；" in keywords:
        keywords = keywords.split("；")
    else:
        keywords = [].append(keywords)

    print('这里没有错的吧')

    for keyword in keywords:
        infos[keyword] = url_parser(keyword)
    print('are you kidding me?')

    return render_template('table2.html', keywords=list(infos.keys()), items=list(infos.values()))


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=8088, debug=True)
