#!/usr/bin/python
#! -*- coding:utf-8 -*-
from app import app, url_for

@app.route('/')
def index():
    return "<span style='color:red'>Welcom to HalfLike's world!</span>"

@app.route('/pr')
def pr():
    return url_for('pr', aa=1, _external=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
