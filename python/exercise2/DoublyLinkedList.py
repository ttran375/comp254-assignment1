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
        # if first node is added to the list then below condition should be true.
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

    def clone(self):
        new_list = DoublyLinkedList()
        current = self.head
        while current is not None:
            new_list.add_node(current.data)
            current = current.next
        return new_list

    def concatenate(self, list2):
        if self.is_empty():
            self.head = list2.head
            self.tail = list2.tail
        elif not list2.is_empty():
            self.tail.next = list2.head
            list2.head.previous = self.tail
            self.tail = list2.tail


if __name__ == "__main__":
    L1 = DoublyLinkedList()
    L1.add_node("MSP")
    L1.add_node("ATL")
    L1.add_node("BOS")
    L1.display_list()

    L2 = DoublyLinkedList()
    L2.add_node("LAX")
    L2.add_node("ABC")
    L2.add_node("XYZ")
    L2.add_node("JFK")
    L2.display_list()

    L = L1.clone()
    L.concatenate(L2)
    L1.display_list()
    L2.display_list()
    L.display_list()
