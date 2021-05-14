# coding=utf-8
from page.community_page import LoginPage

class LoginHandle:
    def __init__(self, i):
        self.login_page = LoginPage(i)

    # 操作登录页面的元素
    def getReleaseButton(self):
        # 点击发布按钮
        self.login_page.clickRelease()

    def sentReleaseContent(self, content):
        # 输入帖子内容
        self.login_page.sendReleaseContent(content)

    def clickCommunityPage(self):
        # 点击社群菜单
        self.login_page.findCommunity()

    def clickCommunity(self):
        # 点击社群
        self.login_page.clickCommunity()
# def get_fail_tost(self,message):
# 	'''
# 	获取tost，根据返回信息进行反数据
# 	'''
# 	tost_element = self.login_page.get_tost_element(message)
# 	if tost_element:
# 		return True
# 	else:
# 		return False
