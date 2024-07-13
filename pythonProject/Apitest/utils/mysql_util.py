import pymysql
from utils.read import base_data
from utils.log_util import logger

data = base_data.read_ini()['mysql']
print(data)
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "passwd": data['MYSQL_PASSWD'],
    'db': data['MYSQL_DB']
}


class MysqlDb:
    def __init__(self):
        # mysql链接，固定写法，不重要
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    #释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    #查询一条数据
    def select_db_one(self, sql):
        logger.info(f'执行sql: {sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    #查询多条数据
    def select_db_all(self, sql):
        logger.info(f'执行sql: {sql}')
        self.cur.execute(sql)
        # 获取数据
        result= self.cur.fetchall()
        logger.info(f'执行结果：{result}')
        return result

    def execute_db(self, sql):
        try:
            logger.info(f'执行sql: {sql}')
            self.cur.execute(sql)
            self.conn.commit()  #提交
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()
if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_one(
        "select code from user_verify code where mobile = '1500000011' order by id desc limit one")
    print(result)