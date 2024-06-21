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

    def swap_two_nodes(self, target_node1, target_node2):
        """
        Swaps two nodes in a singly linked list.

        This method swaps the positions of two nodes identified by `target_node1` and `target_node2`
        within the singly linked list. If either of the target nodes is not found in the list, or
        if both target nodes are the same, the method does nothing.

        Parameters:
        - self: The instance of the class containing the linked list.
        - target_node1: The first node to be swapped.
        - target_node2: The second node to be swapped.

        Returns:
        None

        Note:
        - The method assumes that `target_node1` and `target_node2` are actual node objects and not
        values contained within the nodes.
        - The method updates the `head` and `tail` of the list if necessary.
        - Swapping is done by changing the `next_node` pointers of the nodes preceding
        `target_node1` and `target_node2`, as well as the `next_node` pointers of `target_node1`
        and `target_node2` themselves.
        """
        if target_node1 == target_node2:
            return  # No action required if the nodes are the same

        prev1 = prev2 = None
        curr1 = curr2 = self.head

        # Find target_node1 and its predecessor
        while curr1 and curr1 != target_node1:
            prev1 = curr1
            curr1 = curr1.next_node

        # Find target_node2 and its predecessor
        while curr2 and curr2 != target_node2:
            prev2 = curr2
            curr2 = curr2.next_node

        # Exit if either node is not found
        if not curr1 or not curr2:
            return

        # Swap next_node pointers of predecessors
        if prev1:
            prev1.next_node = curr2
        else:
            self.head = curr2  # Update head if target_node1 was head

        if prev2:
            prev2.next_node = curr1
        else:
            self.head = curr1  # Update head if target_node2 was head

        # Swap next_node pointers of target nodes
        curr1.next_node, curr2.next_node = curr2.next_node, curr1.next_node

        # Update tail if necessary
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
    print(list1)

    first_node = list1.head.next_node
    second_node = list1.tail
    list1.swap_two_nodes(first_node, second_node)
    print(list1)
