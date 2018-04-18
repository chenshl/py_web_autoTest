#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from BaseSe.Selenium2 import Pyse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *

class BaiduPage(Pyse):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    search_loc = (By.XPATH,'//*[@id="kw"]')#定位百度文本框
    click_btn = (By.XPATH,'//*[@id="su"]')#定位百度按钮

    #操作
    #通过集成覆盖（overriding）方法:如果子类和父类的方法名相同，优先用子类自己的方法
    #打开网页
    def open(self):
        #调用selenium2中的_open方法打开链接
        self._open(self.base_url,self.pagetitle)

    def input_baidu_text(self,text):
        # *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
        # 并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前:foo(1,2,3,4, a=1,b=2,c=3)
        self.find_element(*self.search_loc).send_keys(text)

    def click_baidu_btn(self):
        self.find_element(*self.click_btn).click()