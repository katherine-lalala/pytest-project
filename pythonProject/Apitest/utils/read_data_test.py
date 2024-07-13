import yaml
f = open('../config/data.yaml', encoding="utf-8")
data = yaml.safe_load(f)
print(data)
print(data['heroes_name'])