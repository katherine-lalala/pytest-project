import os
import yaml


class YamlUtils:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')

    def read_testcases_yaml(self, yaml_name):
        with open(self.data_path + yaml_name, mode='r', encoding="utf-8") as f:
            value = yaml.safe_load(f)
            return value


if __name__ == '__main__':
    data = YamlUtils().read_testcases_yaml('user_center.yaml')
    print(data)
