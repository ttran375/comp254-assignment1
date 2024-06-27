# -*- coding: utf-8 -*-


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class CircularlyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            return None
        return self.tail.next_node.element

    def last(self):
        if self.is_empty():
            return None
        return self.tail.element

    def rotate(self):
        if self.tail is not None:
            self.tail = self.tail.next_node

    def add_first(self, e):
        if self.is_empty():
            self.tail = Node(e)
            self.tail.next_node = self.tail  # a new list of one element
        else:
            newest = Node(e)
            newest.next_node = self.tail.next_node
            self.tail.next_node = newest
        self.size += 1

    def add_last(self, e):
        self.add_first(e)
        self.tail = self.tail.next_node

    def remove_first(self):
        if self.is_empty():
            return None
        old_head = self.tail.next_node
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next_node = old_head.next_node
        self.size -= 1
        return old_head.element

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = []
        current = self.tail.next_node
        result.append(str(current.element))
        current = current.next_node
        while current != self.tail.next_node:
            result.append(str(current.element))
            current = current.next_node
        return "[" + ", ".join(result) + "]"

    def clone(self):
        """
        Creates a clone of the circularly linked list.
        """
        # Initialize an empty clone list.
        clone_list = CircularlyLinkedList()

        # If the current list is not empty
        if not self.is_empty():

            # Add the element after tail to the clone list
            current = self.tail.next_node
            clone_list.add_last(current.element)

            # Traverse other elements and add them to the clone list
            current = current.next_node
            while current != self.tail.next_node:
                clone_list.add_last(current.element)
                current = current.next_node

        # Return the cloned list
        return clone_list

    def same_sequence(self, other):
        """
        Checks if two circularly linked lists have the same sequence of elements.
        """
        # Return false if the lengths of the two lists are different
        if len(self) != len(other):
            return False

        # Return true if both lists are empty
        if self.is_empty() and other.is_empty():
            return True

        # Start from the element after tail
        start = self.tail.next_node

        # Loop through each possible starting point in the current list
        for _ in range(len(self)):

            # Compare the elements of the two lists starting from the current position
            current_self = start
            current_other = other.tail.next_node
            match = True
            for _ in range(len(self)):
                if current_self.element != current_other.element:
                    match = False
                    break
                current_self = current_self.next_node
                current_other = current_other.next_node

            # If all elements match, the sequences are the same
            if match:
                return True

            # Move to the next starting point in the current list
            start = start.next_node

        # Return False if no matching sequence is found
        return False
