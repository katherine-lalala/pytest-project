#获取短信验证码
from utils.log_util import logger
from utils.mysql_util import db


def get_code(mobile):
    sql = ("select code from users_verifycode where mobile = '%s' order by id desc limit 1" % mobile)
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果:{result}')
    return result['code']


def user_id(mobile):
    sql = "select id from users_userprofile where mobile = '%s'" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')
    return result['id']


def get_shop_cart_num(username, good_id):
    user_id(username)

