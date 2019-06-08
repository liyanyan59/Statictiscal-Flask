# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 13:47
# @Author  : LY
# @FileName: browser
# @Software: PyCharm
# @Official Accounts：大数据学习废话集

import time

import selenium
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser:
    req = None

    def __init__(self):
        self.option = self.get_option()
        self.chrome = webdriver.Chrome(options=self.option)
        self.login("1024407342@qq.com", "123789")

    def login(self, username, passwd):
        self.chrome.get("https://login.aliexpress.com/buyer.htm")
        self.chrome.switch_to.frame('alibaba-login-box')
        pwd_btn = self.chrome.find_element_by_xpath('//input[@type="password"]')
        act_btn = self.chrome.find_element_by_xpath('//input[@id="fm-login-id"]')
        submit_btn = self.chrome.find_element_by_xpath('//button[@class="fm-button fm-submit password-login"]')
        act_btn.send_keys(username)
        time.sleep(1)
        pwd_btn.send_keys(passwd)
        time.sleep(1)
        submit_btn.send_keys(Keys.ENTER)
        time.sleep(3)

        if 'class="close-layer"' in self.chrome.page_source:
            try:
                element = self.chrome.find_element_by_xpath('//a[@class="close-layer"]')
                self.chrome.execute_script("arguments[0].click();", element)  # 关闭href为js的a标签
            except selenium.common.exceptions.NoSuchElementException:
                pass

    def get_option(self):
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument('--no-sandbox')
        # option.add_argument('--disable-gpu')
        option.add_argument('--log-level=3')
        # 不显示图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        option.add_experimental_option("prefs", prefs)
        return option

    def close(self):
        self.chrome.close()
        self.chrome.quit()

    def get_details(self, keyword):
        search_btn = self.chrome.find_element_by_xpath('//input[@id="search-key"]')
        search_btn.clear()
        search_btn.send_keys(keyword)
        search_btn.send_keys(Keys.ENTER)

        # time.sleep(1)

        if 'class="close-layer"' in self.chrome.page_source:
            try:
                element = self.chrome.find_element_by_xpath('//a[@class="close-layer"]')
                self.chrome.execute_script("arguments[0].click();", element)  # 关闭href为js的a标签
            except selenium.common.exceptions.NoSuchElementException:
                return []

        html = etree.HTML(self.chrome.page_source)

        infos = []
        index = 1
        _max = 480
        page = 1
        while index <= _max:
            url_list = html.xpath('//a[@class="history-item product "]/@href')

            # print('第%s页一共%s条' % (page, len(url_list)))
            for url in url_list:
                # infos[str(index)] = url
                infos.append({'id': str(index), 'url': url})
                index += 1

            # 下一页
            page += 1
            next_btn = self.chrome.find_element_by_xpath('//a[@class="page-next ui-pagination-next"]')
            next_btn.send_keys(Keys.ENTER)
            # time.sleep(0.8)
            html = etree.HTML(self.chrome.page_source)
            if page > 15:
                break

        # infos = {k: infos[k] for k in list(infos.keys())[:_max]}
        infos = infos[:_max]
        return infos