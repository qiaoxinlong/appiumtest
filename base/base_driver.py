# coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self, i):
        # devices_name adb devices
        # port
        write_file = WriteUserCommand()
        # devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        devices = '127.0.0.1:21503'

        # port = write_file.get_value('user_info_' + str(i), 'port')
        port = '4723'
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "appActivity": "com.ofbank.lord.activity.MainActivity",
            "appPackage":"com.ofbank.lord",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        # time.sleep(10)
        return driver
