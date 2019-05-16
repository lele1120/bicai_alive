# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 5:38 PM
# @Author  : XuChen
# @File    : aaa.py

import json

import requests
from twilio.rest import Client

get_v_value = {
    "head": {"TYPE": "REQ_NO_VALIDATE", "SESSION_ID": "F03CC1F1A3106DA77F00674E8595CB17", "SCREEN_SIZE": "1334_750",
             "TOKEN": "", "APP_FLAG": "BC", "OPEN_API_CHANNEL_ID": "", "VERSION": "3.0.8",
             "DEVICE_NAME": "iPhone8,1", "CHANNEL": "IOS", "SYSTEM_TYPE": "ios", "CHANNEL_ID": "1",
             "SCREEN_SCALE": "2", "CT_VER": "2", "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25", "CLIENT_ID": "10",
             "DEVICE_ID": "353A0A67-9588-4AC3-9430-55421BF28F31"},
    "param": {"PHONE_NUM": "18301401092", "SAFT_CODE": "1234"}}

get_v_act_result = requests.post('https://finsuit.bicai365.com/finsuit/finsuitPhone/deal',
                                 data={"param_key": json.dumps(get_v_value)})

login_value = {
    "head": {"TYPE": "LOGIN", "SESSION_ID": "F03CC1F1A3106DA77F00674E8595CB17", "SCREEN_SIZE": "1334_750", "TOKEN": "",
             "APP_FLAG": "BC", "OPEN_API_CHANNEL_ID": "", "VERSION": "3.0.8", "DEVICE_NAME": "iPhone8,1",
             "CHANNEL": "IOS", "SYSTEM_TYPE": "ios", "CHANNEL_ID": "1", "SCREEN_SCALE": "2", "CT_VER": "2",
             "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25", "CLIENT_ID": "10",
             "DEVICE_ID": "353A0A67-9588-4AC3-9430-55421BF28F31"},
    "param": {"FUNCTION_ID": "B000A000", "SOURCE_ID": "1", "PHONE_CODE": "123456", "APP_PLACE": "14",
              "PHONE_NUM": "18301401092", "REMARK_DATA": "登录", "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25",
              "NETWORK_TYPE": "2"}}
login_act_result = requests.post('https://finsuit.bicai365.com/finsuit/finsuitPhone/deal',
                                 data={"param_key": json.dumps(login_value)})
lar = json.loads(login_act_result.text)
print(login_act_result.status_code)

try:
    assert login_act_result.status_code == 200
    assert lar["head"]["CODE"] == "0"
    print("登录成功")
except:
    print("登录不成功")
    url = 'https://oapi.dingtalk.com/robot/send?access_token=142c75d8e3fd88972865b8da90a74c32bd41734ab60daf2dc99d38ca59191d56'
    program = {
        "msgtype": "text",
        "text": {"content": "生产服务器有问题请立即查看！\n生产服务器有问题请立即查看！\n生产服务器有问题请立即查看！\n"},
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)

    account_sid = 'ACd214a78b9d245f4420014b82b2b8de11'
    auth_token = '852096d1bb8a3f416d5129ff318ec681'
    client = Client(account_sid, auth_token)
    # message = client.messages.create(from_='+12407861451', body='Server problem check now！！！', to='+8613911645993')
    message = client.messages.create(from_='+12407861451', body='故障，速查！', to='+8613911645993')

