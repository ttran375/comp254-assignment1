class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # TO check weather list is empty or not?

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_node(self, data):
        #  Creating New Node
        newNode = Node(data)

        # Checking where the head and tail pointer is pointing.
        # if first node is added to the list then below condition should be
        # true.
        if self.head is None:
            self.head = newNode
            newNode.previous = newNode.next = None

        else:
            # Addding new node at the last
            self.tail.next = newNode
            newNode.previous = self.tail
            newNode.next = None
        self.tail = newNode

    def display_list(self):
        # Creating temp pointer to travers
        temp = self.head
        if temp is not None:
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            else:
                print("NULL")
        else:
            print("List does not have any nodes")

    def swapTwoNodes(self, node1, node2):
        if node1 is node2:
            return

        # Swap next pointers
        if node1.next is not None:
            node1.next.previous = node2
        if node2.next is not None:
            node2.next.previous = node1
        node1.next, node2.next = node2.next, node1.next

        # Swap previous pointers
        if node1.previous is not None:
            node1.previous.next = node2
        if node2.previous is not None:
            node2.previous.next = node1
        node1.previous, node2.previous = node2.previous, node1.previous

        # Fix head and tail if necessary
        if self.head == node1:
            self.head = node2
        elif self.head == node2:
            self.head = node1

        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail = node1
