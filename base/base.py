from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_driver import GetDriver


class Base:
    # 初始化
    def __init__(self):
        self.driver=GetDriver.get_driver()

    # 定位元素
    def base_find_element(self, method, timeout=10, pro=0.4):
        return WebDriverWait(self.driver, timeout, pro).until(lambda x: x.find_element(*method))

    # 输入
    def base_input_element(self, method, values):
        data = self.base_find_element(method)
        data.clear()
        data.send_keys(values)

    # 点击
    def base_click_element(self, method):
        self.base_find_element(method).click()
