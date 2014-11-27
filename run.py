#!/usr/bin/python
#! -*- coding:utf-8 -*-
from app import app

@app.route('/')
def index():
    return "<span style='color:red'>Welcom to HalfLike's world!</span>"

if __name__ == '__main__':
    app.run(debug=True)