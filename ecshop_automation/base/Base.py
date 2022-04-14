"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/8/4 9:35
@desciption: 2次封装Selenium,提供给po层调的,base属于最底层,抽象层
你还可以封装鼠标,键盘,下拉框的其他行为,内帧中的windows框,警告框,上传/下载
"""

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from automation.utils.Config import Config
from ecshop_automation.utils.Logger import Logger

logger = Logger('Base').getlog()


class Base():
    file = './conf/config.ini'
    config = Config(file)

    def __init__(self, driver):
        self.driver = driver
        self.base_url = self.config.get_value(self.file,'base','url')

    def __waitElemnet(self, selector_by, selector_value, secs=5):
        # secs:超时时间(5秒找不到就超时)
        try:
            # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
            if selector_by == "id":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.ID, selector_value)))
            elif selector_by == "name":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.NAME, selector_value)))
            elif selector_by == "link_text":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.LINK_TEXT, selector_value)))
            elif selector_by == "partial_link_text":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
            elif selector_by == "xpath":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.XPATH, selector_value)))
            elif selector_by == "class_name":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, selector_value)))
            elif selector_by == "css_selector":
                WebDriverWait(self.driver, secs, 1).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector_value)))
            else:
                logger.info("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")
                raise NoSuchElementException("语法错误，参考: 'id=>caichang 或 xpath=>//*[@id='caichang'].")

        except (TimeoutException, NoSuchElementException):
            logger.info('超时或找不到元素')
            print('超时或找不到元素')

    def find_element(self, selector):
        # 根据=>来切割字符串，submit_btn = "id=>caichang"

        element = ''

        if '=>' not in selector:
            logger.info('对不起，至少要包含=>符')
            raise Exception('对不起，至少要包含=>符')

        # 如果包含了=>字符传后开始切割
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 查找元素，超时抛异常
        self.__waitElemnet(selector_by, selector_value)

        # 实在写不下去所有了，自己扩展出所有，一般感觉有这些够了
        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            element = self.driver.find_element_by_css_selector(selector_value)
        return element

    def input(self, selector, text):
        # 输入框输入信息用
        self.find_element(selector).send_keys(text)

    def click(self, selector):
        logger.info(f'对着{selector}元素点击了一下')
        self.find_element(selector).click()

    def into_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    def into_default_content(self):
        self.driver.switch_to.default_content()

    def get_text(self,selector):
        text = self.find_element(selector).text
        return text

    def select_by_value(self,selector,text):
        # 下拉框根据文本来找
        Select(self.find_element(selector)).select_by_visible_text(text)