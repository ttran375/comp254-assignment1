class DoublyLinkedList:
    class Node:
        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

        def get_element(self):
            return self.element

        def get_prev(self):
            return self.prev

        def get_next(self):
            return self.next

        def set_prev(self, prev):
            self.prev = prev

        def set_next(self, next):
            self.next = next

    def __init__(self):
        self.header = self.Node(None)
        self.trailer = self.Node(None, self.header)
        self.header.set_next(self.trailer)
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.header.get_next().get_element()

    def last(self):
        if self.is_empty():
            return None
        return self.trailer.get_prev().get_element()

    def add_first(self, element):
        self._add_between(element, self.header, self.header.get_next())

    def add_last(self, element):
        self._add_between(element, self.trailer.get_prev(), self.trailer)

    def remove_first(self):
        if self.is_empty():
            return None
        return self._remove(self.header.get_next())

    def remove_last(self):
        if self.is_empty():
            return None
        return self._remove(self.trailer.get_prev())

    def _add_between(self, element, predecessor, successor):
        new_node = self.Node(element, predecessor, successor)
        predecessor.set_next(new_node)
        successor.set_prev(new_node)
        self.size += 1

    def _remove(self, node):
        predecessor = node.get_prev()
        successor = node.get_next()
        predecessor.set_next(successor)
        successor.set_prev(predecessor)
        self.size -= 1
        return node.get_element()

    def __str__(self):
        result = "("
        walk = self.header.get_next()
        while walk != self.trailer:
            result += str(walk.get_element())
            walk = walk.get_next()
            if walk != self.trailer:
                result += ", "
        result += ")"
        return result

    def swap_two_nodes(self, node1, node2):
        if node1 == node2:
            return

        temp1 = self.header.get_next()
        temp2 = self.header.get_next()

        while temp1 != node1 and temp1 != self.trailer:
            temp1 = temp1.get_next()

        while temp2 != node2 and temp2 != self.trailer:
            temp2 = temp2.get_next()

        if temp1 == self.trailer or temp2 == self.trailer:
            print("One or both nodes not found in the list")
            return

        pred1 = node1.get_prev()
        succ1 = node1.get_next()
        pred2 = node2.get_prev()
        succ2 = node2.get_next()

        if node1.get_next() == node2:  # node1 is right before node2
            node1.set_next(succ2)
            node2.set_prev(pred1)
            node1.set_prev(node2)
            node2.set_next(node1)
            pred1.set_next(node2)
            succ2.set_prev(node1)
        elif node2.get_next() == node1:  # node2 is right before node1
            node2.set_next(succ1)
            node1.set_prev(pred2)
            node2.set_prev(node1)
            node1.set_next(node2)
            pred2.set_next(node1)
            succ1.set_prev(node2)
        else:  # node1 and node2 are not adjacent
            node1.set_next(succ2)
            node1.set_prev(pred2)
            node2.set_next(succ1)
            node2.set_prev(pred1)
            pred1.set_next(node2)
            succ1.set_prev(node2)
            pred2.set_next(node1)
            succ2.set_prev(node1)


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.add_first("MSP")
    list.add_last("ATL")
    list.add_last("BOS")
    list.add_first("LAX")
    print("Before swap:", list)
    list.swap_two_nodes(
        list.header.get_next().get_next(), list.trailer.get_prev().get_prev()
    )
    print("After swap:", list)
