from collections import defaultdict
from enum import Enum
from node import Node
from typing import Generator, Generic, TypeVar


T = TypeVar("T")


class GraphSearchType(Enum):
    depthFirst = 0
    breadthFirst = 1


class Graph(Generic[T]):
    __nodes: list[Node[T]]

    def __init__(
        self,
        nodes: list[Node[T]] = [],
    ) -> None:
        super().__init__()

        # init nodes to an empty list
        self.__nodes = nodes

    def search(
        self,
        searchType: GraphSearchType,
    ) -> Generator[T, None, None]:
        match searchType:
            case GraphSearchType.depthFirst:
                yield from self.__depthFirstSearch(self.__nodes[0])
            case GraphSearchType.breadthFirst:
                yield from self.__breadthFirstSearch(self.__nodes[0])

    def __depthFirstSearch(
        self,
        node: Node[T],
        visited: defaultdict[Node[T], bool] = defaultdict(),
    ) -> Generator[T, None, None]:
        # return nothing if this node has already been visited
        if visited.get(node) == True:
            return

        # set this node as visited so it won't be visited again
        visited[node] = True

        # yield the node's data
        yield node.data
        # then do the same with all the node's connections recursively
        for connection in node.connections:
            yield from self.__depthFirstSearch(self.__nodes[connection[0]])

    def __breadthFirstSearch(
        self,
        node: Node[T],
    ) -> Generator[T, None, None]:

        visited = defaultdict[Node[T], bool]()
        bfsQueue = list[Node[T]]()
        bfsQueue.append(node)

        while len(bfsQueue) > 0:
            node = bfsQueue.pop()
            
            # return nothing if this node has already been visited
            if visited.get(node) == True:
                pass
            else:
                # set this node as visited so it won't be visted again
                visited[node] = True
                yield node.data

                for connection in node.connections:
                    bfsQueue.append(self.__nodes[connection[0]])


if __name__ == "__main__":
    a = Graph[int](
        [
            Node.withoutWeights(0, [1, 2, 3]),
            Node.withoutWeights(1, [0, 2, 3]),
            Node.withoutWeights(2, [0, 1, 4]),
            Node.withoutWeights(3, [0, 1]),
            Node.withoutWeights(4, [2]),
        ]
    )

    # for c in a.search(GraphSearchType.depthFirst):
        # print(c)

    for c in a.search(GraphSearchType.breadthFirst):
        print(c)
