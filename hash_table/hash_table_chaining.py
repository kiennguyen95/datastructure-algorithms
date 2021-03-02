class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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
            while node:
                new_table.add(node.key, node.value, True)
                node = node.next

        self.array = new_table.array
        self.capacity = new_capacity


    def hash(self, key):
        return key % len(self.array)


    def display(self):
        output = ''
        for i in range(len(self.array)):
            output += '[%s]' % i
            node = self.array[i]
            while node:
                output += " -> (%s, %s)" % (node.key, node.value)
                node = node.next
            output += '\n'
        return output


    def getSize(self):
        return self.size


    def getCapacity(self):
        return self.capacity


    def add(self, key, value, append = False):
        if self.size >= self.capacity / 2:
            self.resize(self.capacity * 2)

        index = self.hash(key)
        node = Node(key, value)

        if not append:
            if self.array[index]:
                node.next = self.array[index]
            self.array[index] = node
        else:
            if not self.array[index]:
                self.array[index] = node
            else:
                p = self.array[index]
                while p.next:
                    p = p.next
                p.next = node
        self.size += 1


    def get(self, key):
        index = self.hash(key)
        node = self.array[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError


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
        h.add(3, 'Three')
        self.assertEqual(h.get(3), 'Three')
        h.add(3, 'New three')
        h.add(5, 'Five')
        h.add(17, 'Seventeen')
        self.assertEqual(h.get(1), 'One')
        self.assertEqual(h.get(3), 'New three')
        self.assertEqual(h.get(17), 'Seventeen')
        self.assertRaises(KeyError, h.get, 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
