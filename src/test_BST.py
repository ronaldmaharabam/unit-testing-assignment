import pytest
from BST import BinarySearchTree

def test_insert_and_search():
    bst = BinarySearchTree()
    keys = [5, 3, 7, 2, 4, 6, 8]

    for key in keys:
        bst.insert(key)

    for key in keys:
        assert bst.search(key) is not None

    assert bst.search(10) is None

def test_insert_duplicates():
    bst = BinarySearchTree()
    keys = [5, 3, 7, 3, 2, 7, 4, 6, 8, 5]

    for key in keys:
        bst.insert(key)

    assert bst.search(3).key == 3
    assert bst.search(7).key == 7
    assert bst.search(5).key == 5

if __name__ == "__main__":
    pytest.main()
