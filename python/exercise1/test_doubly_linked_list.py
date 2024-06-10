import pytest
from doubly_linked_list import DoublyLinkedList


def create_doubly_linked_list(elements):
    dll = DoublyLinkedList()
    for element in elements:
        dll.add_node(element)
    return dll


def get_node_by_index(dll, index):
    current = dll.head
    for _ in range(index):
        if current is not None:
            current = current.next
    return current


@pytest.mark.parametrize("elements,node1_idx,node2_idx,expected_elements", [
    (["A", "B", "C", "D", "E"], 1, 3, ["A", "D", "C", "B", "E"]),
    (["A", "B", "C", "D", "E"], 0, 4, ["E", "B", "C", "D", "A"]),
    (["A", "B", "C", "D", "E"], 2, 2, ["A", "B", "C", "D", "E"]),
])
def test_swap_two_nodes(elements, node1_idx, node2_idx, expected_elements):
    dll = create_doubly_linked_list(elements)
    node1 = get_node_by_index(dll, node1_idx)
    node2 = get_node_by_index(dll, node2_idx)

    dll.swapTwoNodes(node1, node2)
    expected_dll = create_doubly_linked_list(expected_elements)

    current_expected = expected_dll.head
    current_actual = dll.head

    while current_expected is not None:
        assert current_expected.data == current_actual.data
        current_expected = current_expected.next
        current_actual = current_actual.next

    assert current_actual is None
    assert current_expected is None
