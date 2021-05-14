# coding=utf-8
import time
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
class ActionMethod:
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)
        self.driver.find_element_by_id('cn.com.open.mooc:id/iv_cancel').click()
        print('取消广告')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("账号")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("账号密码登录")').click()
        print('点击登录')
    def input(self, *args):
        '''
        输入值
        '''
        # key,value
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.send_keys(args[1])
    def on_click(self, *args):
        '''
        元素点击
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.click()
    def sleep_time(self, *args):
        time.sleep(int(args[0]))
    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self, *args):
        #[100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10*2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self, *args):
        #[100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def get_element(self, *args):
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element


