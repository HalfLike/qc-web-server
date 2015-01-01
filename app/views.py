#!/usr/bin/python
#! -*- coding:utf-8 -*-
from app import app
from flask import Flask, jsonify, abort, request, make_response, url_for

message = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'content': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'time': u'2014-12-20 20:00'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'content': u'Need to find a good Python tutorial on the web', 
        'time': u'2014-12-22 21:00'
    }
]
 
@app.route('/api/get_message', methods = ['GET'])
def get_message():
    return jsonify(message=message)
    