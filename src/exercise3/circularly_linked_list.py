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
        clone_list = CircularlyLinkedList()
        if not self.is_empty():
            current = self.tail.next_node
            clone_list.add_last(current.element)
            current = current.next_node
            while current != self.tail.next_node:
                clone_list.add_last(current.element)
                current = current.next_node
        return clone_list

    def same_sequence(self, other):
        if len(self) != len(other):
            return False

        if self.is_empty() and other.is_empty():
            return True

        start = self.tail.next_node
        for _ in range(len(self)):
            current_self = start
            current_other = other.tail.next_node
            match = True
            for _ in range(len(self)):
                if current_self.element != current_other.element:
                    match = False
                    break
                current_self = current_self.next_node
                current_other = current_other.next_node
            if match:
                return True
            start = start.next_node

        return False


if __name__ == "__main__":
    originalList = CircularlyLinkedList()
    originalList.add_last("MSP")
    originalList.add_last("ATL")
    originalList.add_last("BOS")

    print(originalList)  # Should print: [MSP, ATL, BOS]