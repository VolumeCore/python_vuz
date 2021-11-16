from data import Data

data = Data('valid.txt')
data.writeYamlData(data.getSortedData(), 'yaml.yaml')
print(data.readYamlData('yaml.yaml'))
