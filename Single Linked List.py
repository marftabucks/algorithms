""" 
Single Linked List

Operations:
1. Insert - add a node at the beginning of linked list
2. Delete - delete a node at the beginning of linked list
3. Delete data - delete node that contains the data from the linked list
4. Search - search a node using the given data
5. Update - update a node that contains the data with a new data
6. Display - print all the lists
"""

## Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # Get the node data
    def getData(self):
        return self.data

## Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        
    # Insert a node at the beginning of linked list    
    def insert(self, data):
        temp = Node(data)

        # If the linked list is empty
        if (self.head is None):
            self.head = temp

        # Else, if the linked list is not empty
        else:
            temp.next = self.head
            self.head = temp
        del temp
    
    # Delete a node from the linked list
    def delete(self, data = None):

        # If the linked list is empty
        if (self.head is None):
            return -1

        # Else, if the linked list is not empty
        else:
            # If no parameter is given, delete the beginning
            if (data == None):
                self.head = self.head.next

            # Else, search for the node that contains the data and delete it
            else:
                temp = self.head
                prev = Node(None)
                prev.next = temp

                # If the head is the data
                if (temp.data == data):
                    self.head = temp.next
                    del temp
                    return 0

                while True:

                    # If the data is found
                    if (temp.data == data):
                        prev.next = temp.next
                        del temp
                        return 0
                        
                    else:

                        # If it reaches the end of the linked list
                        if (temp.next == None):
                            return -1
                        
                        # Else, go to the next node
                        else:
                            prev = prev.next
                            temp = temp.next
                del prev
        del temp
        

    # Update a node that contains the data
    def update(self, data, new_data):
        temp = self.head
        while True:

            # If the data is found
            if (temp.data == data):
                temp.data = new_data
                return 0
            else:

                # If it reaches the end of the linked list
                if (temp.next == None):
                    return -1
                
                # Else, go to the next node
                else:
                    temp = temp.next
        del temp

    # Search for a node that contains the data
    def search(self, data):
        temp = self.head
        while True:

            # If the data is found
            if (temp.data == data):
                return 0
            else:

                # If it reaches the end of the linked list
                if (temp.next == None):
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
            while (temp is not None):
                print(temp.getData(), end = " -> ")
                temp = temp.next
            del temp

def main():
    print("1. Insert\n2. Update\n3. Search\n4. Delete\n0. Exit")

    ll = LinkedList()

    while True:
        print("\n--------------------\nInput: ")
        x = int(input())

        if (x == 0):
            return
        elif (x == 1):
            print("Data: ")
            data = int(input())
            ll.insert(data)
        elif (x == 2):
            print("Data: ")
            data = int(input())
            print("Data 2:")
            new_data = int(input())
            if (ll.update(data, new_data) != 0):
                print("Data is not found")
            else:
                print("Data has been successfully updated")
        elif (x == 3):
            print("Data: ")
            data = int(input())
            if (ll.search(data) != 0):
                print("Data is not found")
            else:
                print("Data is found")
        elif (x == 4):
            print("Data: ")
            data = int(input())
            if (ll.delete(data) != 0):
                print("Data is not found")
            else:
                print("Data has been sucessfully deleted")
        else:
            print("Wrong input!")

        print("\n--------------------")
        ll.display()

main()