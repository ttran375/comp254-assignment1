# Test cases for swapTwoNodes using pytest
import pytest
from singly_linked_list import SinglyLinkedList


def create_list(elements):
    sll = SinglyLinkedList()
    for element in elements:
        sll.add_last(element)
    return sll


@pytest.mark.parametrize(
    "elements,node1_idx,node2_idx,expected_elements",
    [
        ([1, 2, 3, 4, 5], 1, 3, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 0, 4, [5, 2, 3, 4, 1]),
        ([1, 2, 3, 4, 5], 2, 2, [1, 2, 3, 4, 5]),
        ([1, 2, 3], 0, 1, [2, 1, 3]),
    ],
)
def test_swap_two_nodes(elements, node1_idx, node2_idx, expected_elements):
    sll = create_list(elements)
    node1 = node2 = sll.head
    for _ in range(node1_idx):
        node1 = node1.next_node
    for _ in range(node2_idx):
        node2 = node2.next_node

    sll.swapTwoNodes(node1, node2)
    expected_sll = create_list(expected_elements)
    assert sll == expected_sll
