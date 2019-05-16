# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 7:36 PM
# @Author  : XuChen
# @File    : ccc.py

from httmock import urlmatch, HTTMock
import requests


@urlmatch(netloc=r'(.*\.)?google\.com$')
def google_mock(url, request):
        return {'status_code': 500}


with HTTMock(google_mock):

    r = requests.get('http://google.com/')
    print(r.status_code)