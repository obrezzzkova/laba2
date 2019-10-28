
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.unique_list = []
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']
        pass

    def __next__(self):
        while True:
            item = self.items.__next__()
            compare_item = None

            if self.ignore_case and type(item) is str:
                compare_item = item.lower()
            else:
                compare_item = item

            if compare_item not in self.unique_list:
                self.unique_list.append(compare_item)
                return item

    def __iter__(self):
        return self
