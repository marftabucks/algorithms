"""
Queue

1. Enqueue - insert an element to the end of queue
2. Dequeue - get and remove the first element of queue
3. Peek - get the first of queue without removing it

"""

class Queue:
    def __init__(self):
        self.elements = []
        self.first = None
    
    def isEmpty(self):
        if (self.first == None):
            return 1
        else:
            return 0

    def enqueue(self, data):
        self.elements.append(data)
        self.first = self.elements[0]

    def dequeue(self):
        if (self.isEmpty()):
            return -1
        else:
            first = self.elements[0]
            max_index = len(self.elements) - 1
            i = 0
            while (i != max_index):
                self.elements[i] = self.elements[i + 1]
                i += 1
            self.first = self.elements[0]
            del max_index, i, self.elements[max_index]
            return first
    
    def peek(self):
        if (self.isEmpty()):
            return -1
        else:
            return self.first

    def display(self):
        print('\n---\nQueue\n---')
        for element in self.elements:
            print(element, end = " ")


def main():
    queue = Queue()
    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Peek\n0. Exit\nInput: ")
        x = int(input())
        if (x == 1):
            print('Data: ')
            data = int(input())
            queue.enqueue(data)
        elif (x == 2):
            dequeue = queue.dequeue()
            if (dequeue == -1):
                print('Queue is empty!')
            else:
                print(str(dequeue) + ' is successfully dequeued from the queue!')
            del dequeue
        elif (x == 3):
            peek = queue.peek()
            if (peek == -1):
                print('Queue is empty!')
            else:
                print('The first element is ' + str(peek))
            del peek
        elif (x == 0):
            return
        else:
            print('Wrong input!')
        queue.display()

main()