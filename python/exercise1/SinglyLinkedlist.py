class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.head.element

    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    def add_first(self, e):
        newest = Node(e, next_node=self.head)
        self.head = newest
        if self.is_empty():
            self.tail = self.head
        self.size += 1

    def add_last(self, e):
        newest = Node(e)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next_node = newest
        self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        answer = self.head.element
        self.head = self.head.next_node
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def __eq__(self, other):
        if not isinstance(other, SinglyLinkedList) or self.size != len(other):
            return False

        node1, node2 = self.head, other.head
        while node1 is not None:
            if node1.element != node2.element:
                return False
            node1, node2 = node1.next_node, node2.next_node

        return True

    def __str__(self):
        result = []
        node = self.head
        while node is not None:
            result.append(str(node.element))
            node = node.next_node
        return "(" + ", ".join(result) + ")"

    def swapTwoNodes(self, node1, node2):
        if node1 == node2:
            return

        prevNode1 = prevNode2 = None
        currentNode = self.head

        while currentNode is not None:
            if currentNode.next_node == node1:
                prevNode1 = currentNode
            elif currentNode.next_node == node2:
                prevNode2 = currentNode
            currentNode = currentNode.next_node

        if prevNode1 is None and prevNode2 is None:
            return

        if prevNode1 is not None:
            prevNode1.next_node = node2
        else:
            self.head = node2

        if prevNode2 is not None:
            prevNode2.next_node = node1
        else:
            self.head = node1

        temp = node1.next_node
        node1.next_node = node2.next_node
        node2.next_node = temp

        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail = node1


if __name__ == "__main__":
    list = SinglyLinkedList()
    list.add_first("MSP")
    list.add_last("ATL")
    list.add_last("BOS")
    list.add_first("LAX")
    print(f"Before swapping: {list}")

    node1 = list.head.next_node
    node2 = list.tail
    list.swapTwoNodes(node1, node2)
    print(f"After swapping: {list}")
