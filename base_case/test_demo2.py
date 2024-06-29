# -*- coding: utf-8 -*-
# @Time    : 2024/06/18 22:26
# @Author  : longrong.lang
# @FileName: test_demo.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
# @Motto：你只管努力，剩下的交给天意.
import re

from playwright.sync_api import Page, expect, sync_playwright


def test_navigationCnblogs(page: Page):
    page.goto("https://www.cnblogs.com/longronglang")
    expect(page).to_have_title(re.compile("久曲健11111111111"))
