import pytest
from .singly_linked_list import SinglyLinkedList


def create_list(elements):
    sll = SinglyLinkedList()
    for element in elements:
        sll.add_last(element)
    return sll


@pytest.mark.parametrize(
    "list1_elements, list2_elements, expected_elements",
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
def test_concatenate(list1_elements, list2_elements, expected_elements):
    list1 = create_list(list1_elements)
    list2 = create_list(list2_elements)
    list1.concatenate(list2)
    expected_list = create_list(expected_elements)
    assert list1 == expected_list
