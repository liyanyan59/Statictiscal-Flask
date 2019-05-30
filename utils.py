# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 19:50
# @Author  : LY
# @FileName: test
# @Software: PyCharm
# @Official Accounts：大数据学习废话集
import collections
import time

import requests
import selenium
from selenium import webdriver


def get_url():
    url = 'https://www.aliexpress.com'
    # 配置option
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument('--no-sandbox')
    # option.add_argument('--disable-gpu')
    option.add_argument('--log-level=3')
    # 不显示图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    option.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=option)
    # driver.implicitly_wait(4)  # 最长加载时间
    driver.get(url)

    driver.find_element_by_xpath('//input[@name="SearchText"]').send_keys("iphone7")
    driver.find_element_by_xpath('//input[@class="search-button"]').submit()

    # 阿里反爬,跳转登录的处理
    # if 'login' in driver.current_url:
    #     time.sleep(2)
    #     driver.switch_to.frame('alibaba-login-box')
    #     driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys("1024407342@qq.com")
    #     driver.find_element_by_xpath('//input[@type="password"]').send_keys('123789')
    #     driver.find_element_by_xpath('//button[@class="fm-button fm-submit password-login"]').click()
    #     time.sleep(3)

    # url = 'https://www.aliexpress.com/wholesale?SearchText=iphone5'

    # driver.get(url)

    infos = {}
    index = 1
    _max = 480
    while len(infos) < _max:
        # time.sleep(3)

        # 弹窗处理
        if '<span class="ui-pagination-active">1</span>' in driver.page_source:
            try:
                element = driver.find_element_by_xpath('//a[@class="close-layer"]')
                driver.execute_script("arguments[0].click();", element)  # 关闭href为js的a标签
            except selenium.common.exceptions.NoSuchElementException:
                return {}

        temp_list = driver.find_elements_by_xpath('//a[@class="item-title"]')

        if not temp_list:
            temp_list = driver.find_elements_by_xpath('//a[@class="history-item product "]')

        for item in temp_list:
            infos[str(index)] = item.get_attribute("href")
            index += 1

        driver.find_element_by_xpath('//a[@class="page-next ui-pagination-next"]').click()

    infos = {k: infos[k] for k in list(infos.keys())[:_max]}

    driver.quit()

    return infos


def url_parser(keyword):
    import scrapy
    import requests
    start_url = 'https://www.aliexpress.com/wholesale'
    data = {'SearchText': '%s' % keyword, 'page': '1', 'ie': 'utf8', 'g': 'y'}

    res = requests.get(start_url, params=data)

    resp = scrapy.Selector(response=res)

    infos = []
    index = 1
    _max = 480
    page = 1
    while len(infos) < _max:
        url_list = resp.xpath('//a[@class="history-item product "]/@href').extract()

        for url in url_list:
            # infos[str(index)] = url
            infos.append({'id': str(index), 'url': url})
            index += 1

        # 下一页
        page += 1
        data['page'] = page
        res = requests.get(start_url, params=data)
        resp = scrapy.Selector(response=res)

    # infos = {k: infos[k] for k in list(infos.keys())[:_max]}
    infos = infos[:_max]

    return infos


if __name__ == "__main__":
    print(get_url())
