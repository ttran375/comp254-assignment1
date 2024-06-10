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


@pytest.mark.parametrize(
    "elements,node1_idx,node2_idx,expected_elements",
    [
        ([1, 2, 3, 4, 5], 1, 3, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 0, 4, [5, 2, 3, 4, 1]),
        ([1, 2, 3, 4, 5], 2, 2, [1, 2, 3, 4, 5]),
        ([1, 2, 3], 0, 1, [2, 1, 3]),
        ([1, 2, 3], 1, 2, [1, 3, 2]),
        ([10, 20, 30, 40], 0, 2, [30, 20, 10, 40]),
        ([10, 20, 30, 40], 2, 3, [10, 20, 40, 30]),
        ([5, 6, 7, 8, 9], 1, 4, [5, 9, 7, 8, 6]),
        ([5, 6, 7, 8, 9], 0, 3, [8, 6, 7, 5, 9]),
        ([5, 6, 7, 8, 9], 0, 1, [6, 5, 7, 8, 9]),
        ([5, 6, 7, 8, 9], 2, 4, [5, 6, 9, 8, 7]),
        ([100, 200, 300, 400], 1, 3, [100, 400, 300, 200]),
        ([100, 200, 300, 400], 0, 1, [200, 100, 300, 400]),
        ([100, 200, 300, 400], 1, 2, [100, 300, 200, 400]),
        ([10, 20], 0, 1, [20, 10]),
        ([10], 0, 0, [10]),
        ([1, 2, 3, 4, 5, 6], 1, 4, [1, 5, 3, 4, 2, 6]),
        ([1, 2, 3, 4, 5, 6], 2, 5, [1, 2, 6, 4, 5, 3]),
        ([1, 2, 3, 4, 5, 6], 0, 5, [6, 2, 3, 4, 5, 1]),
        ([2, 4, 6, 8, 10], 1, 3, [2, 8, 6, 4, 10]),
        ([2, 4, 6, 8, 10], 0, 2, [6, 4, 2, 8, 10]),
        ([2, 4, 6, 8, 10], 2, 4, [2, 4, 10, 8, 6]),
        ([1, 3, 5, 7, 9], 0, 4, [9, 3, 5, 7, 1]),
        ([1, 3, 5, 7, 9], 1, 3, [1, 7, 5, 3, 9]),
        ([1, 3, 5, 7, 9], 2, 4, [1, 3, 9, 7, 5]),
        (["A", "B", "C", "D", "E"], 1, 3, ["A", "D", "C", "B", "E"]),
        (["A", "B", "C", "D", "E"], 0, 4, ["E", "B", "C", "D", "A"]),
        (["A", "B", "C", "D", "E"], 2, 2, ["A", "B", "C", "D", "E"]),
        (["A", "B", "C"], 0, 1, ["B", "A", "C"]),
        (["A", "B", "C"], 1, 2, ["A", "C", "B"]),
        (["X", "Y", "Z"], 0, 2, ["Z", "Y", "X"]),
        (["X", "Y", "Z"], 1, 2, ["X", "Z", "Y"]),
        (["foo", "bar", "baz"], 0, 1, ["bar", "foo", "baz"]),
        (["foo", "bar", "baz"], 1, 2, ["foo", "baz", "bar"]),
        (["red", "blue", "green"], 0, 2, ["green", "blue", "red"]),
        (["red", "blue", "green"], 1, 2, ["red", "green", "blue"]),
        (
            ["alpha", "beta", "gamma", "delta"],
            0,
            3,
            ["delta", "beta", "gamma", "alpha"],
        ),
        (
            ["alpha", "beta", "gamma", "delta"],
            1,
            2,
            ["alpha", "gamma", "beta", "delta"],
        ),
        (["one", "two", "three", "four"], 0, 3, ["four", "two", "three", "one"]),
        (["one", "two", "three", "four"], 1, 3, ["one", "four", "three", "two"]),
        (
            ["apple", "banana", "cherry", "date"],
            0,
            2,
            ["cherry", "banana", "apple", "date"],
        ),
        (
            ["apple", "banana", "cherry", "date"],
            1,
            3,
            ["apple", "date", "cherry", "banana"],
        ),
        (["cat", "dog", "fish", "bird"], 0, 3, ["bird", "dog", "fish", "cat"]),
        (["cat", "dog", "fish", "bird"], 2, 3, ["cat", "dog", "bird", "fish"]),
        (["this", "is", "a", "test"], 0, 3, ["test", "is", "a", "this"]),
        (["this", "is", "a", "test"], 1, 2, ["this", "a", "is", "test"]),
        (
            ["test", "case", "with", "strings"],
            0,
            2,
            ["with", "case", "test", "strings"],
        ),
        (
            ["test", "case", "with", "strings"],
            1,
            3,
            ["test", "strings", "with", "case"],
        ),
        (["python", "java", "c++", "rust"], 0, 3, ["rust", "java", "c++", "python"]),
        (["python", "java", "c++", "rust"], 1, 2, ["python", "c++", "java", "rust"]),
    ],
)
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
