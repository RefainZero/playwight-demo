# -*- coding: utf-8 -*-
# @Time    : 2024/06/18 22:26
# @Author  : longrong.lang
# @FileName: test_demo.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
# @Motto：你只管努力，剩下的交给天意.
import pytest
from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    page.goto("https://www.baidu.com/")
    yield

    print("after the test runs")


def test_main_navigation(page: Page):
    page.locator("#kw").fill("久曲健 博客园")
    page.get_by_role("button", name="百度一下").click()
    expect(page.locator("#content_left")).to_contain_text("久曲健 - 博客园")

