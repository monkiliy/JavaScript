"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/8/4 9:43
@desciption: 登录页的元素定义
"""
from ecshop_automation.base.Base import Base
from ecshop_automation.utils.Logger import Logger

logger = Logger('LoginPage').getlog()
class LoginPage(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    # 打开网页
    def open_url(self):
        logger.info(f'打开的地址是:{self.base_url}')
        self.driver.get(self.base_url)
        logger.info('最大化浏览器')
        self.driver.maximize_window()

    def input_username(self,text):
        logger.info(f'我往输入框中输入了:{text}')
        self.input('name=>username',text)

    def input_pwd(self,text):
        logger.info(f'我往输入框中输入了:{text}')
        self.input('name=>password',text)

    def login_button(self):
        logger.info('点击了登录按钮')
        self.click('class_name=>btn-a')