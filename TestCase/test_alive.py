# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 5:23 PM
# @Author  : XuChen
# @File    : test_alive.py
import pytest
from __future__ import absolute_import

class TestLogin:
    @pytest.allure.feature("Login", "登录")
    @pytest.allure.severity('blocker')
    def test_login(self, data_operation, make_username):
        """
        登录验证获取授权
        """
        with pytest.allure.step("登录"):
            # response_dicts = req.start_request("login", username=make_username)
            response_dicts = req.login_request(username=make_username)
            print(response_dicts)