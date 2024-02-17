import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.index_map = {}

    def search(self, val):
        return val in self.index_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.index_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        index = self.index_map[val]
        self.lst[index] = self.lst[-1]
        self.index_map[self.lst[-1]] = index
        self.lst.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)