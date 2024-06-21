import pytest
from .doubly_linked_list import DoublyLinkedList


def create_doubly_linked_list(elements):
    dll = DoublyLinkedList()
    for element in elements:
        dll.add_node(element)
    return dll


def get_elements(dll):
    elements = []
    current = dll.head
    while current is not None:
        elements.append(current.data)
        current = current.next
    return elements


@pytest.mark.parametrize(
    "elements1, elements2, expected_elements",
    [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [4, 5, 6], [4, 5, 6]),
        ([], [], []),
        (["a", "b", "c"], ["d", "e", "f"], ["a", "b", "c", "d", "e", "f"]),
        (["apple"], ["banana", "cherry"], ["apple", "banana", "cherry"]),
        ([1], [2], [1, 2]),
        ([None], [None], [None, None]),
        ([1, 2], [3, 4, 5], [1, 2, 3, 4, 5]),
        (["x", "y"], ["z"], ["x", "y", "z"]),
        ([""], [""], ["", ""]),
        ([True, False], [False, True], [True, False, False, True]),
        ([1.1, 2.2], [3.3, 4.4], [1.1, 2.2, 3.3, 4.4]),
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([1, 2, 3], [1, 2, 3], [1, 2, 3, 1, 2, 3]),
        ([None], [], [None]),
        ([], [None], [None]),
        ([1, 2, 3], [None], [1, 2, 3, None]),
        ([None], [1, 2, 3], [None, 1, 2, 3]),
        ([0], [0], [0, 0]),
        ([1, 2], ["a", "b"], [1, 2, "a", "b"]),
        (["a", "b"], [1, 2], ["a", "b", 1, 2]),
        ([1.5], [2.5], [1.5, 2.5]),
        ([1], [1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([1, 1, 1, 1], [1], [1, 1, 1, 1, 1]),
        ([1], [None, 2, 3], [1, None, 2, 3]),
        ([None, 2, 3], [1], [None, 2, 3, 1]),
        ([None, "x"], [True, 2.5], [None, "x", True, 2.5]),
        ([1, 2.2, "a"], [None, False], [1, 2.2, "a", None, False]),
        ([], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [], [1, 2, 3, 4, 5]),
        ([1, "a", None], [2, "b", True], [1, "a", None, 2, "b", True]),
        ([1], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 4, 5, 6], [1], [1, 2, 3, 4, 5, 6, 1]),
        ([None, None], [None, None], [None, None, None, None]),
        ([1], [None, None], [1, None, None]),
        ([None, None], [1], [None, None, 1]),
        ([1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]),
        ([1, "two"], [3.0, True], [1, "two", 3.0, True]),
        ([1, 2], [1, 2], [1, 2, 1, 2]),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        (
            ["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
            ["a", "b", "c", "d", "e", "f", "g", "h"],
        ),
        ([1, 2, 3], ["a", "b", "c"], [1, 2, 3, "a", "b", "c"]),
        ([None, 1, "a"], [None, 2, "b"], [None, 1, "a", None, 2, "b"]),
        ([True, False], [False, True, True], [True, False, False, True, True]),
        ([], [1, None, True, "x"], [1, None, True, "x"]),
        ([1, None, True, "x"], [], [1, None, True, "x"]),
        ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
        ([-1, -2, -3], [-4, -5, -6], [-1, -2, -3, -4, -5, -6]),
        ([float("inf"), float("-inf")], [0], [float("inf"), float("-inf"), 0]),
    ],
)
def test_concatenate(elements1, elements2, expected_elements):
    dll1 = create_doubly_linked_list(elements1)
    dll2 = create_doubly_linked_list(elements2)

    dll1.concatenate(dll2)

    assert get_elements(dll1) == expected_elements
