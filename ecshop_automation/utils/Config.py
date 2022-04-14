# -*- coding: utf-8 -*-
import configparser

from ecshop_automation.utils.Logger import Logger

logger = Logger('Config').getlog()


class Config(object):

    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.file = file

    def read(self, file, encoding='utf-8'):
        """抽取公共的读"""
        self.config.read(file, encoding)

    def write(self, file):
        """抽取公共的写"""
        with open(file, 'w') as configfile:
            self.config.write(configfile)

    def create_section(self, file, section):
        """创建标签"""
        self.read(file)
        try:
            self.config.add_section(section)
        except Exception:
            logger.info('对不起，你的' + section + '已存在')
        else:
            self.write(file)
            logger.info('恭喜你，成功创建：' + section)

    def rename_section(self, file, section):
        """移除标签"""
        self.read(file)
        if not section in self.config.sections():
            self.config.add_section(section)
            self.write(file)
            logger.info('恭喜你，成功修改：' + section)
        else:
            logger.info('对不起，你的' + section + '已存在')

    def delete_section(self, file, section):
        """删除标签"""
        self.read(file)
        self.config.remove_section(section)
        self.write(file)
        logger.info('恭喜你，成功删除：' + section)

    def getall_section(self, file):
        """获得所有的标签"""
        self.read(file)
        sections = self.config.sections()
        logger.info('所有的section为：' + str(sections))
        return sections

    def create_value(self, file, section, option, value):
        """创建标签旗下的属性和值"""
        self.read(file)
        if self.config.has_section(section):
            self.config.set(section, option, value)
            self.write(file)
            logger.info('恭喜你，成功创建：' + section + '下的屬性' + option + '中的' + value)
        else:
            logger.info('对不起，你的' + section + '不存在')

    def rename_value(self, file, section, option, value):
        """修改标签旗下的属性和值"""
        self.read(file)
        if self.config.has_section(section):
            if self.config.has_option(section, option):
                self.config.set(section, option, value)
                self.write(file)
                logger.info('恭喜你，成功修改：' + section + '下的屬性' + option + '中的' + value)
            else:
                logger.info('对不起，你的' + section + '中的' + option + '不存在')
        else:
            logger.info('对不起，你的' + section + '不存在')

    def get_value(self, file, section, option):
        """获取指定标签下的属性值"""
        self.read(file)
        if self.config.has_section(section):
            if self.config.has_option(section, option):
                value = self.config.get(section, option)
                logger.info('你的value值为：' + value)
                return value
            else:
                logger.info('对不起，你的' + section + '中的' + option + '不存在')
        else:
            logger.info('对不起，你的' + section + '不存在')

    def getall_option(self, file, section):
        """获取指定标签下的属性列表"""
        self.read(file)
        try:
            sections = self.config.options(section)
        except Exception:
            logger.info('对不起，你的' + section + '不存在')
        else:
            logger.info('你的value值为：' + str(sections))
            return sections

    def delete_option(self, file, section, option):
        """删除指定标签下的属性和值"""
        self.read(file)
        try:
            self.config.remove_option(section, option)
            self.write(file)
            logger.info('恭喜你，成功删除：' + option + '属性和对应值')
        except Exception:
            logger.info('对不起，你的' + section + '不存在')
