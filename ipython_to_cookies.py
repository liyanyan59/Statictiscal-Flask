# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 14:55
# @Author  : LY
# @FileName: ipython_to_cookies
# @Software: PyCharm
# @Official Accounts：大数据学习废话集

from selenium import webdriver
from cookie import exist_cookies

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
driver.get(url)

# 阿里反爬,登录的处理
driver.switch_to.frame('alibaba-login-box')
driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys("1024407342@qq.com")
driver.find_element_by_xpath('//input[@type="password"]').send_keys('123789')
driver.find_element_by_xpath('//button[@class="fm-button fm-submit password-login"]').click()
cookies = exist_cookies
driver.set_page_load_timeout(15)
try:
    cookies = driver.get_cookies()
except:
    cookies = driver.get_cookies()


driver.quit()
