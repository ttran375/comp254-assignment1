class Node:
    """Node of a singly linked list, which stores a reference to its element and to the subsequent node in the list (or None if this is the last node)."""

    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node

    def get_element(self):
        return self.element

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class SinglyLinkedList:
    """A basic singly linked list implementation."""

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
        return self.head.get_element()

    def last(self):
        if self.is_empty():
            return None
        return self.tail.get_element()

    def add_first(self, e):
        new_node = Node(e, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def add_last(self, e):
        new_node = Node(e, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
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
        if other is None or type(self) is not type(other):
            return False
        if self.size != other.size:
            return False
        walk_a = self.head
        walk_b = other.head
        while walk_a is not None:
            if walk_a.get_element() != walk_b.get_element():
                return False
            walk_a = walk_a.get_next()
            walk_b = walk_b.get_next()
        return True

    def __hash__(self):
        h = 0
        walk = self.head
        while walk is not None:
            h ^= hash(walk.get_element())
            h = (h << 5) | (h >> 27)
            walk = walk.get_next()
        return h

    def __str__(self):
        result = []
        walk = self.head
        while walk is not None:
            result.append(str(walk.get_element()))
            walk = walk.get_next()
        return "(" + ", ".join(result) + ")"

    def swap_two_nodes(self, node1, node2):
        if node1 == node2:
            return

        prev_node1, prev_node2 = None, None
        current_node = self.head

        # Find previous nodes of node1 and node2
        while current_node is not None:
            if current_node.get_next() == node1:
                prev_node1 = current_node
            elif current_node.get_next() == node2:
                prev_node2 = current_node
            current_node = current_node.get_next()

        # If either node1 or node2 is not present in the list
        if prev_node1 is None or prev_node2 is None:
            return

        # If node1 is not head of list
        if prev_node1 is not None:
            prev_node1.set_next(node2)
        else:
            self.head = node2

        # If node2 is not head of list
        if prev_node2 is not None:
            prev_node2.set_next(node1)
        else:
            self.head = node1

        # Swap next pointers of node1 and node2
        temp = node1.get_next()
        node1.set_next(node2.get_next())
        node2.set_next(temp)

        # Change tail if needed
        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail = node1

    def clone(self):
        other = SinglyLinkedList()
        if self.size > 0:
            other.head = Node(self.head.get_element(), None)
            walk = self.head.get_next()
            other_tail = other.head
            while walk is not None:
                newest = Node(walk.get_element(), None)
                other_tail.set_next(newest)
                other_tail = newest
                walk = walk.get_next()
        other.size = self.size
        return other

    @staticmethod
    def main():
        list = SinglyLinkedList()
        list.add_first("MSP")
        list.add_last("ATL")
        list.add_last("BOS")
        list.add_first("LAX")

        print("Before swapping:", list)

        node1 = list.head.get_next()  # Node with "MSP"
        node2 = list.tail  # Node with "BOS"

        list.swap_two_nodes(node1, node2)

        print("After swapping:", list)


if __name__ == "__main__":
    SinglyLinkedList.main()
