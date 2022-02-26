#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/3
# @File Name: __init__.py.py

import sys

sys.stdout.write('\033[0;34mMySQL数据库支持在./bin/tests/MySQLSET/MySQL.py\n\033[0m'
                 '\033[0;34m由原本pymysql库更换为了SQLAlchemy库, 已经将增删查改四个功能写好\n\033[0m'
                 '\033[0;34m由于一些原因无法使用\033[0m'
                 '\033[0;34m数据库导入文件请前往 https://themedatabase.vercel.app/source/sql 下载\n\033[0m'
                 '\033[0;34msql文件来源: 使用SQLiteStudio直接导出为.sql文件\n\033[0m'
                 '\033[0;34m使用 source db.sql 导入数据库时出现了一些错误:\n\033[0m'
                 '\033[0;34m有几个base64编码的值无法插入到表内\n\033[0m'
                 '\033[0;34m如果你有能力贡献代码请毫不犹豫地提交 pull request 吧!\n\n\033[0m')
sys.stdout.write('\033[1;31m----------以下为报错信息----------\033[0m')
sys.stdout.write(
    r"""
    Traceback (most recent call last):
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\mysql\connector\connection_cext.py", line 523, in cmd_query
        self._cmysql.query(query,
    _mysql_connector.MySQLInterfaceError: Table 'data.reqcount' doesn't exist

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 1802, in _execute_context
        self.dialect.do_execute(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
        cursor.execute(statement, parameters)
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\mysql\connector\cursor_cext.py", line 269, in execute
        result = self._cnx.cmd_query(stmt, raw=self._raw,
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\mysql\connector\connection_cext.py", line 528, in cmd_query
        raise errors.get_mysql_exception(exc.errno, msg=exc.msg,
    mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'data.reqcount' doesn't exist

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "C:\Users\Tapso\PycharmProjects\RequestCounter\bin\tests\MySQL.py", line 133, in <module>
        print(mysql.fetch('AAA'))
      File "C:\Users\Tapso\PycharmProjects\RequestCounter\bin\tests\MySQL.py", line 102, in fetch
        data = self.session.query(ReqCount).filter(ReqCount.name == name).all()
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\orm\query.py", line 2759, in all
        return self._iter().all()
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\orm\query.py", line 2894, in _iter
        result = self.session.execute(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\orm\session.py", line 1692, in execute
        result = conn._execute_20(statement, params or {}, execution_options)
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 1614, in _execute_20
        return meth(self, args_10style, kwargs_10style, execution_options)
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\sql\elements.py", line 325, in _execute_on_connection
        return connection._execute_clauseelement(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 1481, in _execute_clauseelement
        ret = self._execute_context(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 1845, in _execute_context
        self._handle_dbapi_exception(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 2026, in _handle_dbapi_exception
        util.raise_(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\util\compat.py", line 207, in raise_
        raise exception
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\base.py", line 1802, in _execute_context
        self.dialect.do_execute(
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
        cursor.execute(statement, parameters)
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\mysql\connector\cursor_cext.py", line 269, in execute
        result = self._cnx.cmd_query(stmt, raw=self._raw,
      File "C:\Users\Tapso\AppData\Local\Programs\Python\Python310\lib\site-packages\mysql\connector\connection_cext.py", line 528, in cmd_query
        raise errors.get_mysql_exception(exc.errno, msg=exc.msg,
    sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1146 (42S02): Table 'data.reqcount' doesn't exist
    [SQL: SELECT reqcount.name AS reqcount_name, reqcount.times AS reqcount_times
    FROM reqcount
    WHERE reqcount.name = %(name_1)s]
    [parameters: {'name_1': 'AAA'}]
    (Background on this error at: https://sqlalche.me/e/14/f405)"""
)

input()