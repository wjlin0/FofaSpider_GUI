#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   :wjlin0
# @Blog     :https://wjlin0.com
# @Email    :wjlgeren@163.com
# @Time     :2022-07-14 9:57
# @File     :db
import sqlite3
import threading
import loguru


class SQL:
    instance = None
    lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance

    def __init__(self, db_name=None):
        self.conn = sqlite3.connect(db_name if db_name else 'spider.sqlite3', check_same_thread=False)
        self.cursor = self.conn.cursor()
        loguru.logger.success("初始化打开数据库成功")

    def update_field(self, table_name: str, field_dict: dict, ID=-1, name=None, str_=None, ):
        try:
            fields = ""
            fieldD = {

            }
            for key, value in field_dict.items():
                fields += f"{key}=:{key},"
                fieldD[f'{key}'] = value
            # fields = ",".join([key + " = " + '"' + str(value) + '"' for key, value in field_dict.items()])
            fields = fields.rstrip(",").lstrip(",")
            if ID == -1:
                # sql = f"UPDATE {table_name} SET {fields} WHERE {name}={str_};"
                sql = "UPDATE " + table_name + " SET " + fields + " WHERE " + name + "=:str_;"
                fieldD['str_'] = str_
                print(sql)
                self.cursor.execute(sql, fieldD)
            else:
                # sql = f"UPDATE {table_name} SET {fields} WHERE ID={ID};"

                sql = "UPDATE " + table_name + " set " + fields + " WHERE ID=:id;"
                fieldD['id'] = ID
                print(sql)
                self.cursor.execute(sql, fieldD)
            # self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            loguru.logger.error("更新数据错误：" + table_name)
            loguru.logger.error(e)
            return False

    def drop_tables(self, table_name: str) -> bool:
        try:
            sql = f"DROP  TABLE {table_name};"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            loguru.logger.error("删除表失败：" + table_name)
            loguru.logger.error(e)
            return False

    def delete_tables(self, table_name: str) -> bool:
        try:
            sql = f"DELETE FROM {table_name}"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            loguru.logger.info("删除数据失败：", e)
            return False

    '''
    创建表格
    @:param table_name 表名
    @:param field_list 字段列表,例如：["name","age","gender"]
    @:return 
    '''

    def create_tables(self, table_name: str, field_list: list) -> bool:
        try:
            fields = ",".join([field for field in field_list])
            sql = f"CREATE TABLE {table_name} ({fields});"
            self.cursor.execute(sql)
            self.conn.commit()
            loguru.logger.success(f"创建数据表 {table_name}成功")
            return True
        except Exception as ex:
            loguru.logger.error("创建表出错，错误信息：", str(ex))
            return False

    '''
    插入数据，根据传入的数据类型进行判断，自动选者插入方式
    @:param table_name 表名
    @:param data 要插入的数据
    '''

    def insert_data(self, table_name: str, data) -> bool:
        try:
            if isinstance(data, list):
                for item in data:
                    keys = ",".join(list(item.keys()))
                    v = []
                    for x in list(item.values()):
                        x = str(x).strip(",")
                        if x == "":
                            continue
                        v.append(x)
                    values = ",".join(v)
                    sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values});"
                    self.cursor.execute(sql)
            elif isinstance(data, dict):
                keys = ",".join(list(data.keys()))
                # values = ",".join([f"'{x}'" for x in list(data.values())])
                values = ""
                for x in list(data.keys()):
                    values += f"?,"
                values = values.rstrip(',')
                sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values});"
                temp = tuple(list(data.values()))
                # print(sql, temp)
                self.cursor.execute(sql, temp)
            # self.conn.commit()
            # print(data)
            return True
        except Exception as ex:
            loguru.logger.info(ex)
            return False
        finally:
            self.conn.commit()

    '''
    查询数据
    @:param 要查询的sql语句
    '''

    def queryDataAll(self, sql, fields=None) -> list:
        if fields is None:
            fields = {}
        try:
            self.cursor.execute(sql, fields)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            loguru.logger.info(e)
            return []

    def queryData(self, sql, fields=None) -> list:
        if fields is None:
            fields = {}
        try:
            self.cursor.execute(sql, fields)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            loguru.logger.info(e)
            return []

    def query_data_all(self, sql: str) -> list:
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as ex:
            loguru.logger.info(ex)
            return []

    def query_data(self, sql: str) -> list:
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as ex:
            loguru.logger.info(ex)
            return []

    '''
    关闭数据库连接
    '''

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as ex:
            raise Exception("关闭数据库连接失败")
