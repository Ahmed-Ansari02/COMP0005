"""
Python program to implement insert operation
in Red Black Tree.
"""
from typing import Any
import enum


class Color(enum.Enum):
    """Enums for the colors"""

    RED = True
    BLACK = False


class Node:
    def __init__(self, value: Any):
        self.val: Any = value
        self.color: Color = Color.RED
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node(val={self.val}, color={self.color.value}, left={self.left}, right={self.right})"


class RBT:
    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> None:
        """Insertion and updation of root"""
        self.root = self.__insert(self.root, value)
        self.root.color = Color.BLACK

    def __insert(self, root: Node, val: Any) -> Node:
        """Recursive insertion of the root"""
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self.__insert(root.left, val)
        elif val > root.val:
            root.right = self.__insert(root.right, val)
        else:
            root.val = val

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)

        return root

    @staticmethod
    def is_red(node: Node) -> bool:
        if node is None:
            return False
        return node.color == Color.RED

    @staticmethod
    def flip_color(node: Node) -> None:
        """Flips the color if both left and right child are RED"""
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK

    def rotate_left(self, node: Node) -> Node:
        """Rotate the node left send the new node
            if the right node is Red
        Args:
            node: The node which has a Red node on Right
        Returns: the rotated new node
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = Color.RED
        print("Left Rotation !!")
        return new_root

    def rotate_right(self, node: Node) -> Node:
        """Rotate the node right send the new node
            if the left node is Red and left of left is Red
        Args:
            node: The node which has both left child and left of left child Red
        Returns: the rotated new node
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = Color.RED
        print("Right Rotation !!")
        return new_root

    def inorder(self) -> None:
        """Inorder Traversal for root"""
        self.__inorder(self.root)

    def __inorder(self, root: Node) -> None:
        """Recursive Inorder Traversal for any node"""
        if root is None:
            return
        self.__inorder(root.left)
        print(root.val, end=" ")
        self.__inorder(root.right)
    

if __name__ == "__main__":
    """
    LLRB tree made after all insertions are made.
 
    1. Nodes which have double INCOMING edge means
       that they are RED in color.
    2. Nodes which have single INCOMING edge means
       that they are BLACK in color.
         
            root
             |
             40
           //  \
          20    50
         /  \
        10    30
            //
           25 
    """

    tree = RBT()

    file = open("./test3-dickens.txt", "r")
    test_file = open("./test-search.txt", "r")
    for line in file:
        for word in line.split():
            tree.insert(word)



