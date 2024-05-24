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

    def swapTwoNodes(self, node1, node2):
        if node1 == node2:
            return

        if node1.next == node2:
            node1.previous, node2.next, node2.previous, node1.next = (
                node2.previous,
                node1,
                node1,
                node2.next,
            )
            if node1.previous:
                node1.previous.next = node2
            if node2.next:
                node2.next.previous = node1
            if self.head == node1:
                self.head = node2
            if self.tail == node2:
                self.tail = node1
        elif node2.next == node1:
            self.swapTwoNodes(node2, node1)
        else:
            node1_next = node1.next
            node1_prev = node1.previous
            node2_next = node2.next
            node2_prev = node2.previous

            if node1_next:
                node1_next.previous = node2
            if node1_prev:
                node1_prev.next = node2
            if node2_next:
                node2_next.previous = node1
            if node2_prev:
                node2_prev.next = node1

            node1.next, node2.next = node2_next, node1_next
            node1.previous, node2.previous = node2_prev, node1_prev

            if self.head == node1:
                self.head = node2
            elif self.head == node2:
                self.head = node1

            if self.tail == node1:
                self.tail = node2
            elif self.tail == node2:
                self.tail = node1


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    list1.add_node("MSP")
    list1.add_node("ATL")
    list1.add_node("BOS")
    list1.add_node("LAX")
    print("Before swapping:")
    list1.display_list()

    node1 = list1.head.next
    node2 = list1.tail
    list1.swapTwoNodes(node1, node2)
    print("After swapping:")
    list1.display_list()
