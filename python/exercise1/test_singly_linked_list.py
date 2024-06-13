import pytest
from .singly_linked_list import SinglyLinkedList


def create_list(elements):
    sll = SinglyLinkedList()
    for element in elements:
        sll.add_last(element)
    return sll


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
    sll = create_list(elements)
    node1 = node2 = sll.head
    for _ in range(node1_idx):
        node1 = node1.next_node
    for _ in range(node2_idx):
        node2 = node2.next_node

    sll.swap_two_nodes(node1, node2)
    expected_sll = create_list(expected_elements)
    assert sll == expected_sll
