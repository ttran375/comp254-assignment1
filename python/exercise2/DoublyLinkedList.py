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


def clone_linked_list(l1):
    dl = DoublyLinkedList()
    temp = l1.head
    if temp is not None:
        while temp is not None:
            dl.add_node(temp.data)
            temp = temp.next
    return dl


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    list1.add_node("MSP")
    list1.add_node("ATL")
    list1.add_node("BOS")
    # list1.remove_first()
    print(list1.display_list())
