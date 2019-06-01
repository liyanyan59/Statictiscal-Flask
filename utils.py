# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 19:50
# @Author  : LY
# @FileName: test
# @Software: PyCharm
# @Official Accounts：大数据学习废话集

import requests
import time
from selenium import webdriver
from lxml import etree

from cookie import exist_cookies


def get_cookie():
    url = 'https://login.aliexpress.com'
    # 配置option
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--log-level=3')
    # 不显示图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    option.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=option)


    # driver.get(url)
    # print('你是真tm有毒啊啊啊啊')
    # time.sleep(3)
    # driver.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')

    driver.get(url)
    # print('你是真tm有毒')

    # driver.find_element_by_xpath('//input[@name="SearchText"]').send_keys("iphone7")
    # driver.find_element_by_xpath('//input[@class="search-button"]').submit()

    # 阿里反爬,登录的处理
    driver.switch_to.frame('alibaba-login-box')
    driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys("1024407342@qq.com")
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('123789')
    driver.find_element_by_xpath('//button[@class="fm-button fm-submit password-login"]').click()
    cookies = exist_cookies
    # print('你有毒吧')
    driver.set_page_load_timeout(15)
    try:
        cookies = driver.get_cookies()
        # print("qiuguo")
    except:
        cookies = driver.get_cookies()
        # print("不要伤害我了!!!")

    # url = 'https://www.aliexpress.com/wholesale?SearchText=iphone5'

    # driver.get(url)

    # 弹窗处理
    # if '<span class="ui-pagination-active">1</span>' in driver.page_source:
    #     try:
    #         element = driver.find_element_by_xpath('//a[@class="close-layer"]')
    #         driver.execute_script("arguments[0].click();", element)  # 关闭href为js的a标签
    #     except selenium.common.exceptions.NoSuchElementException:
    #         return {}

    driver.quit()

    return cookies


def url_parser(keyword):
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
               }
    session.headers.update(headers)

    # 反爬登录
    # print('这登录是什么鬼  fhjdhfkjnkjjfkjk#$%TY*&')
    cookies = get_cookie()
    print(cookies)
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    start_url = 'https://www.aliexpress.com/wholesale'
    data = {'SearchText': '%s' % keyword, 'page': '1', 'ie': 'utf8', 'g': 'y'}

    # print('keyword:  %s' % keyword)

    res = session.get(start_url, params=data)

    # resp = scrapy.Selector(response=res)
    html = etree.HTML(res.content)

    infos = []
    index = 1
    _max = 480
    page = 1
    while index <= _max:
        time.sleep(5)
        url_list = html.xpath('//a[@class="history-item product "]/@href')

        print(url_list)
        for url in url_list:
            # infos[str(index)] = url
            infos.append({'id': str(index), 'url': url})
            index += 1

        # 下一页
        page += 1
        data['page'] = str(page)
        res = session.get(start_url, params=data)
        # resp = scrapy.Selector(response=res)
        html = etree.HTML(res.content)
        print('没有出错辽咩  %s' % page)

    # infos = {k: infos[k] for k in list(infos.keys())[:_max]}
    infos = infos[:_max]

    return infos


if __name__ == "__main__":
    print(url_parser('cup;sugar'))
