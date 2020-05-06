"""
Stack

1. Push - insert an element to the top of stack
2. Pop - get and remove the top element of stack
3. Peek - get the top of stack without removing it

"""

class Stack:
    def __init__(self):
        self.elements = []
        self.top = None
    
    def isEmpty(self):
        if (self.top == None):
            return 1
        else:
            return 0

    def push(self, data):
        self.elements.append(data)
        self.top = data

    def pop(self):
        if (self.isEmpty()):
            return -1
        else:
            top_index = len(self.elements) - 1
            if (top_index == 0):
                self.top = None
            else:
                self.top = self.elements[top_index - 1]
            del top_index
            return self.elements.pop()
    
    def peek(self):
        if (self.isEmpty()):
            return -1
        else:
            return self.top

    def display(self):
        length = len(self.elements)
        print('\n---\nStack\n---')
        while (length != 0):
            print(self.elements[length - 1])
            length = length - 1
        print('---')


def main():
    stack = Stack()

    while True:
        print("\n1. Push\n2. Pop\n3. Peek\n0. Exit\nInput: ")
        x = int(input())
        if (x == 1):
            print('Data: ')
            data = int(input())
            stack.push(data)
        elif (x == 2):
            pop = stack.pop()
            if (pop == -1):
                print('Stack is empty!')
            else:
                print(str(pop) + ' is successfully popped from the stack!')
            del pop
        elif (x == 3):
            peek = stack.peek()
            if (peek == -1):
                print('Stack is empty!')
            else:
                print('The top element is ' + str(peek))
            del peek
        elif (x == 0):
            return
        else:
            print('Wrong input!')
        stack.display()

main()