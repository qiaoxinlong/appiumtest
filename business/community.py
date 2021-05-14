# coding=utf-8
import time

from handle.community_handle import LoginHandle
class LoginBusiness:
    def __init__(self, i):
        self.login_handle = LoginHandle(i)
    def sentCommunity(self):
         # 点击社群菜单
        self.login_handle.clickCommunityPage()
        # # 进入社群
        self.login_handle.clickCommunity()
        # 点击发布
        self.login_handle.getReleaseButton()
        # 输入帖子内容
        time.sleep(3)
        self.login_handle.sentReleaseContent('"hello,world"')
        # 点击发布
        self.login_handle.getReleaseButton()
if __name__ == '__main__':
    loginBase = LoginBusiness(1)
    loginBase.sentCommunity()
