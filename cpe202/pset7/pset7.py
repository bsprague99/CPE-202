# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Winter 2021

from typing import List


def to_adj_matrix(adj_list: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency list, return its equivalent adjacency matrix, in which
    each inner list represents a row in the matrix, with a 0 or 1 in the row
    indicating whether a directed edge does not or does exist, respectively,
    between the row vertex to the column vertex.

    >>> to_adj_matrix([[1, 2], [0, 2], [0, 1]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    """
    if len(adj_list) == 0:
        return None

    v = max(adj_list)
    if v:
        size = max(v) + 1
    else:
        size = len(adj_list)

    newMatrix = [[0 for j in range(size)]
                 for i in range(size)]
    for i in range(len(adj_list)):
        for j in adj_list[i]:
            newMatrix[i][j] = 1
    return newMatrix


def to_adj_list(adj_matrix: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency matrix, return its equivalent adjacency list, in which
    each inner list represents all vertex labels for which the vertex at that
    index has a directed edge. For example, the first inner list contains all
    vertex labels for which Vertex 0 has a directed edge.

    >>> to_adj_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    [[1, 2], [0, 2], [0, 1]])
    """
    size = len(adj_matrix)
    newList: List[List[int]] = []
    for i in range(size):
        newList.append([])

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                newList[i].append(j)
    return newList


def order_bfs(adj_list: List[List[int]], start: int) -> List[int]:
    """
    Return a list of unique vertex labels from the given graph representing a
    breadth-first traversal of the graph starting at the specified vertex (with
    lower-numbered vertices chosen before higher-numbered vertices).

    >>> order_bfs([[1, 2], [0, 3], [0, 3], [1, 2]], 3)
    [3, 1, 2, 0]
    """
    if len(adj_list) == 0:
        return None

    queue = [start]
    result = [start]

    while len(queue) != 0:
        item = queue.pop(0)
        for i in adj_list[item]:
            if i not in result:
                result.append(i)
                queue.append(i)

    return result


def order_dfs(adj_list: List[List[int]], start: int,
              explored: List[int]) -> List[int]:
    """
    Return a list of unique vertex labels from the given adjacency list
    representing a depth-first traversal of the graph starting at the specified
    vertex (with lower-numbered vertices chosen over higher-numbered vertices).
    The explored argument may be used as an accumulator and will initially be
    an empty list.

    >>> order_dfs([[1, 2], [0, 3], [0, 3], [1, 2]], 2, [])
    [2, 0, 1, 3]
    """
    if len(adj_list) == 0:
        return None
    if start not in explored:
        explored.append(start)
        for ref in adj_list[start]:
            order_dfs(adj_list, ref, explored)
    return explored


def has_cycle(adj_list: List[List[int]], start: int, path: List[int]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) has a
    cycle and False otherwise. A graph has a cycle if there exists a path of
    unique edges that start and end at the same vertex.

    >>> has_cycle([[1, 2], [0, 3], [0, 3], [1, 2]], 0, [])  # square
    True
    >>> has_cycle([[1, 2], [], []], 0, [])  # tree
    False
    """
    if len(adj_list) == 0:
        return False
    index = start
    path.append(start)
    for child in adj_list[start]:
        if child in path and child != index:
            return True
        return has_cycle(adj_list, child, path) or False
    return False


def count_components(adj_list: List[List[int]]) -> int:
    """
    Return the number of components in the given graph (represented as an
    adjacency list). A component is defined as a subgraph of vertices in which
    no vertex in the subgraph has a path (a sequence of edges) to a vertex
    outside the subgraph.

    >>> count_components([[1], [0], [3], [2], [5], [4]])
    3
    """
    discover = [0 for k in range(len(adj_list))]
    temp = 0

    for i in range(len(adj_list)):
        if discover[i] == 0:
            discover[i] = 1
            count = order_dfs(adj_list, i, [])
            temp += 1
        for k in count:
            discover[k] = 1

    return temp
