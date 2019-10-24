from appium import webdriver
import page

class GetDriver:
    driver = None
    package=page.app_package
    activity=page.app_activity
    @classmethod
    def get_driver(cls):
        if GetDriver.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = GetDriver.package
            desired_caps['appActivity'] = GetDriver.activity

            # 声明⼿机驱动对象
            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if GetDriver.driver:
            GetDriver.driver.quit()
            GetDriver.driver = None
