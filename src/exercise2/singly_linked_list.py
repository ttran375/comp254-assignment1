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

    def concatenate(self, new_list):
        """
        Concatenates another singly linked list to the end of this list.
        """
        # Set head and tail to the new list's head and tail if the current list is empty
        if self.is_empty():
            self.head = new_list.head
            self.tail = new_list.tail

        # If the new list is not empty
        elif not new_list.is_empty():

            # Link the last node of the current list to the first node of the new list
            self.tail.next_node = new_list.head

            # Update the tail to be the last node of the new list
            self.tail = new_list.tail

        # Update the size of the current list by adding the size of the new list
        self.size += new_list.size


def clone_linked_list(l1):
    dl = SinglyLinkedList()
    temp = l1.head
    if temp is not None:
        while temp is not None:
            dl.add_last(temp.element)
            temp = temp.next_node
    return dl


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.add_first("MSP")
    list1.add_last("ATL")
    list1.add_last("BOS")
    print(list1)

    list2 = SinglyLinkedList()
    list2.add_first("ABC")
    list2.add_last("XYZ")
    list2.add_first("MNP")
    print(list2)

    list_concat = clone_linked_list(list1)
    list_concat.concatenate(list2)
    print(list_concat)
