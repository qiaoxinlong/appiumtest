# coding=utf-8

from util.operate_excel import operaExcel


class GetData:
    def __init__(self):
        self.opera_excel = operaExcel()

    def get_case_lines(self):
        '''
        获取case的行数
        '''
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self, row):
        '''
        获取操作步骤里面的操作方法名字
        '''
        method_name = self.opera_excel.get_cell(row, 3)
        return method_name

    def get_element_key(self, row):
        '''
        获取操作元素的key
        '''
        element_key = self.opera_excel.get_cell(row, 4)
        if element_key == '':
            return None
        return element_key

    def get_handle_value(self, row):
        '''
        获取操作元素的值
        '''
        handle_value = self.opera_excel.get_cell(row, 5)
        if handle_value == '':
            return None
        return handle_value

    def get_expect_element(self, row):
        '''
        获取预期结果元素element
        '''
        expect_element = self.opera_excel.get_cell(row, 6)
        if expect_element == '':
            return None
        return expect_element

    def get_is_run(self, row):
        is_run = self.opera_excel.get_cell(row, 8)
        if is_run == 'yes':
            return True
        else:
            return False

    def get_expect_handle(self, row):
        expect_step = self.opera_excel.get_cell(row, 7)
        if expect_step == "":
            return None
        return expect_step

