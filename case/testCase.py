import unittest

class Test_Math(unittest.TestCase):

    #每执行一个用例，都会执行setup()和teardown()方法
    #如果跑所有用例，只运行一次前提条件和结束条件。则用setupclass()和teardownclass()
    def setUp(self):
        print("测试用例执行前的初始化操作========")

    def tearDown(self):
        print("测试用例执行完之后的收尾操作=====")


    def test_addTwoNum_01(self):
        print(5+7)

    def test_subTwoNum_02(self):
        print(3-2)