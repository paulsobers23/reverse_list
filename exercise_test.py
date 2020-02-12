import pytest 
from exercise import Node, reverse

# @pytest.mark.skip(reason="not implemented yet")
def test_reverse():
    lst = Node(1, Node(2, Node(3, Node(4))))
    reversed_lst = reverse(lst)
    assert reversed_lst.data == 4
    assert reversed_lst.next.data == 3
    assert reversed_lst.next.next.data == 2
    assert reversed_lst.next.next.next.data == 1

