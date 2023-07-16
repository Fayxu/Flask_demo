#!/usr/bin/python# coding=utf-8

"""
编写一个Flask demo 文件


"""

from flask import Flask, request, session, jsonify, app

USERNAME = 'admin'
PASSWORD = '123456'
pp = Flask(__name__)
app.secret_key = 'pithy'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return jsonify({'code': 200, 'msg': 'success'})


@app.route('/info', methods=['get'])
def info():

    if not session.get('logged_in'):
        return jsonify({'code': 401, 'msg': 'please login !!'})


if __name__ == '__main__':
    app.run(debug=True)