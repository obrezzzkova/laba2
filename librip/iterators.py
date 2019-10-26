data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['A','b','a','B']

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = list(items)
        self.items = [str(x) for x in self.items]
        self.unique_list = []
        self.index = 0
        self.ignore_case = False
        if len(kwargs > 0):
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        if self.index > len(self.items):
            raise StopIteration
        if self.ignore_case is False:
            if self.items[self.current].upper() and self.items[self.current].lower() not in self.unique_list:
                self.unique_list.append(self.iems[current].lower())
                self.index += 1
                return self.unique_list[len(self.unique_list) - 1]
        if self.ignore_case is True:
            if self.items[self.current].upper() and self.items[self.current].lower() not in self.unique_list:
                self.unique_list.append(self.items[self.index])
                self.index += 1
                return self.unique_list[len(self.unique_list) -1]

    def __iter__(self):
        return self
