#-*- coding=ascii -*-
import itchat
from itchat.content import *
import requests

# import numpy

apiUrl = "http://www.tuling123.com/openapi/api"


def get_info(message):
    data = {
        "key": "d82ddc14269b4b4ebf5aa6848977a75e",
        "info": message,
        "userid": "robot"
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        if r['code'] == 100000:
            info = r["text"]
        elif r['code'] == 200000:
            info = r['url']
        else:
            return info
        return info
    except:
        return


CONSTANT = u'0'
NAME = []


@itchat.msg_register([PICTURE, TEXT, RECORDING, MAP, VIDEO, NOTE, SHARING, CARD, ATTACHMENT], isFriendChat=True)
def simple_reply(msg):
    # print(msg)
    global CONSTANT
    global NAME
    if CONSTANT == 0:
        itchat.send(
            u'aaaaa',
            msg['FromUserName'])
        CONSTANT += 1
        NAME.append(msg['FromUserName'])
        return CONSTANT

    else:
        if msg['FromUserName'] in NAME:
            reply = get_info(msg["Text"])
            itchat.send(reply, toUserName=msg['FromUserName'])
        else:
            itchat.send(
                u'1aa10',
                msg['FromUserName'])
            CONSTANT == 1
            NAME.append(msg['FromUserName'])
            return CONSTANT


MOUT = 0
GROUPNAME = []


@itchat.msg_register([PICTURE, TEXT, RECORDING, MAP, VIDEO, NOTE, SHARING, CARD, ATTACHMENT], isGroupChat=True)
def text_reply(msg):
    print(msg['Text'])
    global MOUT
    global GROUPNAME
    print(msg)
    if msg['isAt'] == True:
        if MOUT == 0:
            itchat.send(
                u'1a8503135697',
                msg['FromUserName'])
            MOUT += 1
            GROUPNAME.append(msg['FromUserName'])
            return MOUT
        else:
            if msg['FromUserName'] in GROUPNAME:
                reply = get_info(msg["Text"].strip('@??????????????'))
                itchat.send(reply, toUserName=msg['FromUserName'])
            else:
                itchat.send(
                    u'a18503135697',
                    msg['FromUserName'])
                MOUT == 1
                GROUPNAME.append(msg['FromUserName'])
                return MOUT
                # print(msg)
    else:
        return


itchat.auto_login(hotReload=True)
itchat.run()
