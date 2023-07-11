# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2021

from typing import List, Optional, Tuple


class ListNode:

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
        return str(self.val) + " " + str(self.ref)


class Queue:

    def __init__(self, head: Optional[ListNode]) -> None:
        """
        An instance of Queue has two attributes.

            head: A reference to the first ListNode in the queue.
            tail: A reference to the final ListNode in the queue.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """
        self.head = head
        temp = head
        if temp == None:
            self.tail = None
        else:
            while temp.ref is not None:
                temp = temp.ref
            self.tail = temp

    def __eq__(self, other: "Queue") -> bool:
        """
        Return True if both Queue objects maintain references to the same
        sequence of ListNode objects and False otherwise.

        >>> qx = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qy = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qz = Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        >>> qx == qy
        True
        >>> qx == qz
        False
        """
        self = self.head
        other = other.head
        while self is not None and other is not None:
            if self.val != other.val:
                return False

            self = self.ref
            other = other.ref
            
        return self is None and other is None

    def enqueue(self, val: int) -> None:
        """
        Add the given integer as a ListNode to the tail of the queue. This
        function mutates the calling Queue object in-place and does not return
        a value.

        >>> queue = Queue(ListNode(1, ListNode(2, None)))
        >>> queue.enqueue(3)
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """
        node = self.head
        if self.head is None:
            self.head = ListNode(val, None)
            self.tail = self.head

        else:
            while node.ref is not None:
                node = node.ref
            node.ref = ListNode(val, None)

            self.tail.ref = ListNode(val, None)
            
            self.tail = self.tail.ref

    def dequeue(self) -> ListNode:
        """
        Remove the ListNode at the head of the queue and return it with its
        reference set to None. If the queue is empty, raise a ValueError. This
        function mutates the calling Queue object.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.dequeue()
        ListNode(1, None)
        >>> queue.head
        ListNode(2, ListNode(3, None))
        >>> queue.tail
        ListNode(3, None)
        """
        if self.head is None:
            raise ValueError

        head = ListNode(self.head.val, None)

        self.head = self.head.ref
        if self.head is None:
            self.tail = self.head

        return head


def size(queue: Queue) -> int:
    """
    Return the number of ListNodes in the given queue. The queue must contain
    its original ListNodes in the same order at the end of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> size(queue)
    3
    """
    c = 0
    temp_node = queue
    new_queue = Queue(None)

    while temp_node.head is not None:
        c += 1
        x = temp_node.dequeue()
        new_queue.enqueue(x.val)

    if queue.head is None:

        queue.head = new_queue.head
        queue.tail = new_queue.tail

    return c


def dequeue_all(queue: Queue, val: int) -> int:
    """
    Using dequeue and enqueue operations, remove all ListNodes from the queue
    that contain the given integer value and return the number of nodes removed.
    All other ListNodes must be in the queue in their original order at the end
    of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(1, ListNode(3, None)))))
    >>> dequeue_all(queue, 1)
    2
    >>> queue.head
    ListNode(2, ListNode(3, None))
    """
    c = 0
    temp_list = []
    while queue.head is not None:
        if queue.head.val == val:
            queue.dequeue()
            c += 1
        else:
            temp_list.append(queue.dequeue())
    if len(temp_list) >= 1:
        queue2 = Queue(temp_list.pop(0))
        for x in temp_list:
            queue2.enqueue(x.val)
        queue.head = queue2.head
        queue.tail = queue2.tail

    return c


def flip(queue: Queue) -> None:
    """
    Reverse the ListNodes of the given queue such that the original tail node
    becomes the head and vice versa. This function mutates the queue.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> flip(queue)
    >>> queue.head
    ListNode(3, ListNode(2, ListNode(1, None)))
    >>> queue.tail
    ListNode(1, None)
    """
    reverse_list = []
    while queue.head is not None:
        reverse_list.append(queue.dequeue())

    reverse_list.reverse()
    if len(reverse_list) >= 1:
        queue_copy = Queue(reverse_list.pop(0))
        for x in reverse_list:
            queue_copy.enqueue(x.val)
        queue.head = queue_copy.head
        queue.tail = queue_copy.tail


def sift_up(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap that has undergone a sift-up operation for the value at
    the given index.

    >>> sift_up([7, 6, 5, 4, 3, 2, 8], 6)
    [8, 6, 7, 4, 3, 2, 5]
    """
    i = (index - 1) // 2
    while heap[index] > heap[i] and i >= 0:
        heap[i], heap[index] = heap[index], heap[i]
        index = i
        i = (index - 1) // 2
    return heap


def sift_down(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap in which the root of a subtree at the given index has
    been sifted down (if necessary) to maintain the Heap Property.

    >>> sift_down([1, 7, 6, 5, 4, 3, 2], 0)
    [7, 5, 6, 1, 4, 3, 2]
    """

    length = len(heap) - 1

    while (2 * index + 1) <= length:

        c1 = 2 * index + 1
        c2 = 2 * index + 2

        if c2 <= length and heap[index] < heap[c2] \
                and heap[c2] >= heap[c1]:
            heap[index], heap[c2] = heap[c2], heap[index]
            index = c2

        elif c1 <= length and heap[index] < heap[c1]:
            heap[index], heap[c1] = heap[c1], heap[index]
            index = c1

        else:
            return heap

    return heap


def heapify(ints: List[int]) -> List[int]:
    """
    Return a max-heap (represented as a list of integers) created using the
    given integers. This function must using sifting instead of insert to run
    in linear (instead of log-linear) time.

    >>> heapify([1, 2, 3, 4, 5, 6, 7])
    [7, 5, 6, 4, 2, 1, 3]
    """
    i = 1
    index = len(ints) - i

    while index >= 0:
        sift_down(ints, index)
        index -= i
    index = len(ints) - i

    while index >= 0:
        sift_up(ints, index)
        index -= 1

    return ints


def insert(heap: List[int], val: int) -> List[int]:
    """
    Return a max-heap with the given value added, using the sift-up operation
    to restore the Heap Property as necessary.

    >>> insert([6, 5, 4, 3, 2, 1], 7)
    [7, 5, 6, 3, 2, 1, 4]
    """
    heap.append(val)
    sift_up(heap, len(heap) - 1)

    return heap


def remove(heap: List[int]) -> Tuple[int, List[int]]:
    """
    Return a tuple containing the removed value (previously at the root of the
    max-heap) along with the updated max-heap, using the sift-down operation to
    restore the Heap Property as necessary. If the heap is empty, raise a
    ValueError.

    >>> remove([7, 6, 5, 4, 3, 2, 1])
    (7, [6, 4, 5, 1, 3, 2])
    """
    if len(heap) == 0:
        raise ValueError
    else:
        removedVal = heap.pop(0)
        if len(heap) == 0:
            return removedVal, heap

        else:
            new_root = heap.pop(len(heap) - 1)
            heap.insert(0, new_root)
            heap = sift_down(heap, 0)

            return removedVal, heap
