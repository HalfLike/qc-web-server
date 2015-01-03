#!/usr/bin/python
#! -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String
from database import Base

class Message(Base):
    __tablename__ = 'message'
    MessageId = Column(Integer, primary_key=True) 
    DeviceId = Column(String(50))
    MessageBody = Column(String(1000))
    MessageType = Column(Integer)
    CreatedTime = Column(String(50))

    def __init__(self, json):
        self.DeviceId = json["DeviceId"]
        self.CreatedTime = json["CreatedTime"]
        self.MessageType = json["MessageType"]
        self.MessageBody = json["MessageBody"]

    def get_json(self):
        return {
            "MessageId":self.MessageId,
            "DeviceId":self.DeviceId,
            "CreatedTime":self.CreatedTime,
            "MessageType":self.MessageType,
            "MessageBody":self.MessageBody
        }


class UserInfo(Base):
    __tablename__ = 'userinfo'
    DeviceId = Column(String(50), primary_key=True)
    UseTimes = Column(Integer)
    LastUseTime = Column(String(50))

    def __init__(self, json):
        self.DeviceId = json["DeviceId"]
        self.UseTimes = json["UseTimes"]
        self.LastUseTime = json["LastUseTime"]

    def get_json(self):
        return {
            "DeviceId":self.DeviceId,
            "UseTimes":self.UseTimes,
            "LastUseTime":self.LastUseTime
        }

