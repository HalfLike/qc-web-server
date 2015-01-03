#!/usr/bin/python
#! -*- coding:utf-8 -*-
import time
from models import Message
from database import init_db, db_session
from myconst import MyConst

def query_message():
    """query the message that need to reply """
    messages = Message.query.filter(Message.MessageType == MyConst.MESSAGETYPE_NOT_REPLIED).all()
    for msg in messages:
        print msg.get_json()

def reply():
    """reply to user"""
    message_id = raw_input("please input message id and message body to reply user:\n")
    body = raw_input()
    Message.query.filter(Message.MessageId == message_id).update({Message.MessageType:MyConst.MESSAGETYPE_REPLIED})
    msg = Message.query.get(message_id)
    beijing_time = time.time() + 8*3600
    reply = {
        "DeviceId":msg.DeviceId,
        "CreatedTime":time.strftime('%Y-%m-%d %H:%M',time.gmtime(beijing_time)),
        "MessageType":MyConst.MESSAGETYPE_NOT_RECEIVED,
        "MessageBody":body
    }
    reply_msg = Message(reply)
    db_session.add(reply_msg)
    db_session.commit()

if __name__ == '__main__':
    init_db()
    query_message()
    reply()
