from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    data: T
    connections: list[tuple[int, Optional[float]]]

    def __init__(
        self,
        data: T,
        connections: list[
            tuple[int, Optional[float]]
        ] = [],  # item 0 is the index of the other node, item 1 is the edge weight
    ) -> None:
        """Constructor for a binary tree node.

        Args:
            data (T): This node's data.
            connections (list[int], optional): The list of pointers that are connections of this node. Defaults to an emply list[int]().
        """
        self.data = data
        self.connections = connections

    @staticmethod
    def withoutWeights(
        data: T,
        connections: list[int] = [],
    ) -> "Node[T]":
        """Constructor for a binary tree node.

        Args:
            data (T): This node's data.
            connections (list[int], optional): The list of pointers that are connections of this node. Defaults to an emply list[int]().
        """

        connectionsWithWeights = list[tuple[int, Optional[float]]]()

        # add connections with no edge weights
        for connection in connections:
            connectionsWithWeights.append((connection, None))

        return Node(data, connectionsWithWeights)
