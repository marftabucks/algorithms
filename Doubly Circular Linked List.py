""" 
Doubly Linked List

Operations:
1. Insert - add a node to the linked list
    a. Insert First
    b. Insert Last
2. Delete - delete a node from the linked list
    a. Delete a given data
    b. Delete First
    c. Delete Last
4. Search - search a node
    a. Search with a given data
5. Update - update a node 
    a. Update with a given data
    b. Update first
    c. Update last
6. Display - print all the lists
"""

## Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    # Get the node data
    def getData(self):
        return self.data

## Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Insert a node at the beginning of linked list    
    def insertHead(self, data):
        temp = Node(data)

        # If the linked list is empty
        if (self.head is None):
            self.head = temp
            self.tail = temp
            self.head.prev = self.tail
            self.tail.next = self.head

        # Else, if the linked list is not empty
        else:
            temp.next = self.head
            self.head.prev = temp
            temp.prev = self.tail
            self.tail.next = temp
            self.head = temp
        del temp

    # Insert a node at the end of linked list    
    def insertTail(self, data):
        temp = Node(data)

        # If the linked list is empty
        if (self.head is None):
            self.head = temp
            self.tail = temp
            self.head.prev = self.tail
            self.tail.next = self.head

        # Else, if the linked list is not empty
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
            self.tail.next = self.head
        del temp

    # Delete a node with a given data
    def delete(self, data = None):

        # If the linked list is empty
        if (self.head is None):
            return -1

        # Else, if the linked list is not empty
        else:
            # If no parameter is given, delete the beginning
            if (data == None):
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                return 0

            # Else, search for the node that contains the data and delete it
            else:
                temp = self.head
                prev = temp.prev

                # If the head is the data
                if (temp.data == data):
                    self.head = temp.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    del temp
                    return 0

                while True:

                    # If the data is found
                    if (temp.data == data):
                        temp = temp.next
                        temp.prev = prev
                        prev.next = temp
                        del temp
                        return 0
                        
                    else:

                        # If it reaches the end of the linked list
                        if (temp.next is self.head):
                            return -1
                        
                        # Else, go to the next node
                        else:
                            prev = prev.next
                            temp = temp.next
                del prev, temp

    # Delete head from the linked list
    def deleteHead(self):

        # If the linked list is empty
        if (self.head is None):
            return -1

        # Else, the linked list is not empty
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            return 0

    # Delete tail from the linked list
    def deleteTail(self):

        # If the linked list is empty
        if (self.head is None):
            return -1

        # Else, the linked list is not empty
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            return 0

    # Update a node with a given data to new data
    def update(self, data, new_data):
        temp = self.head
        while True:

            # If the data is found
            if (temp.data == data):
                temp.data = new_data
                return 0
            else:

                # If it reaches the end of the linked list
                if (temp.next is self.head):
                    return -1
                
                # Else, go to the next node
                else:
                    temp = temp.next
        del temp

    # Update head with a new data
    def updateHead(self, new_data):

        # If the linked list is empty
        if (self.head is None):
            return -1
        else:
            self.head.data = new_data
            return 0

    # Update tail with a new data
    def updateTail(self, new_data):

        # If the linked list is empty
        if (self.head is None):
            return -1
        else:
            self.tail.data = new_data
            return 0

    # Search for a node that contains the data
    def search(self, data):
        temp = self.head
        while True:

            # If the data is found
            if (temp.data == data):
                return 0
            # If the data is not found
            else:

                # If it reaches the end of the linked list
                if (temp.next is self.head):
                    return -1
                
                # Else, go to the next node
                else:
                    temp = temp.next
        del temp

    # Print all the nodes in linked list
    def display(self):
        if (self.head is None):
            print("Linked list is empty")
        else:
            temp = self.head
            while True:
                print(temp.getData(), end = " -> ")
                temp = temp.next
                if (temp is self.head):
                    break
            del temp

def main():
    print("1. Insert Head\n2. Insert Tail\n3. Update with a given data\n4. Update Head\n5. Update Tail\n6. Search\n7. Delete with a given data\n8. Delete Head\n9. Delete Tail\n0. Exit")

    ll = LinkedList()

    while True:
        print("\n--------------------\nInput: ")
        x = int(input())
        if (x == 0):
            return
        elif (x == 1):
            print("Data: ")
            data = int(input())
            ll.insertHead(data)
        elif (x == 2):
            print("Data: ")
            data = int(input())
            ll.insertTail(data)
        elif (x == 3):
            print("Data to be changed: ")
            data = int(input())
            print("New data:")
            new_data = int(input())
            if (ll.update(data, new_data) != 0):
                print("Data is not found")
            else:
                print("Data has been successfully updated")
        elif (x == 4):
            print("New data:")
            new_data = int(input())
            if (ll.updateHead(new_data) != 0):
                print("Data is not found")
            else:
                print("Data has been successfully updated")
        elif (x == 5):
            print("New data:")
            new_data = int(input())
            if (ll.updateTail(new_data) != 0):
                print("Data is not found")
            else:
                print("Data has been successfully updated")
        elif (x == 6):
            print("Data: ")
            data = int(input())
            if (ll.search(data) != 0):
                print("Data is not found")
            else:
                print("Data is found")
        elif (x == 7):
            print("Data: ")
            data = int(input())
            if (ll.delete(data) != 0):
                print("Data is not found")
            else:
                print("Data has been sucessfully deleted")
        elif (x == 8):
            if (ll.deleteHead() != 0):
                print("Data is not found")
            else:
                print("Data has been sucessfully deleted")
        elif (x == 9):
            if (ll.deleteTail() != 0):
                print("Data is not found")
            else:
                print("Data has been sucessfully deleted")
        else:
            print("Wrong input!")

        print("\n--------------------")
        ll.display()

main()