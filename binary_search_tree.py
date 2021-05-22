from comparable import Comparable
from typing import Optional, TypeVar, Generic


T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    value: Optional[T]
    leftChild: Optional["Node[T]"] = None
    rightChild: Optional["Node[T]"] = None

    def __init__(self, value: Optional[T] = None):
        self.value = value


class BinarySearchTree(Generic[T]):
    __root: Node[T]

    def __init__(self, rootNode: Optional[Node[T]] = None):
        if rootNode is not None:
            self.__root = rootNode
        else:
            self.__root = Node[T]()

    def _insertNode(self, node: Node[T], value: T):
        """Insert a node into the tree from a given node (recursive).

        Args:
            node (Node[T]): The node to start insertion from.
            value (T): The value to insert.
        """
        if node.value is None:
            # node hasn't been given a value
            # so set it as the given value
            node.value = value
        elif node.value >= value:
            # node value is greater than or equal to `value` so go left
            if node.leftChild is not None:
                # traverse the left subtree
                self._insertNode(node.leftChild, value)
            else:
                # set the left child to `value` bc leftChild is None
                node.leftChild = Node(value)
        elif node.value < value:
            # node value is less than `value` so go right
            if node.rightChild is not None:
                # traverse the right subtree
                self._insertNode(node.rightChild, value)
            else:
                # set the right child to `value` bc rightChild is None
                node.rightChild = Node(value)

    def insert(self, value: T):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self._insertNode(self.__root, value)

    def _findNode(self, node: Node[T], value: T) -> Optional[Node[T]]:
        if node.value is None:
            # node hasn't been given a value
            # so set it as the given value
            raise Exception("Empty tree; node nonexistent.")
        elif node.value == value:
            # found it!
            return node
        elif node.value > value:
            # node value is greater than `value` so go left
            if node.leftChild is not None:
                # traverse the left subtree
                return self._findNode(node.leftChild, value)
            else:
                # node does not exist
                raise Exception("Node does not exist in graph.")
        elif node.value < value:
            # node value is less than `value` so go right
            if node.rightChild is not None:
                # traverse the right subtree
                return self._findNode(node.rightChild, value)
            else:
                # node does not exist
                # raise an exception bc node does not exist
                raise Exception("Node does not exist in graph.")

    def find(self, value: T) -> Optional[Node[T]]:
        return self._findNode(self.__root, value)
