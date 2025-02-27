import yaml

with open('hp_test.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)