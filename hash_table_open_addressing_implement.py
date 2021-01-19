class Node:
    def __init__(self, key, value):
       self.key = key
       self.value = value


class HashTable(object):

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.array = self.createArray(self.capacity)


    def createArray(self, capacity):
        return [None] * capacity


    def resize(self, new_capacity):
        new_table = HashTable(new_capacity)
        for i in range(self.capacity):
            node = self.array[i]
            if node:
                new_table.add(node.key, node.value)

        self.array = new_table.array
        self.capacity = new_capacity


    def hash(self, key, trial_count):
        return (key + trial_count) % len(self.array)


    def display(self):
        output = ''
        for i in range(len(self.array)):
            output += '[%s] -> ' % (i)
            if self.array[i]:
                output += '(%s: %s)' % (self.array[i].key, self.array[i].value)
            output += '\n'
        return output


    def getSize(self):
        return self.size


    def getCapacity(self):
        return self.capacity


    def add(self, key, value):
        if self.size >= self.capacity / 2:
            self.resize(self.capacity * 2)

        trial_count = 0
        index = self.hash(key, trial_count)
        while self.array[index] and self.array[index].key != key:
            trial_count += 1
            index = self.hash(key, trial_count)

        self.array[index] = Node(key, value)
        self.size += 1


    def get(self, key):
        trial_count = 0
        index = self.hash(key, trial_count)
        while True:
            if trial_count > self.capacity or self.array[index] == None:
                raise KeyError
            if self.array[index] and self.array[index].key == key:
                return self.array[index].value
            trial_count += 1
            index = self.hash(key, trial_count)


    def delete(self, key):
        trial_count = 0
        index = self.hash(key, trial_count)
        while True:
            if trial_count > self.capacity or self.array[index] == None:
                raise KeyError
            if self.array[index] and self.array[index].key == key:
                self.array[index] = 0
                return
            trial_count += 1
            index = self.hash(key, trial_count)


import unittest


class TestHashTable(unittest.TestCase):

    def testTableDoubling(self):
        h = HashTable(4)
        h.add(1, 'One')
        h.add(2, 'Two')
        self.assertEqual(h.getCapacity(), 4)
        h.add(3, 'Three')
        self.assertEqual(h.getCapacity(), 8)
        h.add(4, 'Four')
        h.add(5, 'Five')
        h.add(6, 'Six')
        self.assertEqual(h.getCapacity(), 16)
        self.assertEqual(h.getSize(), 6)


    def testIO(self):
        h = HashTable(4)
        h.add(1, 'One')
        h.add(2, 'Two')
        h.delete(2)
        h.add(3, 'Three')
        self.assertEqual(h.get(3), 'Three')
        h.add(3, 'New three')
        h.add(5, 'Five')
        h.add(17, 'Seventeen')
        self.assertEqual(h.get(1), 'One')
        self.assertEqual(h.get(3), 'New three')
        self.assertEqual(h.get(17), 'Seventeen')
        self.assertRaises(KeyError, h.get, 2)
        self.assertRaises(KeyError, h.get, 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)