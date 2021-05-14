# coding=utf-8
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal


class LoginPage:
    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def clickRelease(self):
        # 点击发布按钮
        return self.get_by_local.get_element('Release').click()

    def sendReleaseContent(self, content):
        # 找到发布内容框
        return self.get_by_local.get_element('Content').send_keys(content)

    def findCommunity(self):
        # 找到社群菜单
        return self.get_by_local.get_element('CommunityPage').click()

    def clickCommunity(self):
        # 点击社群
        return self.get_by_local.get_element('Community').click()
# 	'''
# 	获取tostelement
# 	'''
# 	time.sleep(2)
# 	tost_element = ("xpath","//*[contains(@text,"+message+")]")
# 	return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))
