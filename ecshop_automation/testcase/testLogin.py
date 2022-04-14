"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/8/4 9:52
@desciption: 业务实现(百度搜索功能)
"""
import unittest
from time import sleep

from selenium import webdriver

from ecshop_automation.po.LoginPage import LoginPage
from ecshop_automation.utils.Config import Config
from ecshop_automation.utils.Logger import Logger

logger = Logger('TestLogin').getlog()


class TestLogin(unittest.TestCase):
    file = './conf/config.ini'
    config = Config(file)

    def setUp(self):
        if self.config.get_value(self.file, 'base', 'browser') == 'Chrome':
            self.driver = webdriver.Chrome(self.config.get_value(self.file, 'base', 'driver'))
        elif self.config.get_value(self.file, 'base', 'browser') == 'Firefox':
            self.driver = webdriver.Firefox(self.config.get_value(self.file, 'base', 'driver'))
        else:
            pass

    # 一个一个的测试用例
    def testLogin(self):
        login = LoginPage(self.driver)
        logger.info('你实例化了searchpage类')

        login.open_url()
        login.input_username('caichang')
        login.input_pwd('caichang1')
        login.login_button()
        sleep(1)

    def tearDown(self):
        self.driver.close()
