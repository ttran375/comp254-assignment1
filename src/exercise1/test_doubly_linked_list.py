import pytest
from .doubly_linked_list import DoublyLinkedList


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


@pytest.mark.parametrize(
    "elements,node1_idx,node2_idx,expected_elements",
    [
        ([1, 2, 3, 4, 5], 1, 3, [1, 4, 3, 2, 5]),
        ([1, 2, 3], 0, 1, [2, 1, 3]),
        (["A", "B", "C", "D", "E"], 1, 3, ["A", "D", "C", "B", "E"]),
        (
            ["alpha", "beta", "gamma", "delta"],
            0,
            3,
            ["delta", "beta", "gamma", "alpha"],
        ),
        ([1, 2, 3, 4], 0, 3, [4, 2, 3, 1]),
        ([1, 2, 3, 4], 1, 3, [1, 4, 3, 2]),
        ([1, 2, 3, 4], 2, 3, [1, 2, 4, 3]),
        (["a", "b", "c", "d", "e"], 0, 4, ["e", "b", "c", "d", "a"]),
        (["a", "b", "c", "d", "e"], 1, 3, ["a", "d", "c", "b", "e"]),
        ([1, 2], 0, 1, [2, 1]),
        ([1], 0, 0, [1]),
        ([], 0, 0, []),
        ([1, 2, 3], 0, 2, [3, 2, 1]),
        ([1, 2, 3], 1, 2, [1, 3, 2]),
        ([True, False, None], 0, 2, [None, False, True]),
        ([1.1, 2.2, 3.3], 0, 2, [3.3, 2.2, 1.1]),
        ([1, None, True], 1, 2, [1, True, None]),
        ([None, "x", True], 0, 2, [True, "x", None]),
        ([1, 2, 3, 4, 5, 6], 0, 5, [6, 2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5, 6], 2, 5, [1, 2, 6, 4, 5, 3]),
        (["cat", "dog", "bird"], 1, 2, ["cat", "bird", "dog"]),
        (["red", "green", "blue"], 0, 2, ["blue", "green", "red"]),
        ([10, 20, 30, 40], 1, 3, [10, 40, 30, 20]),
        ([None, 1, 2], 0, 1, [1, None, 2]),
        ([None, 1, 2], 1, 2, [None, 2, 1]),
        ([None, 1, 2], 0, 2, [2, 1, None]),
        ([1, 1, 1], 0, 2, [1, 1, 1]),
        ([1, 1, 1], 0, 1, [1, 1, 1]),
        ([1, 1, 1], 1, 2, [1, 1, 1]),
        ([True, False], 0, 1, [False, True]),
        ([True, False, None], 1, 2, [True, None, False]),
        ([True, False, None], 0, 2, [None, False, True]),
        ([True, False, None], 0, 1, [False, True, None]),
        ([1, 2, 3, 4, 5, 6], 1, 4, [1, 5, 3, 4, 2, 6]),
        ([1, 2, 3, 4, 5, 6], 0, 4, [5, 2, 3, 4, 1, 6]),
        ([1, 2, 3, 4, 5, 6], 1, 3, [1, 4, 3, 2, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 0, 3, [4, 2, 3, 1, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 1, 2, [1, 3, 2, 4, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 2, 3, [1, 2, 4, 3, 5, 6]),
        ([1, 2, 3, 4, 5, 6], 4, 5, [1, 2, 3, 4, 6, 5]),
        ([-1, -2, -3, -4], 0, 3, [-4, -2, -3, -1]),
        ([0, 1, 2, 3], 0, 3, [3, 1, 2, 0]),
        ([0, 1, 2, 3], 1, 3, [0, 3, 2, 1]),
        ([0, 1, 2, 3], 2, 3, [0, 1, 3, 2]),
        ([0, 1, 2, 3], 0, 2, [2, 1, 0, 3]),
        ([0, 1, 2, 3], 1, 2, [0, 2, 1, 3]),
        ([float("inf"), float("-inf")], 0, 1, [float("-inf"), float("inf")]),
        ([None, "a", True], 0, 2, [True, "a", None]),
        ([1, 2, 3, 4, 5, 6, 7], 0, 6, [7, 2, 3, 4, 5, 6, 1]),
        (["x", "y", "z", "a", "b"], 2, 3, ["x", "y", "a", "z", "b"]),
    ],
)
def test_swap_two_nodes(elements, node1_idx, node2_idx, expected_elements):
    dll = create_doubly_linked_list(elements)
    node1 = get_node_by_index(dll, node1_idx)
    node2 = get_node_by_index(dll, node2_idx)

    dll.swap_two_nodes(node1, node2)
    expected_dll = create_doubly_linked_list(expected_elements)

    current_expected = expected_dll.head
    current_actual = dll.head

    while current_expected is not None:
        assert current_expected.data == current_actual.data
        current_expected = current_expected.next
        current_actual = current_actual.next

    assert current_actual is None
    assert current_expected is None
