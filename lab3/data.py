import json
from interface import Node
from sort import merge_sort
import yaml


class Data:
    """Reads file data by path name"""
    data: list[Node]

    def __init__(self, path) -> None:
        """Contstructor: writes data to instance"""
        self.data = json.load(open(path, encoding='windows-1251'))

    def getData(self) -> list[Node]:
        """Returns all nodes"""
        return self.data

    def getSortedData(self) -> list[Node]:
        return merge_sort(self.data)

    def writeYamlData(self, data: list[Node], path) -> None:
        with open(path, 'w') as f:
            yaml.dump(data, f)
            print('Yaml sorted data has written')

    def readYamlData(self, path):
        with open(path, 'r') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

    def writeSortedData(self, path):
        sorted = merge_sort(self.data)
        f = open(path, 'w')
        for i in sorted:
            f.write(str(i) + "\n")
