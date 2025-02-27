import yaml

with open('hp_test.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)

# writing to a YAML file
data1 = {
    'name': 'test',
    'age': 20,
    'city': 'Ghent',
    'skills': ['Python', 'Data Analysis', 'Machine Learning']
}

data.update(data1)

with open('hp_test.yaml', 'w') as f:
    yaml.dump(data, f)

print("Data has been written to yaml file")