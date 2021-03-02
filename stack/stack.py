class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Array implementation class
    """

    def __init__(self):
        self.head = None


    def display(self):
        """
        Print stack
        """
        if self.isEmpty():
            return ''
        curr = self.head
        output = ''
        while curr:
            output += str(curr.data) + '->'
            curr = curr.next
        return output[:-2]


    def isEmpty(self):
        """
        Check if the stack is empty
        """
        return self.head == None


    def peek(self):
        """
        Get the top item of the stack
        """
        if self.isEmpty():
            return IndexError('Stack is empty.')
        return self.head.data


    def push(self, data):
        """
        Push a data into the stack
        """
        node = Node(data)
        node.next = self.head
        self.head = node


    def pop(self):
        """
        Remove a data from the stack and return
        """
        if self.isEmpty():
            return IndexError('Stack is empty.')
        node = self.head
        self.head = self.head.next
        return node.data