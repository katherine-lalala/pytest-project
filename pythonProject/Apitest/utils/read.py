import yaml
import configparser
import os
# dirname是获取当前目录的上一层目录
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'settings.ini')
class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
    def read_data(self):
        f = open(data_path, encoding="utf-8")
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(ini_path, encoding='utf-8')
        return config


base_data = FileRead()  #实例化一个class类，base_data去接收

