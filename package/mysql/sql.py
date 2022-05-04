import re

import pymysql
import logging as log


class SqlAction():
    def __init__(self):
        try:
            self.database = pymysql.connect(host='101.35.49.209',
                                            user='root',
                                            password='543049601',
                                            database='Generation')
            self.cursor = self.database.cursor()
            self.cursor.execute('SELECT VERSION()')
            log.info('Database Version:', self.cursor.fetchone())
            log.info('数据库连接成功')
        except Exception as e:
            log.error('数据库连接失败')
            raise e

    def check_table_exist(self, table) -> None:
        '''
        判断表是否存在
        :param table: str 表名
        '''
        sql = "show tables"
        self.cursor.execute(sql)
        tables = self.cursor.fetchall()
        # print(tables)
        tables_list = re.findall('(\'.*?\')', str(tables))
        # print(tables_list)
        tables_list = [re.sub("'", '', each) for each in tables_list]
        # print(tables_list)
        if table not in tables_list:
            log.error(f'{table}不存在')
            self.database.close()
            raise Exception

    def check_connection(self) -> None:
        '''
        确认连接未断开，否则重连
        '''
        self.database.ping()
        self.cursor = self.database.cursor()

    def insert_data_into_mysql(self, table, data, condition='') -> None:
        '''
        写入数据到数据库
        :param table: str 表名
        :param data: tuple 值
        :param condition: str 条件
        '''
        self.check_connection()
        self.check_table_exist(table)
        if condition == '':
            sql = f"""INSERT INTO {table}
         VALUES {data}"""
        else:
            sql = f"""INSERT INTO {table}
            VALUES {data} WHERE {condition}"""
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.database.commit()
            log.info('写入数据库成功')
        except:
            # 如果发生错误则回滚
            self.database.rollback()
            log.error('写入数据库出错，已回滚')
            self.database.close()
            raise Exception

    def get_data_from_mysql(self, table, data_name ='*', condition=''):
        '''
        从数据库读取信息
        :param table: str 表名
        :param data_name: str 需要获取的字段名
        :param condition: str 条件
        :return:
        '''
        self.check_connection()
        self.check_table_exist(table)
        if condition == '':
            sql = f"""SELECT {data_name} FROM {table}"""
        else:
            sql = f"""SELECT {data_name} FROM {table} WHERE {condition}"""
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if data_name.find(',') == -1 and data_name != '*':
            new_data = []
            for i in data:
                new_data.append((i[0]))
            data = tuple(new_data)
        return data

    def quit_database(self):
        self.database.close()
        log.info('已经关闭sql连接')

if __name__ == '__main__':
    test = SqlAction()
    test.insert_data_into_mysql('user_info',('lcc','112233','user'))
    test.get_data_from_mysql('user_info')
    test.quit_database()