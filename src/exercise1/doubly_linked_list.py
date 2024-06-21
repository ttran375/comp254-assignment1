class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # TO check weather list is empty or not?

    def is_empty(self):
        return self.head is None

    def add_node(self, data):
        #  Creating New Node
        new_node = Node(data)

        # Checking where the head and tail pointer is pointing.
        # if first node is added to the list then below condition should be
        # true.
        if self.head is None:
            self.head = new_node
            new_node.previous = new_node.next = None

        else:
            # Addding new node at the last
            self.tail.next = new_node
            new_node.previous = self.tail
            new_node.next = None
        self.tail = new_node

    def display_list(self):
        # Creating temp pointer to traverse
        temp = self.head
        if temp is not None:
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")
        else:
            print("List does not have any nodes")

    def swap_two_nodes(self, node1, node2):
        """
        Swaps two nodes in a doubly linked list.

        This method swaps two nodes, `node1` and `node2`, by adjusting their `next` and `previous`
        pointers.
        It handles cases where the nodes to be swapped are adjacent and also updates the `head` and
        `tail` of the list
        if either node is currently at one of these positions. The swap does not proceed if `node1`
        and `node2` are the same.

        Parameters:
            node1 (Node): The first node to swap.
            node2 (Node): The second node to swap.

        Returns:
            None: This method returns nothing and modifies the list in-place.

        Raises:
            AttributeError: If either `node1` or `node2` is not of the correct `Node` type or is
            None.

        Example:
            Given a doubly linked list: A <-> B <-> C <-> D,
            if `node1` is B and `node2` is C, calling `swap_two_nodes(node1, node2)` will modify
            the list to: A <-> C <-> B <-> D.
        """
        # Check if the nodes are the same; if so, no need to swap
        if node1 is node2:
            return

        # Swap the next pointers of node1 and node2
        if node1.next is not None:
            node1.next.previous = node2
        if node2.next is not None:
            node2.next.previous = node1

        # Swap the next pointers
        node1.next, node2.next = node2.next, node1.next

        # Swap the previous pointers of node1 and node2
        if node1.previous is not None:
            node1.previous.next = node2
        if node2.previous is not None:
            node2.previous.next = node1

        # Swap the previous pointers
        node1.previous, node2.previous = (
            node2.previous,
            node1.previous,
        )

        # Update the head of the list if necessary
        if self.head == node1:
            self.head = node2
        elif self.head == node2:
            self.head = node1

        # Update the tail of the list if necessary
        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail = node1


def clone_linked_list(l1):
    dl = DoublyLinkedList()
    temp = l1.head
    if temp is not None:
        while temp is not None:
            dl.add_node(temp.data)
            temp = temp.next
    return dl


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    list1.add_node("MSP")
    list1.add_node("ATL")
    list1.add_node("BOS")
    list1.add_node("LAX")
    list1.display_list()

    first_node = list1.head.next
    second_node = list1.tail
    list1.swap_two_nodes(first_node, second_node)
    list1.display_list()
