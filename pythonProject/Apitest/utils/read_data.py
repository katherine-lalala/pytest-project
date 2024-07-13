import yaml
import os
# dirname是获取当前目录的上一层目录
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', "data.yaml")
def read_data():
    f = open('../config/data.yaml', encoding="utf-8")
    data = yaml.safe_load(f)
    return data

get_data = read_data()


