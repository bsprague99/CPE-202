# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Final Exam
# Term:         Winter 2021

from typing import List, Optional, Tuple


##############################################################################
# IMPORTANT: By taking this exam, you agree not to discuss its contents with #
# any other student who has yet to take it, in this or future terms.         #
#                                                                            #
# Violation of this agreement will constitute cheating and may result in     #
# retroactive course failure, as well as other disciplinary action.          #
##############################################################################


######################################################
# Submit Command: /home/dkauffma/casey.exe 202 final #  <- Don't ask for this!
######################################################


class ListNode:  # do not modify

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: Optional["ListNode"]) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.ref == other.ref

    def __repr__(self) -> str:
        if self.ref is None:
            return str(self.val)
        return (str(self.val) + " " + str(self.ref)).strip()




##################################################
#                Multiple Choice                 #
# ---------------------------------------------- #
# When a problem's return statement contains an  #
# empty string, insert exactly one char into it. #
#                                                #
#  When a return statement contains one or more  #
#   underscores _, replace each underscore with  #
#                your answer(s).                 #
#                                                #
#     If you receive a NameError that states     #
#             name '_' is not defined            #
#  it means you did not replace all underscores  #
#                for that problem.               #
#                                                #
#   When a problem contains multiple parts, all  #
# parts must be attempted to receive any credit  #
# for that problem. An error will be display for #
#     each such problem that is incomplete.      #
##################################################


def time_complexity_1() -> List[str]:
    """
    For each empty string "", insert a character A through E, each of which
    corresponds to a worst-case runtime, as shown below.

    [A] O(1)
    [B] O(log n)
    [C] O(n)
    [D] O(n log n)
    [E] none of the above

    Enter only one character each. The first answer is provided for you as an
    example.
    """
    return [
        # EXAMPLE: perform bubble sort on random data
        "E",

        # insert to binary heap
        "B",

        # remove from binary heap
        "B",

        # find value in binary heap
        "C",

        # create binary heap of size N
        "B",

        # remove node from BST
        "C",

        # perform merge sort on random data
        "D",

        # find highest value in hash table
        "C",

        # remove value from hash table
        "C",

        # insert to middle of linked list
        "E",

        # enqueue to FIFO queue
        "A",

        # insert to beginning of linked list
        "A",

        # find value in BST
        "C"
    ]




def time_complexity_2() -> str:
    """
    What is the Big-O time complexity of the function zignog below? Assume that
    the Python len and insert functions run in constant time.

    Return a character A through F, each of which corresponds to a worst-case
    runtime, as shown below.

    [A] O(1)
    [B] O(log n)
    [C] O(n)
    [D] O(n log n)
    [E] O(n^2)
    [F] none of the above
    """
    def zignog(n):
        ints = []
        for i in range(n + 4):
            ints.insert(max(0, len(ints) - 3), i / 4)
        return ints

    return "C"  # <- insert character in string




def time_complexity_3() -> str:
    """
    What is the Big-O time complexity of the function test_queue below? Assume
    that the Python append and pop functions run in constant time.

    Return a character A through F, each of which corresponds to a worst-case
    runtime, as shown below.

    [A] O(1)
    [B] O(log n)
    [C] O(n)
    [D] O(n log n)
    [E] O(n^2)
    [F] none of the above
    """
    def test_queue(n):
        queue = []
        for i in range(n):
            queue.append(i)
        ints = []
        for i in range(n):
            ints.append(queue.pop(0))
        return ints

    return "C"  # <- insert character in string




def binary_trees_1() -> str:
    """
    Which of the following trees are valid BSTs?

    Return a character A through F, each of which corresponds to one or more of
    the options below.

    (1) 
          52
       /      \
      39      65
     / \     /  \
    33  46  58  72
       /  \   \   \
      41  49  67  76


    (2) 
          43
       /      \
      22      57
     / \     /  \
    11  33  48  64
       /      \
      28      52


    (3) 
          37
       /      \
      27      49
     / \     /  \
    18  29  42  57
      \   \   \   \
      22  33  44  62


    [A] 1 and 2
    [B] 1 and 3
    [C] 2 and 3
    [D] 1 only
    [E] 1, 2, and 3
    [F] none of the above
    """

    return "C"  # <- insert character in string




def binary_trees_2() -> str:
    """
    Return a character A through F that completes the sentence below. 

    The motivation for balanced search tree structures, such as AVL trees, is
    to ensure that the performance of searches is:

    [A] O(1)
    [B] O(log n)
    [C] O(n)
    [D] O(n log n)
    [E] O(n^2)
    [F] none of the above
    """

    return "C"  # <- insert character in string




def ternary_search_tree() -> Tuple[int, bool]:
    """
    Consider a ternary search tree, in which each node contains two values and
    three children, with a similar ordering scheme (i.e. values in the middle
    child must be greater than the parent's first value and less than the
    parent's second value).

    Return a 2-tuple that contains an answer to both of the following questions.

    * What is the minimum number of levels required for a tree of eight values?
    * True or False: Searching for values in a ternary search tree would
                     generally be faster than in a binary search tree.
    """

    return (2, False)  # <- insert int in first position, bool in second position




def queues_1():
    """
    If the characters 'D', 'C', 'B', 'A' are placed in a queue (in that order)
    and then removed one at a time, in what order will they be removed?

    [A] ABCD
    [B] DCBA
    [C] DACB
    [D] undetermined

    Insert a character A through D that answers the question above.
    """

    return "A"  # <- insert character in string




def queues_2():
    """
    The behavior of a queue is referred to as:

    [A] FIFO
    [B] FILO
    [C] FIDO
    [D] LIFO

    Insert a character A through D that completes the sentence above.
    """

    return "A"  # <- insert character in string




def queues_3():
    """
    When working with graphs, a queue is a useful data structure for:

    [A] inserting a vertex into the graph
    [B] managing a depth-first search of the graph
    [C] managing a breadth-first search of the graph
    [D] finding edges in the graph

    Insert a character A through D that completes the sentence above.
    """

    return "C"  # <- insert character in string




def queues_4():
    """
    Suppose a novice developer (not someone who has completed CSC 202)
    implements a linked list version of a queue that uses the head of the list
    as the tail of the queue, but does not implement a reference to the tail
    of the list.

    Return a 2-tuple that contains an answer to both of the following questions.
    For each empty string "", insert a character A through F, each of which
    corresponds to a worst-case runtime, as shown below.

    * What will be the time complexity of enqueueing items?
    * What will be the time complexity of dequeueing items?

    [A] O(1)
    [B] O(log n)
    [C] O(n)
    [D] O(n log n)
    [E] O(n^2)
    [F] none of the above
    """

    return ("C", "E")  # <- insert enqueue option in first position,
                     #    insert dequeue option in second position




def queues_5() -> Tuple[int, int]:
    """
    Given the Queue class below, answer both questions regarding the function
    queue_know_it (below the Queue class). Assume all Queue methods are
    already properly implemented ('...' is used to represent each definition).

    Return a 2-tuple that contains an answer to both of the following questions.

    * What value is printed when queue_know_it is called?
    * By the end of queue_know_it, how many values remain in the queue?
    """
    class Queue:

        def empty_queue() -> "Queue":
            """Return an empty Queue"""
            ...

        def enqueue(q: "Queue", val: int) -> "Queue":
            """Add val to tail of queue and return updated queue."""
            ...

        def dequeue(q: "Queue") -> Tuple[int, "Queue"]:
            """Remove head of queue and return removed item and updated queue."""
            ...

    def queue_know_it(q: Queue) -> None:
        q = q.empty_queue()
        for i in range(6):
            q = q.enqueue(q, i + 1)
        for i in range(3):
            val, q = dequeue(q)
            val, q = dequeue(q)
            q = q.enqueue(q, val)
        val, q = dequeue(q)
        print(val)

    return (_, _)  # <- insert int printed in first position
                   #    insert queue size in second position




def hash_tables_1() -> str:
    """
    Which of the following expressions describes a perfect hashing function
    (no collisions) for a Python string |s| with these possible values:
    
        'Jane', 'Ken', 'William', 'Wyatt', 'Franklin', 'Flora', 'Enrico'

    In other words, given that |s| may be any of the above strings, which of
    the following expressions guarantees no values of |s| will result in the
    same hash key?

    [A] ord(s[len(s) - 1])
    [B] ord(s[0])
    [C] ord(s[1])
    [D] len(s)
    [E] none of the above
    """

    return "A"  # <- insert character in string




def hash_tables_2() -> Tuple[bool, str]:
    """
    Consider the hash function below and answer the following questions.

    * True or False: This is a legal implementation of a hash function.

    * What is the biggest problem with this function with respect to hashing?
        [A] it does not use its argument |s|
        [B] it returns a constant value
        [C] it does not have a hash table to access
        [D] it requires a hash table of length 18, which is not a prime number
        [E] none of the above
    """
    def hash(s: str) -> int:
        return 17

    return (False, "B")  # <- insert bool in first position, char in second position




def hash_tables_3() -> str:
    """
    Why do we need to store keys in hash tables, and not just the values?

    Without storing keys:
        [A] it would be impossible to add entries to the table
        [B] it would be impossible to remove entries from the table
        [C] it would be impossible to look up entries in the table
        [D] A and C
        [E] B and C
        [F] none of the above
    """

    return "C"  # <- insert character in string




def hash_tables_4() -> str:
    """
    * What is the maximum load factor in a hash table with separate chaining?

    [A] 0.5
    [B] 0.7
    [C] 1.0
    [D] 2.0
    [E] none of the above
    """

    return "C"  # <- insert character in string




def select_data_structure() -> str:
    """
    As a newly hired economist at the Federal Reserve, you are choosing a data
    structure to represent the GDP for the period from 2000 to 2020. You could
    use either an array or a hash table - which would be better?

    [A] an array because it would consume less memory
    [B] an array because it does not need to be resized
    [C] a hash table because it has constant-time look up 
    [D] a hash table because the years are unique keys
    [E] A and B
    [F] C and D
    """

    return "E"  # <- insert character in string




def graphs_dfs() -> List[int]:
    """
    Starting at Vertex 1, in what order does DFS visit the vertices in the
    following undirected graph? If there is a choice when deciding which vertex
    to visit next, always choose the numerically smaller vertex. In your answer,
    only include the order in which each vertex is visited the first time (do
    not record re-visits).

      1 -- 2 --- 3    4
      |    |     |    |
      5 -- 6 --- 7 -- 8
      |    |     |   /
      |    |     |  /
      9 -- 10 -- 11
       \   |
        \  |
         \ |
     12 -- 13
    """

    return [1, 2, 3, 7, 6, 5, 8, 4, 11, 10, 9, 13, 12]




def graphs_bfs() -> List[int]:
    """
    Starting at Vertex 1, in what order does BFS visit the vertices in the
    following undirected graph? If there is a choice when deciding which vertex
    to visit next, always choose the numerically smaller vertex. In your answer,
    only include the order in which each vertex is visited the first time (do
    not record re-visits).

    NOTE: The graph below is the same as in the previous problem.

      1 -- 2 --- 3    4
      |    |     |    |
      5 -- 6 --- 7 -- 8
      |    |     |   /
      |    |     |  /
      9 -- 10 -- 11
       \   |
        \  |
         \ |
     12 -- 13
    """

    return [_, _, _, _, _, _, _, _, _, _, _, _, _]

    


##################################################
#              Programming Problems              #
# ---------------------------------------------- #
#    Implement each function definition below.   #
#          Helper functions may be used.         #
##################################################




def bitwise_and(xs: Optional[ListNode],
                ys: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return a linked list representing the bitwise AND of the given two
    equal-length linked lists, where each integer value is either 0 or 1.

    Do not use loops for this definition.

    A bitwise AND operation results in 1 where both bits at the same location
    are 1 and 0 otherwise. 
    
    Example:

        0110
      & 1100
        ----
        0100  <- result contains 1 only where both operands contained 1

    >>> xs = ListNode(0, ListNode(1, ListNode(1, ListNode(0, None))))
    >>> ys = ListNode(1, ListNode(1, ListNode(0, ListNode(0, None))))
    >>> bitwise_and(xs, ys)
    ListNode(0, ListNode(1, ListNode(0, ListNode(0, None))))
    """
    if xs is None:
        return None

    if ys is None:
        return None

    if xs.val == 1 and ys.val == 1:
        i = 1
    else:
        i = 0

    return ListNode(i, bitwise_and(xs.ref, ys.ref))




def has_triangle(graph: Tuple[ListNode, ...]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) contains
    a simple triangle and False otherwise. For this problem, a simple triangle
    is composed of exactly 3 vertices; in other words, do not count triangles
    that require considering more than 3 vertices to form.

    The graph below does contain a simple triangle, BDE. Note that a graph with
    a simple triangle may still have additional vertices outside the triangle.

             0
           /   \
          1     2
         /  \    \
        3 -- 4 -- 5

    The graph below does not contain a simple triangle, as its triangle is
    composed of more than 3 vertices.

             0
           /   \
          1     2
         /       \
        3 -- 4 -- 5

    >>> graph = (ListNode(1, ListNode(2, None)),
                 ListNode(0, ListNode(3, ListNode(4, None))),
                 ListNode(0, ListNode(5, None)),
                 ListNode(1, ListNode(4, None)),
                 ListNode(1, ListNode(3, ListNode(5, None))),
                 ListNode(2, ListNode(4, None)))
    >>> has_triangle(graph)
    True

    >>> graph = (ListNode(1, ListNode(2, None)),
                 ListNode(0, ListNode(3, None)),
                 ListNode(0, ListNode(5, None)),
                 ListNode(1, ListNode(4, None)),
                 ListNode(3, ListNode(5, None)),
                 ListNode(2, ListNode(4, None)))
    >>> has_triangle(graph)
    False
    """

