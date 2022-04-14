"""
@author: caichang
@email: caichangfast@qq.com
@time: 2021/7/16 10:07
@desciption: 二次开发pymysql类
"""
from pymysql import connect

from ecshop_automation.utils.Config import Config
from ecshop_automation.utils.Logger import Logger

logger = Logger('MySQLHelper').getlog()
class MySQLHelper():
    file = './conf/config.ini'
    config = Config(file)

    def __init__(self):
        """默认链本机和3306端口和root超管用户"""
        self.host = self.config.get_value(self.file,'mysql','host')
        self.user = self.config.get_value(self.file,'mysql','user')
        self.password = self.config.get_value(self.file,'mysql','password')
        self.database = self.config.get_value(self.file,'mysql','database')
        self.port = int(self.config.get_value(self.file,'mysql','port'))

    def __get_conn(self):
        """返回connect的对象"""
        conn = connect(host=self.host, user=self.user, password=self.password, database=self.database,
                       port=self.port)  # conn是Connection类的对象
        return conn

    def __get_cursor(self):
        """返回游标"""
        cursor = self.__get_conn().cursor()  # cursor 是Cursor类的对象
        return cursor

    def find(self, sql, flag, number=None):
        """
            查数据均用这个方法
            sql:你需要查询的sql语句
            flag:查询方式,提供:one,many,all三种
            number:如果flag=many时候,传这个参数,代表你需要返回多少个值
        """
        cursor = self.__get_cursor()
        cursor.execute(sql)
        logger.info(f'你的sql为:{sql}')
        if flag == 'all':
            result = cursor.fetchall()
        elif flag == 'one':
            result = cursor.fetchone()
        elif flag == 'many':
            result = cursor.fetchmany(number)
        else:
            logger.info('对不起,请你只能填all,many,one中的其中一个')
            raise Exception('对不起,请你只能填all,many,one中的其中一个')
        logger.info(f'你返回的值是:{result}')
        return result

    def dml(self, sql):
        """sql写增删改语句即可"""
        cursor = self.__get_cursor()
        cursor.execute(sql)
        logger.info(f'你的sql为:{sql}')
        self.__get_conn().commit()

    def close(self):
        """关闭游标和链接"""
        self.__get_cursor().close()  # 关闭游标
        self.__get_conn().close()  # 关闭链接

# help = MySQLHelper()
# help.password = 'root'
# help.database = 'caichang'
#
# sql = 'select * from dept'
# print(help.find(sql, 'one'))
# print(help.dml('insert into dept values (50,"测试","sz")'))
