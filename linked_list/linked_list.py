class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def display(self):
        current = self.first
        while current:
            print(current.data, end = ' ')
            current = current.next

    def getNode(self, index):
        current = self.first
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def remove(self, node):
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev

    def insertAfter(self, ref_node, new_node):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.last = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        ref_node.next = new_node

    def insertBefore(self, ref_node, new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.first = new_node
        else:
            new_node.prev = ref_node.prev
            new_node.prev.next = new_node
        ref_node.prev = new_node

    def size(self):
        """
        Return number of nodes are currently stored in list
        """
        return self._size

    def isEmpty(self):
        """
        Determine list is empty or not
        """
        return self._size == 0

    def valueAt(self, index):
        """
        Determine list is empty or not
        """
        node = self.getNode(index)
        if node:
            return node.data
        else:
            return None

    def pushFront(self, value):
        """
        Add a node with value to the front of list
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.insertBefore(self.first, new_node)
        self._size += 1

    def popFront(self):
        """
        Remove front node and return its value
        """
        first_node = self.first
        self.remove(self.first)
        self._size -= 1
        return first_node.data

    def pushBack(self, value):
        """
        Add a node with value to the end of list
        """
        new_node = Node(value)
        if self.last is None:
            self.last = new_node
            self.first = new_node
        else:
            self.insertAfter(self.last, new_node)
        self._size += 1

    def popBack(self):
        """
        Remove last node and return its value
        """
        last_node = self.last
        self.remove(self.last)
        self._size -= 1
        return last_node.data

    def front(self):
        """
        Return value of front node
        """
        return self.first.data

    def back(self):
        """
        Return value of last node
        """
        return self.last.data

    def insert(self, value, index):
        """
        Insert a node with value at given index
        """
        new_node = Node(value)
        current_node = self.getNode(index)
        self.insertBefore(current_node, new_node)

    def removeAt(self, index):
        """
        Remove node at given index
        """
        node = self.getNode(index)
        self.remove(node)
