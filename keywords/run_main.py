# coding=utf-8
import time

from keywords.get_data import GetData
from keywords.action_method import ActionMethod
from util.server import Server
class RunMain:
    def run_method(self):
        # 启动appium服务
        server = Server()
        server.main()
        # 生成Server
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        time.sleep(5)
        for i in range(1, lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_handle_value(i)
            expect_key = data.get_expect_element(i)
            expect_step = data.get_expect_handle(i)
            excute_method = getattr(action_method, handle_step)
            if element_key != None:
                excute_method(element_key, handle_value)
            else:
                excute_method(handle_value)
            if expect_step != None:
                expect_result = getattr(action_method, expect_step)
                expect_result(expect_key)
if __name__ == '__main__':
    run = RunMain()
    run.run_method()
