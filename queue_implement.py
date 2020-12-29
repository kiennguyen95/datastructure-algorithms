class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    Array implementation class
    """

    def __init__(self):
        self.front = self.rear = None


    def display(self):
        """
        Print queue
        """
        if self.isEmpty():
            return ''
        curr = self.front
        output = ''
        while curr:
            output += str(curr.data) + '->'
            curr = curr.next
        return output[:-2]


    def isEmpty(self):
        """
        Check if the queue is empty
        """
        return self.front == None


    def enQueue(self, data):
        """
        Add an item to the queue
        """
        node = Node(data)

        if self.rear == None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node


    def deQueue(self):
        """
        Remove an item from queue
        """
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None