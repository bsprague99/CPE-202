# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz IV
# Term:         Winter 2021


##############################################################################
# IMPORTANT: By taking this quiz, you agree not to discuss its contents with #
# any other student who has yet to take it, in this or future terms.         #
#                                                                            #
# Violation of this agreement will constitute cheating and may result in     #
# retroactive course failure, as well as other disciplinary action.          #
##############################################################################


##################################################
# Submit Command: /home/dkauffma/casey 202 quiz4 #  <- Don't ask me for this!
##################################################


###############################################################################
# This quiz will assess your understanding of trees and graphs.               #
# Any additional functions written will also require 5 test cases.            #
###############################################################################


from typing import List


def is_tree(adj_list: List[List[int]]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) is a tree
    and False otherwise. Assume the graph is acyclic and that there is only one
    component (all vertices are connected by one or more edges).

    In addition to needing to be acyclic (which is given), a graph is a tree if:
    - There exists only directed (one-way) edges
    - Each vertex has exactly one parent (except the root, which has none)

    >>> adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
    >>> is_tree(adj_list)
    True
    """
    traversed = []
    for i in range(len(adj_list)):

        for x in range(len(adj_list[i])):

            if adj_list[i][x] in traversed:
                return False

            traversed.append(adj_list[i][x])

    return True


def get_height(adj_list: List[List[int]]) -> int:
    """
    Return the height (length of the longest path from the root) of the given
    tree (represented as an adjacency list). Let a single-vertex tree have a
    height of zero and an empty tree a height of -1.

    Do not create a class to solve this problem; traverse the adjacency list.

    >>> adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
    >>> get_height(adj_list)
    2
    """
    if len(adj_list) == 0:
        return -1
    if len(adj_list) == 1:
        return 0
    x = 0
    extra: list = []
    root = find_root(adj_list, x)
    path = order_dfs(adj_list, root, extra)
    for i in path:
        temp = order_dfs(adj_list, i, extra)
        if len(temp) == 1:
            return x
        x += 1
    return x


def find_root(adj_list: List[List[int]], x: int) -> int:
    temp = []
    element: int = 0
    for i in range(len(adj_list)):

        if x in adj_list[i]:
            temp.append(i)

    if len(temp) == 1:
        return find_root(adj_list, temp[element])

    elif len(temp) == 0:
        return x


def order_dfs(adj_list: List[List[int]], start: int, explored: List[int]) \
                                                             -> List[int]:
    if len(adj_list) == 0:
        return []

    if start not in explored:
        explored.append(start)

        for ref in adj_list[start]:
            order_dfs(adj_list, ref, explored)

    return explored
