import json
from interface import Node
from sort import merge_sort


class Data:
    """Reads file data by path name"""
    data: list[Node]

    def __init__(self, path) -> None:
        """Contstructor: writes data to instance"""
        self.data = json.load(open(path, encoding='windows-1251'))

    def getData(self) -> list[Node]:
        """Returns all nodes"""
        return self.data

    def writeData(self) -> None:
        print('hehe')

    def writeSortedData(self):
        sorted = merge_sort(self.getData())
        f = open('sorted.txt', 'w')
        for i in sorted:
            f.write(str(i) + "\n")