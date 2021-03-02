import ctypes


class Array():
    """
    Array implementation class
    """

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self.array = self._create_array(self._capacity)

    def _create_array(self, capacity):
        return [ctypes.py_object] * capacity

    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self.array[i]

        self.array = new_array
        self._capacity = new_capacity

    def display(self):
        for items in self.array:
            return " ".join(str(self.array[x]) for x in range(self._size))

    def size(self):
        """
        Return number of items are currently stored in array-linkedlist
        """
        return self._size

    def capacity(self):
        """
        Return number of items array-linkedlist can hold
        """
        return self._capacity

    def isEmpty(self):
        """
        If array-linkedlist is empty, return true. Otherwise, return false
        """
        return self._size == 0

    def itemAt(self, index):
        """
        Return item at given index
        """
        if not 0 <= index < self._size:
            return IndexError('Index out of range')
        return self.array[index]

    def append(self, item):
        """
        Append given item to the end of array-linkedlist, increase capacity if not available
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self.array[self._size] = item
        self._size += 1

    def insert(self, item, index):
        """
        Insert item at given index
        """
        if not 0 <= index < self._size:
            return IndexError('Index out of range')

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = item
        self._size += 1

    def pop(self):
        """
        Remove last item and return its value
        """
        if self._size == 0:
            return None
        last_item = self.array[self._size - 1]
        self._size -= 1
        if self._size <= self._capacity / 4:
            self._resize(self._capacity / 2)

        return last_item

    def removeAt(self, index):
        """
        Remove item at given index and return its value
        """
        if not 0 <= index < self._size:
            return IndexError('Index out of range')

        removed_item = self.array[index]
        for i in range(index, self._size - 1):
            self.array[i] = self.array[i + 1]

        self._size -= 1
        if self._size <= self._capacity / 4:
            self._resize(self._capacity / 2)

        return removed_item
