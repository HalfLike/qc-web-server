#!/usr/bin/python
#! -*- coding:utf-8 -*-
from app import app
from flask import jsonify, request
from database import db_session
from models import Message, UserInfo
from myconst import MyConst

 
@app.teardown_appcontext
def shutdown_session(exception=None): 
    db_session.remove()

@app.route('/api/get_message', methods = ['GET'])
def get_message():
    try:
        device = request.args["DeviceId"]
        message = Message.query.filter(Message.DeviceId == device).\
            filter(Message.MessageType == MyConst.MESSAGETYPE_NOT_RECEIVED).first()
        resp = message.get_json()
        Message.query.filter(Message.MessageId == message.MessageId).\
            update({Message.MessageType:MyConst.MESSAGETYPE_RECEIVED})
        db_session.commit()
    except AttributeError, e:
        resp = {'msg':'null', 'flag':'-1'}
    except Exception, e:
        resp = {'msg':'exception:%s' % e.message, 'flag':'-1'}
    return jsonify(resp)

@app.route('/api/feedback', methods=['POST'])
def feedback():
    resp = {'msg':'request params is error', 'flag':'-1'}
    if not request.json : 
        return jsonify(resp)
    try:
        #init_db()
        message = Message(request.json)
        db_session.add(message)
        db_session.commit()
        resp = {'msg':'feedback succeed', 'flag':'0'}
    except KeyError, e:
        resp = {'msg':'request params is error, had not "%s"' % e.message, 'flag':'-1'}
    except Exception, e:
        resp = {'msg':'operated database error, "%s"' % e.message, 'flag':'-1'}
    finally:
        return jsonify(resp)

@app.route('/api/get_userinfo', methods = ['GET'])
def get_userinfo():
    try:
        device = request.args["DeviceId"]
        userinfo = UserInfo.query.filter(UserInfo.DeviceId == device).first()
        resp = userinfo.get_json()
    except Exception, e:
        resp = {'msg':'exception:%s' % e.message, 'flag':'-1'}
    if not userinfo:
        resp = {'msg':'null', 'flag':'-1'}
    return jsonify(resp)

@app.route('/api/post_userinfo', methods=['POST'])
def userinfo():
    resp = {'msg':'request params is error', 'flag':'-1'}
    if not request.json : 
        return jsonify(resp)
    try:
        #init_db()
        userinfo = UserInfo(request.json)
        db_session.merge(userinfo)
        db_session.commit()
        resp = {'msg':'post userinfo succeed', 'flag':'0'}
    except KeyError, e:
        resp = {'msg':'request params is error, had not "%s"' % e.message, 'flag':'-1'}
    except Exception, e:
        resp = {'msg':'operated database error, "%s"' % e.message, 'flag':'-1'}
    finally:
        return jsonify(resp)
