"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/14 16:29
@desciption: 把函数封装成自己的类(二次开发)
"""

from xlwt import Workbook, XFStyle, Font, Borders, Alignment, Pattern
from xlrd import open_workbook
from xlutils.copy import copy

"""
    自己封装的Excel类
    1.先封装了xlrd库,后期加入xlwt和xlutils等库的封装
    2.write_workbook方法是xlwt的封装
    3.copy_write是xlutils的封装
    4.上班后,如果你要修改我的类,可直接修改并测试
      一般你只需要动样式即可,逻辑上如无特殊需求一般不会动
"""


class ExcelHelper():
    def __init__(self):
        self.bk = ''  # 指定要打开的工作簿位置,如: r'd:\mendao,xls'
        self.sheet = ''  # 指定要读取的Sheet名,如:'员工表'
        self.save_path = ''
        self.sheet_index = 0

    def __get_sheet(self):
        """返回sheet类的对象,私有,仅仅提供给其他方法用,用的目的是拿到sheet对象"""
        bk = open_workbook(self.bk)  # bk是Book类的对象
        sheet = bk.sheet_by_name(self.sheet)  # sheet是Sheet类的对象
        return sheet

    def get_value_by_row(self, start_row, start_col, end_col=None):
        """读一行"""
        row_values = self.__get_sheet().row_values(start_row, start_col, end_col)
        return row_values

    def get_value_by_col(self, start_col, start_row, end_row=None):
        """读一列"""
        col_values = self.__get_sheet().col_values(start_col, start_row, end_row)
        return col_values

    def get_value_by_cell(self, row, col):
        """读一个单元格"""
        cell_value = self.__get_sheet().cell_value(row, col)
        return cell_value

    def get_all(self, start_row, end_row, start_col, end_col=None):
        """读指定行列的所有数据,读出来是个二维列表"""
        values = []
        for row in range(start_row, end_row):
            values.append(self.__get_sheet().row_values(row, start_col, end_col))
        return values

    def write_workbook(self, title, start_row, start_col, content):
        """
            创建一个新的excel并写入内容
            title:标题,传一个一维列表
            start_row:从哪行开始插入
            start_col:从哪列开始插入
            调用时,一定要声明sheet和save_path,否则会失败
        """
        wb = Workbook('utf-8')  # wb是Workbook的对象
        sheet = wb.add_sheet(self.sheet)  # sheet是Worksheet的对象

        font = Font()
        font.bold = True
        font.colour_index = 33

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        alignment = Alignment()
        alignment.horz = alignment.HORZ_CENTER

        # 颜色对照表:https://blog.csdn.net/zkw_1998/article/details/103930052
        pattern = Pattern()
        pattern.pattern = pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 7

        # 样式请你根据具体的需求来修改即可,标题和内容可灵活变更
        style = XFStyle()
        style.font = font
        style.borders = borders
        style.alignment = alignment
        style.pattern = pattern

        for i in range(len(title)):
            sheet.write(start_row, i + start_col, title[i], style)  # 5-->第6行,i+4--->向右移动多少,+4,右移4

        content_style = XFStyle()
        content_style.borders = borders

        # j为行,k为列
        for j in range(len(content)):
            for k in range(len(content[j])):
                # 因为内容在标题下一行,因此start_row+1
                sheet.write(start_row + 1 + j, k + start_col, content[j][k], content_style)

        wb.save(self.save_path)

    def copy_write(self, start_row, start_col,value):
        """往一个已存在的excel中插入值"""
        wb = open_workbook(self.bk, formatting_info=True)
        new_wb = copy(wb)
        new_sheet = new_wb.get_sheet(self.sheet_index)

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        # 具体你要的样式自己定义,可以修改这部分代码来满足样式需求
        style = XFStyle()
        style.borders = borders


        sheet = wb.sheet_by_name(self.sheet)  # sheet是Sheet类的对象
        #print(sheet.nrows)
        # values为预期结果列,只是读出来,作为一个一维列表试用
        # values = []
        # for i in range(start_row, sheet.nrows):
        #     values.append(sheet.row_values(i, start_col, end_col))
        #print(values)


        for i in range(start_row, sheet.nrows):
            new_sheet.write(i, start_col, value, style)



        # for j in range(len(values)):
        #     # print(values[j])
        #     print(values[j][0])
        #     print(values[j][1])
        #     if values[j][0] == values[j][1]:
        #         new_sheet.write(j + start_row, end_col, '通过', style)
        #     else:
        #         new_sheet.write(j + start_row, end_col, '不通过', style)

        new_wb.save(self.save_path)


    # 完成写入到新excel中
    def copy_wirte_col(self,value):
        wb = open_workbook(self.bk, formatting_info=True)
        new_wb = copy(wb)
        new_sheet = new_wb.get_sheet(self.sheet_index)

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        # 具体你要的样式自己定义,可以修改这部分代码来满足样式需求
        style = XFStyle()
        style.borders = borders

        for i in range(6,11):
            new_sheet.write(i, 8, value[i-6], style)

        new_wb.save(self.save_path)

    def write_actual(self):
        wb = open_workbook(r'd:\mendao_bak.xls', formatting_info=True)
        new_wb = copy(wb)
        new_sheet = new_wb.get_sheet(0)

        data = self.get_all(6,11,7)
        print(data)

        borders = Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN

        # 具体你要的样式自己定义,可以修改这部分代码来满足样式需求
        style = XFStyle()
        style.borders = borders
        for j in range(len(data)):
            if data[j][0] == data[j][1]:
                new_sheet.write(j + 6, 9, '通过', style)
            else:
                new_sheet.write(j + 6, 9, '不通过', style)
        new_wb.save(r'd:\cc.xls')

# help = ExcelHelper()
# help.bk=r'd:\mendao.xls'
# help.sheet='员工表'
# rows  = help.get_value_by_row(9,4,7)
# print(rows)
# print(help.get_value_by_cell(8,8))
# print(help.get_all(9,12,5,8))


# title = ['部门编号', '部门名称', '部门位置']
# content = [[10, '测试部', '深圳'], [20, '开发部', '重庆'], [30, '运维部', '北京'], [40, '营销部', '纽约']]
# help = ExcelHelper()
# help.sheet='明星表'
# help.save_path=r'e:\caichang.xls'
# help.write_workbook(title,1,1,content)


# help = ExcelHelper()
# help.bk = r'd:\mendao.xls'
# help.sheet='员工表'
# help.save_path = r'd:\ccc.xls'
# help.copy_write(7,11,13)
