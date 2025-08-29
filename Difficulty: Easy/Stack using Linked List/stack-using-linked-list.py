class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    def __init__(self):
        self.top = None   # head pointer of stack

    # Function to push an integer into the stack
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.top   # new node points to old top
        self.top = newNode        # move top to new node

    # Function to remove an item from top of the stack
    def pop(self):
        if self.top is None:
            return -1   # stack underflow case

        popped = self.top.data
        self.top = self.top.next  # move top down
        return popped