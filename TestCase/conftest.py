# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 5:27 PM
# @Author  : XuChen
# @File    : conftest.py
import pytest
phone_num = ["13911645993"]


@pytest.fixture(params=phone_num)
def make_phone_num(request):
    return request.param