import pytest
from circularly_linked_list import CircularlyLinkedList


@pytest.mark.parametrize(
    "elements",
    [
        ([], "[]"),
        (["A"], "[A]"),
        (["A", "B", "C"], "[A, B, C]"),
        (["1"], "[1]"),
        ([1, 2, 3], "[1, 2, 3]"),
        ([None], "[None]"),
        ([True, False], "[True, False]"),
        (["long string with spaces"], "[long string with spaces]"),
        (["A", "A", "A"], "[A, A, A]"),
        ([1.1, 2.2, 3.3], "[1.1, 2.2, 3.3]"),
        ([1, "A", True, None], "[1, A, True, None]"),
        ([[], {}, set()], "[[], {}, set()]"),
        (["\n", "\t", " "], "[\n, \t,  ]"),
        (["A", None, "B"], "[A, None, B]"),
        ([1, [2, 3], 4], "[1, [2, 3], 4]"),
        (["日本語", "English", "Español"], "[日本語, English, Español]"),
        (["abc", "def", "ghi"], "[abc, def, ghi]"),
        ([0, 0, 0], "[0, 0, 0]"),
        ([10**5, 10**10, 10**15], "[100000, 10000000000, 1000000000000000]"),
        (["", "Non-empty", ""], "[, Non-empty, ]"),
        (["A", 123, 45.67, None], "[A, 123, 45.67, None]"),
        ([float("inf"), float("-inf"), float("nan")], "[inf, -inf, nan]"),
        (["A", "B", "C", "D", "E"], "[A, B, C, D, E]"),
        (
            ["short", "a bit longer", "the longest string in the list"],
            "[short, a bit longer, the longest string in the list]",
        ),
        ([b"bytes", b"more bytes"], "[b'bytes', b'more bytes']"),
        (["special char: @#$%^&*()"], "[special char: @#$%^&*()]"),
        ([range(3)], "[range(0, 3)]"),
        (["tuple", (1, 2), (3, 4)], "[tuple, (1, 2), (3, 4)]"),
        ([dict(a=1, b=2)], "[{'a': 1, 'b': 2}]"),
        ([{"nested": {"dict": "example"}}], "[{'nested': {'dict': 'example'}}]"),
        ([set([1, 2, 3]), frozenset([4, 5, 6])], "[{1, 2, 3}, frozenset({4, 5, 6})]"),
        ([complex(1, 1), complex(2, 2)], "[(1+1j), (2+2j)]"),
        ([True, False, True, False], "[True, False, True, False]"),
        ([1, 2.2, "3", [4], (5,)], "[1, 2.2, 3, [4], (5,)]"),
        ([{"a": [1, 2], "b": (3, 4)}], "[{'a': [1, 2], 'b': (3, 4)}]"),
        ([3.14, 2.718, 1.618], "[3.14, 2.718, 1.618]"),
        ([Ellipsis, NotImplemented], "[Ellipsis, NotImplemented]"),
        ([{"set"}, {"of"}, {"dictionaries"}], "[{'set'}, {'of'}, {'dictionaries'}]"),
        ([float("nan")], "[nan]"),
        (
            ["First", "Second", "Third", "Fourth", "Fifth"],
            "[First, Second, Third, Fourth, Fifth]",
        ),
        ([3 + 4j, 5 - 6j, -7 + 8j], "[(3+4j), (5-6j), (-7+8j)]"),
        ([0.1, 0.2, 0.3], "[0.1, 0.2, 0.3]"),
        (["unicode"], "[unicode]"),
        ([bytearray(b"byte array")], "[bytearray(b'byte array')]"),
        ([slice(1, 10, 2)], "[slice(1, 10, 2)]"),
        (
            [{"key": "value"}, {"another_key": "another_value"}],
            "[{'key': 'value'}, {'another_key': 'another_value'}]",
        ),
        ([None, None, None], "[None, None, None]"),
        (["", "", ""], "[, , ]"),
        ([[], [], []], "[[], [], []]"),
        ([{}, {}, {}], "[{}, {}, {}]"),
    ],
)
def test_clone(elements):
    input_elements, expected_str = elements

    # Create the original list
    original_list = CircularlyLinkedList()
    for element in input_elements:
        original_list.add_last(element)

    # Clone the list
    cloned_list = original_list.clone()

    # Check that the cloned list has the same elements
    assert str(cloned_list) == expected_str

    # Check that the cloned list is a separate object
    if input_elements:
        assert original_list is not cloned_list
        assert str(original_list) == expected_str
        assert cloned_list.tail is not original_list.tail
        current_original = original_list.tail.next_node
        current_cloned = cloned_list.tail.next_node
        while current_original != original_list.tail:
            assert current_original is not current_cloned
            current_original = current_original.next_node
            current_cloned = current_cloned.next_node
        # Check the tail nodes separately
        assert current_original is not current_cloned


# Run tests
if __name__ == "__main__":
    pytest.main()
