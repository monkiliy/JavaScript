"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/8/4 9:52
@desciption: 业务实现(百度搜索功能)
"""
import unittest
from time import sleep

from selenium import webdriver

from ecshop_automation.dao.MySQLHelper import MySQLHelper
from ecshop_automation.po.GoodListPage import GoodListPage
from ecshop_automation.po.LoginPage import LoginPage
from ecshop_automation.utils.Config import Config
from ecshop_automation.utils.Logger import Logger

logger = Logger('TestGoodList').getlog()


class TestGoodList(unittest.TestCase):
    file = './conf/config.ini'
    config = Config(file)

    def login(self):
        login = LoginPage(self.driver)
        logger.info('你实例化了searchpage类')

        login.open_url()
        login.input_username('caichang')
        login.input_pwd('caichang1')
        login.login_button()
        sleep(1)


    def setUp(self):
        self.driver = webdriver.Chrome(self.config.get_value(self.file, 'base', 'driver'))


    # 一个一个的测试用例
    @unittest.skip
    def testSearch(self):
        self.login()

        glp = GoodListPage(self.driver)
        glp.into_menu_frame()
        glp.click_good_list_link()
        glp.default_frame()
        glp.into_main_frame()

        glp.input_keyword()
        glp.click_search_button()
        sleep(3)

        total = glp.get_total()

        help = MySQLHelper()
        sql = 'select goods_name from ecs_goods where goods_name like "%车%"'
        result = help.find(sql, 'all')

        self.assertEqual(len(result), int(total))

    @unittest.skip
    def testaddgoods(self):
        # 添加商品
        self.login()

        glp = GoodListPage(self.driver)
        glp.into_menu_frame()
        glp.click_good_list_link()
        glp.default_frame()
        glp.into_main_frame()

        glp.click_add()
        glp.input_goods_name()
        glp.select_cate_goods()

        glp.add_click()
        sleep(1)

        help = MySQLHelper()
        sql = "select count(*) from ecs_goods where goods_name = '包包爱吃包子'"
        result = help.find(sql, 'one')

        self.assertEqual(result[0], 1)



    def testisonsal_disable(self):
        self.login()
        help = MySQLHelper()

        update_status = "update ecs_goods set is_on_sale=1 where goods_name = '包包爱吃包子'"
        help.dml(update_status)

        glp = GoodListPage(self.driver)
        glp.into_menu_frame()
        glp.click_good_list_link()
        glp.default_frame()
        glp.into_main_frame()
        glp.click_disable()


        change_status = "select is_on_sale from ecs_goods where goods_name = '包包爱吃包子'"
        result = help.find(change_status, 'one')

        self.assertEqual(result[0], 0)

    def tearDown(self):
        self.driver.close()
