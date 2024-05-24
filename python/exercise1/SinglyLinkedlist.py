# -*- coding: utf-8 -*-


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
        # If the nodes to be swapped are the same, no need to do anything
        if node1 == node2:
            return

        # Initialize pointers for tracking previous and current nodes
        prev1 = prev2 = None
        curr1 = curr2 = self.head

        # Traverse the list to find node1 and node2 and keep track of their previous node
        while curr1 and curr1 != node1:
            prev1 = curr1
            curr1 = curr1.next_node
        while curr2 and curr2 != node2:
            prev2 = curr2
            curr2 = curr2.next_node

        # If either node1 or node2 is not found in the list, exit the function
        if not curr1 or not curr2:
            return

        # If prev1 is not None, link the previous node of node1 to node2
        # Otherwise, update the head to point to node2
        if prev1:
            prev1.next_node = curr2
        else:
            self.head = curr2

        # If prev2 is not None, link the previous node of node2 to node1
        # Otherwise, update the head to point to node1
        if prev2:
            prev2.next_node = curr1
        else:
            self.head = curr1

        # Swap the next pointers of node1 and node2
        curr1.next_node, curr2.next_node = curr2.next_node, curr1.next_node

        # If the new next node of curr1 is None, update the tail to curr1
        # If the new next node of curr2 is None, update the tail to curr2
        if curr1.next_node is None:
            self.tail = curr1
        elif curr2.next_node is None:
            self.tail = curr2


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.add_first("MSP")
    list1.add_last("ATL")
    list1.add_last("BOS")
    list1.add_first("LAX")
    print(f"Before swapping: {list1}")

    node1 = list1.head.next_node
    node2 = list1.tail
    list1.swapTwoNodes(node1, node2)
    print(f"After swapping: {list1}")
