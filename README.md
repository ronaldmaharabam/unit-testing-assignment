# Binary Search Tree (BST) Unit Testing
This repository contains a simple implementation of a Binary Search Tree (BST) in Python, and a simple unit testing implementation using pytest.

## BinarySearchTree.py
The *BinarySearchTree.py file* contains the implementation of a Binary Search Tree. The key features include:

- Insertion of keys into the BST.
- Searching for keys in the BST.

### Usage

Insertion:
\
To insert a key into the BST, use the insert method:
```python
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
```

Search: 
\
To search for a key in the BST, use the search method:

```python
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)

result = bst.search(3)
if result:
    print(f"Key 3 found in the BST.")
else:
    print(f"Key 3 not found in the BST.")
```
# Running Tests
This project includes tests to ensure the correctness of the insert and search operations. To run the tests, execute the following command:

```bash
pytest test_BinarySearchTree.py
```
Ensure that pytest is installed in your Python environment before running the tests.