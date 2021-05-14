# coding=utf-8'''
import time
import unittest
import util.HTMLTestRunner
listaa = "..\\case"
def createsuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


now = time.strftime("%Y-%m-%d", time.localtime())
filename = "D:\\Work\\AppiumTest\\report\\reportLog\\" + now + "_result.html"
with open(filename, 'wb') as f:
    runner = util.HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title=u'领主推荐自动化测试报告',
        description=u'用例执行情况：')
    runner.run(createsuite1())
f.close()