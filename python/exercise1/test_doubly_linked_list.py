import pytest
from doubly_linked_list import DoublyLinkedList


def create_list_with_nodes(data_list):
    dll = DoublyLinkedList()
    nodes = []
    for data in data_list:
        dll.add_node(data)
        nodes.append(dll.tail)
    return dll, nodes


@pytest.mark.parametrize(
    "initial_data, idx1, idx2, expected_data",
    [
        (["A", "B", "C", "D"], 1, 3, ["A", "D", "C", "B"]),
        (["A", "B", "C", "D"], 0, 2, ["C", "B", "A", "D"]),
        (["A", "B", "C", "D"], 1, 1, ["A", "B", "C", "D"]),
        (["A", "B", "C", "D"], 2, 3, ["A", "B", "D", "C"]),
        (["A", "B", "C"], 0, 2, ["C", "B", "A"]),
    ]
)
def test_swapTwoNodes(initial_data, idx1, idx2, expected_data):
    dll, nodes = create_list_with_nodes(initial_data)
    dll.swapTwoNodes(nodes[idx1], nodes[idx2])

    current = dll.head
    result = []
    while current:
        result.append(current.data)
        current = current.next

    assert result == expected_data
