# coding=utf-8

import xlrd


# data = excel.sheets()[0]
# print(data.cell(3,4).value)
class operaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path == None:
            self.file_path = "D:\work\AppiumTest\case\case.xls"
        else:
            self.file_path = file_path
        if i == None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheet(i)

    def get_excel(self):
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheet(self, i):
        # 获取sheet
        table = self.excel.sheets()[i]
        return table

    def get_lines(self):
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        # 获取单元格内容
        data = self.data.cell(row, cell).value
        return data
