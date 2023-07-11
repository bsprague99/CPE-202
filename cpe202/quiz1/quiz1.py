# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz I
# Term:         Winter 2021


##############################################################################
# IMPORTANT: By taking this quiz, you agree not to discuss its contents with #
# any other student who has yet to take it, in this or future terms.         #
#                                                                            #
# Violation of this agreement will constitute cheating and may result in     #
# retroactive course failure, as well as other disciplinary action.          #
##############################################################################


##################################################
# Submit Command: /home/dkauffma/casey 202 quiz1 #  <- Don't ask me for this!
##################################################


from typing import Optional


# do not modify this class (except __repr__)
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __repr__(self) -> str:
        """
        Return a string representation of a ring of ListNodes. This method is
        optional as a debugging aid and is not for credit.
        """


def create_ring(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Form a ring of ListNodes such that all nodes are in the same order but the
    last ListNode (the tail) has its reference pointing to the head of the list
    instead of None. The node returned must be the original tail.

    Loops must be used; do not use recursion or Python lists.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> tail = create_ring(head)
    >>> head.val == tail.ref.val
    True
    """

    if head is None:
        return None

    head1 = head.ref
    new_Node = ListNode(head.val, None)
    new_head = new_Node

    while head1 is not None and head1 != head:
        new_Node.ref = ListNode(head1.val, None)
        head1 = head1.ref
        new_Node = new_Node.ref

    new_Node.ref = new_head

    return new_Node


def are_rings_equal(xs: Optional[ListNode], ys: Optional[ListNode]) -> bool:
    """
    Return True if both ListNode rings are equal and False otherwise. Assume
    the values of the ListNodes in each ring are unique and in ascending order,
    and that the arguments refer to head (lowest-valued) nodes in their rings.

    Loops must be used; do not use recursion or Python lists.

    >>> xs = create_ring(ListNode(1, ListNode(2, None))).ref
    >>> ys = create_ring(ListNode(1, ListNode(3, None))).ref
    >>> are_rings_equal(xs, ys)
    False
    """
    xs_copy = xs
    ys_copy = ys
    # If xs and ys are none --> equal
    if xs is None and ys is None:
        return True
    # If xs is none and ys isn't --> not equal
    elif xs is None and ys is not None:
        return False
    # If xs is not none and ys is none --> not equal
    elif xs is not None and ys is None and xs_copy.val != ys_copy.val:
        return False

    headX = xs.ref
    headY = ys.ref

    while xs is not None and ys is not None:
        if headX.val != headY.val:
            return False

        elif xs != headX and ys != headY:
            headX = headX.ref
            headY = headY.ref

        elif headX == xs and headY == ys:
            return True

    return False
