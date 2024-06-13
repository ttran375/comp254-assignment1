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
        return self.head is None

    def add_node(self, data):
        #  Creating New Node
        new_node = Node(data)

        # Checking where the head and tail pointer is pointing.
        # if first node is added to the list then below condition should be
        # true.
        if self.head is None:
            self.head = new_node
            new_node.previous = new_node.next = None

        else:
            # Addding new node at the last
            self.tail.next = new_node
            new_node.previous = self.tail
            new_node.next = None
        self.tail = new_node

    def display_list(self):
        # Creating temp pointer to traverse
        temp = self.head
        if temp is not None:
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")
        else:
            print("List does not have any nodes")

    def concatenate(self, list2):
        if self.is_empty():
            self.head = list2.head
            self.tail = list2.tail
        elif not list2.is_empty():
            self.tail.next = list2.head
            list2.head.previous = self.tail
            self.tail = list2.tail


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
    list1.display_list()

    list2 = DoublyLinkedList()
    list2.add_node("ABC")
    list2.add_node("XYZ")
    list2.add_node("MNP")
    list2.display_list()

    list_concat = clone_linked_list(list1)
    list_concat.concatenate(list2)
    list_concat.display_list()
