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
        (["a", "b", "c", "d", "e"], 0, 4, ["e", "b", "c", "d", "a"]),
        (["a", "b", "c", "d", "e"], 1, 3, ["a", "d", "c", "b", "e"]),
        (["apple", "banana", "cherry"], 0, 2, ["cherry", "banana", "apple"]),
        (["apple", "banana", "cherry"], 1, 2, ["apple", "cherry", "banana"]),
        (["one", "two", "three", "four"], 0, 1, ["two", "one", "three", "four"]),
        (["one", "two", "three", "four"], 2, 3, ["one", "two", "four", "three"]),
        (
            ["alpha", "beta", "gamma", "delta"],
            1,
            3,
            ["alpha", "delta", "gamma", "beta"],
        ),
        (
            ["alpha", "beta", "gamma", "delta"],
            0,
            2,
            ["gamma", "beta", "alpha", "delta"],
        ),
        (["cat", "dog", "fish"], 0, 2, ["fish", "dog", "cat"]),
        (["cat", "dog", "fish"], 1, 2, ["cat", "fish", "dog"]),
        (["red", "blue", "green"], 0, 1, ["blue", "red", "green"]),
        (["red", "blue", "green"], 1, 2, ["red", "green", "blue"]),
        (["x", "y", "z"], 0, 2, ["z", "y", "x"]),
        (["x", "y", "z"], 1, 2, ["x", "z", "y"]),
        (["first", "second", "third"], 0, 2, ["third", "second", "first"]),
        (["first", "second", "third"], 1, 2, ["first", "third", "second"]),
        (["foo", "bar", "baz"], 0, 1, ["bar", "foo", "baz"]),
        (["foo", "bar", "baz"], 1, 2, ["foo", "baz", "bar"]),
        (["hello", "world"], 0, 1, ["world", "hello"]),
        (["single"], 0, 0, ["single"]),
        (["this", "is", "a", "test"], 1, 3, ["this", "test", "a", "is"]),
        (["this", "is", "a", "test"], 0, 2, ["a", "is", "this", "test"]),
        (
            ["test", "case", "with", "strings"],
            1,
            2,
            ["test", "with", "case", "strings"],
        ),
        (["python", "java", "c++", "rust"], 0, 3, ["rust", "java", "c++", "python"]),
        (["python", "java", "c++", "rust"], 2, 3, ["python", "java", "rust", "c++"]),
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
