"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/8/4 9:43
@desciption: 登录页的元素定义
"""
from ecshop_automation.base.Base import Base
from ecshop_automation.utils.Logger import Logger

logger = Logger('GoodListPage').getlog()


class GoodListPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def into_menu_frame(self):
        self.into_frame('menu-frame')

    def click_good_list_link(self):
        self.click('link_text=>商品列表')

    def default_frame(self):
        self.into_default_content()

    def into_main_frame(self):
        self.into_frame('main-frame')

    def input_keyword(self):
        self.input('name=>keyword','车')

    def click_search_button(self):
        self.click("xpath=>//input[@value=' 搜索 ']")

    def get_total(self):
        text = self.get_text("xpath=>//*[@id='totalRecords']")
        logger.info(f'我获得的文本内容是{text}')
        return text

    def click_add(self):
        self.click("xpath=>/html/body/h1/span[1]/a")

    def input_goods_name(self):
        # 商品名称输入框
        self.input('name=>goods_name','包包爱吃包子')


    def select_cate_goods(self):
        # 商品分类下拉框
        self.select_by_value('name=>cat_id','数码时尚')

    def add_click(self):
        self.click("xpath=>//input[@value=' 确定 ']")

    # 点击上架中的勾
    def click_disable(self):
        self.click("xpath=>//*[@id='listDiv']/table[1]/tbody/tr[3]/td[5]/img")
