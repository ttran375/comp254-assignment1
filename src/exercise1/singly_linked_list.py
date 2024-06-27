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

    def swap_two_nodes(self, node1, node2):
        """
        Swaps two nodes in a singly linked list.
        """
        # No need to swap if the nodes are the same
        if node1 == node2:
            return

        # Initialize previous and current pointers for both nodes.
        prev1 = prev2 = None
        curr1 = curr2 = self.head

        # Find node1 and keep track of its previous node.
        while curr1 and curr1 != node1:
            prev1 = curr1
            curr1 = curr1.next_node

        # Find node2 and keep track of its previous node.
        while curr2 and curr2 != node2:
            prev2 = curr2
            curr2 = curr2.next_node

        # If either node1 or node2 is not found, no action is needed.
        if not curr1 or not curr2:
            return

        # Update the previous node's next pointer for node1.
        if prev1:
            prev1.next_node = curr2
        else:
            self.head = curr2

        # Update the previous node's next pointer for node2.
        if prev2:
            prev2.next_node = curr1
        else:
            self.head = curr1

        # Swap the next pointers of node1 and node2.
        curr1.next_node, curr2.next_node = curr2.next_node, curr1.next_node

        # Update the tail if necessary.
        if curr1.next_node is None:
            self.tail = curr1
        elif curr2.next_node is None:
            self.tail = curr2
