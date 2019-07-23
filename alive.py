# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 8:59 AM
# @Author  : XuChen
# @File    : alive.py

import json
import time
import random
import requests
from twilio.rest import Client
import hashlib


def post_request(phone_number):
    url = 'https://finsuit.bicai365.com'
    md5 = hashlib.md5()  # 应用MD5算法
    data = random.randint(1, 99999999)
    md5.update(str(data).encode('utf-8'))
    DEVICE_ID = str(md5.hexdigest())
    get_v_value = {
        "head": {
            "TYPE": "REQ_NO_VALIDATE",
            "SESSION_ID": "F03CC1F1A3106DA77F00674E8595CB17",
            "SCREEN_SIZE": "1334_750",
            "TOKEN": "",
            "APP_FLAG": "BC",
            "OPEN_API_CHANNEL_ID": "",
            "VERSION": "3.0.8",
            "DEVICE_NAME": "iPhone8,1",
            "CHANNEL": "IOS",
            "SYSTEM_TYPE": "ios",
            "CHANNEL_ID": "1",
            "SCREEN_SCALE": "2",
            "CT_VER": "2",
            "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25",
            "CLIENT_ID": "10",
            "DEVICE_ID": DEVICE_ID
        },
        "param": {
            "PHONE_NUM": str(phone_number),
            "SAFT_CODE": "1234"
        }
    }

    get_v_act_result = requests.post(
        url=url + '/finsuit/finsuitPhone/deal',
        data={"param_key": json.dumps(get_v_value)})

    login_value = {
        "head": {
            "TYPE": "LOGIN",
            "SESSION_ID": "F03CC1F1A3106DA77F00674E8595CB17",
            "SCREEN_SIZE": "1334_750",
            "TOKEN": "",
            "APP_FLAG": "BC",
            "OPEN_API_CHANNEL_ID": "",
            "VERSION": "3.0.8",
            "DEVICE_NAME": "iPhone8,1",
            "CHANNEL": "IOS",
            "SYSTEM_TYPE": "ios",
            "CHANNEL_ID": "1",
            "SCREEN_SCALE": "2",
            "CT_VER": "2",
            "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25",
            "CLIENT_ID": "10",
            "DEVICE_ID": DEVICE_ID
        },
        "param": {
            "FUNCTION_ID": "B000A000",
            "SOURCE_ID": "1",
            "PHONE_CODE": "123456",
            "APP_PLACE": "14",
            "PHONE_NUM": str(phone_number),
            "REMARK_DATA": "登录",
            "IDFA": "C07F2895-8471-40D0-8B1F-72FC9461AC25",
            "NETWORK_TYPE": "2"
        }
    }
    login_act_result = requests.post(
        'https://finsuit.bicai365.com/finsuit/finsuitPhone/deal',
        data={"param_key": json.dumps(login_value)})
    return login_act_result


def report_police():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=142c75d8e3fd88972865b8da90a74c32bd41734ab60daf2dc99d38ca59191d56'
    program = {
        "msgtype": "text",
        "text": {
            "content": "生产服务器有问题请立即查看！\n生产服务器有问题请立即查看！\n生产服务器有问题请立即查看！\n"
        },
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=json.dumps(program), headers=headers)

    account_sid = 'ACd214a78b9d245f4420014b82b2b8de11'
    auth_token = '852096d1bb8a3f416d5129ff318ec681'
    client = Client(account_sid, auth_token)
    client.messages.create(from_='+12407861451',
                           body='故障，速查！',
                           to='+8613911645993')


if __name__ == '__main__':
    # phone_numbers = ["13911645993", "18301401092"]
    phone_numbers = [
        "18303030303", "18301010101", "18305050505", "18302020202",
        "18304040404"
    ]
    # phone_numbers = [
    #     "18303030309", "18301010109", "18305050509", "18302020209",
    #     "18304040409"
    # ]
    start = time.time()
    number = 0
    print(phone_numbers.__len__())
    for each in phone_numbers:
        print(each)
        login_act_result = post_request(each)
        print(login_act_result.text)
        if login_act_result.status_code == 200 and login_act_result.json(
        )["head"]["CODE"] == "0":
            print("登录成功，服务器正常")
            # time.sleep(60)
            pass
        else:
            number = number + 1
            print(number)
            print("登录不成功，服务器异常")
            # time.sleep(60)

    if number == phone_numbers.__len__():
        report_police()
        print("================")

    end = time.time()

    print('Running time: %s Seconds' % (end - start))
