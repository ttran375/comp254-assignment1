class SinglyLinkedList:
    class Node:
        def __init__(self, element, next=None):
            self.element = element
            self.next = next

        def get_element(self):
            return self.element

        def get_next(self):
            return self.next

        def set_next(self, next):
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.head.get_element()

    def last(self):
        if self.is_empty():
            return None
        return self.tail.get_element()

    def add_first(self, element):
        self.head = self.Node(element, self.head)
        if self.size == 0:
            self.tail = self.head
        self.size += 1

    def add_last(self, element):
        newest = self.Node(element, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.set_next(newest)
        self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        answer = self.head.get_element()
        self.head = self.head.get_next()
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return answer

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SinglyLinkedList):
            return False
        if self.size != other.size:
            return False
        walkA = self.head
        walkB = other.head
        while walkA is not None:
            if walkA.get_element() != walkB.get_element():
                return False
            walkA = walkA.get_next()
            walkB = walkB.get_next()
        return True

    def __clone__(self):
        other = SinglyLinkedList()
        if self.size > 0:
            other.head = self.Node(self.head.get_element(), None)
            walk = self.head.get_next()
            other_tail = other.head
            while walk is not None:
                newest = self.Node(walk.get_element(), None)
                other_tail.set_next(newest)
                other_tail = newest
                walk = walk.get_next()
        return other

    def __hash__(self):
        h = 0
        walk = self.head
        while walk is not None:
            h ^= hash(walk.get_element())
            h = (h << 5) | (h >> 27)
            walk = walk.get_next()
        return h

    def __str__(self):
        result = "("
        walk = self.head
        while walk is not None:
            result += str(walk.get_element())
            if walk != self.tail:
                result += ", "
            walk = walk.get_next()
        result += ")"
        return result

    def swap_two_nodes(self, node1, node2):
        if node1 == node2:
            return

        prev_node1 = None
        prev_node2 = None
        current_node = self.head

        while current_node is not None:
            if current_node.get_next() == node1:
                prev_node1 = current_node
            elif current_node.get_next() == node2:
                prev_node2 = current_node
            current_node = current_node.get_next()

        if prev_node1 is None or prev_node2 is None:
            return

        if prev_node1 is not None:
            prev_node1.set_next(node2)
        else:
            self.head = node2

        if prev_node2 is not None:
            prev_node2.set_next(node1)
        else:
            self.head = node1

        temp = node1.get_next()
        node1.set_next(node2.get_next())
        node2.set_next(temp)

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

    print("Before swapping:", list)

    node1 = list.head.get_next()
    node2 = list.tail

    list.swap_two_nodes(node1, node2)

    print("After swapping:", list)
