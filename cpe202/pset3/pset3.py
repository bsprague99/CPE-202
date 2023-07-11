# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Winter 2021

from typing import Optional


# do not modify this class
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: "ListNode") -> bool:
        """
        Return True if the two given lists have the same number of ListNodes and
        the same ListNode val at each respective position and False otherwise.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> ys = ListNode(1, ListNode(2, ListNode(4, None)))
        >>> xs == ys
        False
        """
        while self is not None and other is not None:
            if self.val != other.val:
                return False
            self = self.ref
            other = other.ref
        return self is None and other is None

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list. String
        representations of objects are useful for reading test suite errors.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> str(xs)
        "1-2-3"
        """
        list_str = str(self.val)
        while True:
            self = self.ref
            if self is None:
                return list_str
            list_str += "-" + str(self.val)


def mul(x: int, y: int) -> int:
    """
    Return the product of x and y without using the multiplication operator.

    >>> mul(-2, -3)
    6
    """
    if y == 0:
        return 0
    elif y == 1:
        return x
    elif y < 0:
        return - x + mul(x, y + 1)
    else:
        return x + mul(x, y - 1)


def exp(x: int, y: int) -> int:
    """
    Return the result of taking x to the y power without using the
    multiplication or exponentiation operators. Assume y is non-negative.

    >>> exp(-2, 3)
    -8
    """
    if y == 0:
        return 1
    else:
        return mul(exp(x, y-1), x)



def fac(n: int) -> int:
    """
    Return n factorial without using the multiplication operator. Assume n is
    non-negative.

    >>> fac(5)
    120
    """
    #if n is 1:
      #  return n
   # else:
      #  return mul(n, fac(n - 1))
    if n == 0:
        return 1
    return mul(fac(n - 1), n)


def fibonacci(n: int, a: int, b: int) -> int:
    """
    Return an integer representing the Fibonacci Sequence at the given nth
    position. Each integer in this sequence is the sum of the previous two
    integers (except for the first two integers, 0 and 1, which are base values
    not derived from adding other integers). Assume n is positive.

    Use the a and b parameters to keep track of the previous two values in the
    sequence. These two values should always start as 0 and 1, respectively.

    >>> fibonacci(8, 0, 1)
    13
    """
    if n - 1 == 0:
        return a
    return fibonacci(n - 1, a=b, b=a + b)


def make_substring(string: str, start: int, stop: int, step: int) -> str:
    """
    Return a substring of the given string that begins at the start index
    (inclusive) and ends at the stop index (exclusive), increasing step
    characters each iteration. Assume start and stop are non-negative and step
    is positive.

    >>> make_substring("COMPUTER", 0, 10, 3)
    "CPE"
    """
    if (start > len(string) - 1) or start >= stop:
        return ''
    if ((start + step) > stop - 1) or ((start + step) > len(string) + step):
        return string[start]
    return string[start] + make_substring(string, start + step, stop, step)


def is_palindrome(chars: str) -> bool:
    """
    Return True if the given string is a palindrome and False otherwise. A
    palindrome is a symmetric sequence of characters, reading the same forward
    and backward.

    Use make_substring to modify the string for each recursive call.

    >>> is_palindrome("tacocat")
    True
    >>> is_palindrome("palindrome")
    False
    """
    if len(chars) <= 1:
        return True
    if chars[0] != chars[len(chars) - 1]:
        return False
    return is_palindrome(make_substring(chars, 1, len(chars) - 1, 1))


def swap_chars(chars: str) -> str:
    """
    Return a string in which each pair of adjacent characters in the given
    string have switched positions. If the number of characters in the string
    is odd, leave the position of the final character unchanged.

    Use make_substring to modify the string on each recursive call.

    >>> swap_chars("AaBbCcD")
    "aAbBcCD"
    """
    if len(chars) <= 1:
        return chars

    return (chars[1] + chars[0] +
            swap_chars(make_substring(chars, 2, len(chars), 1)))


def length(head: Optional[ListNode]) -> int:
    """
    Return the number of nodes in the given linked list.

    >>> length(ListNode(1, ListNode(2, ListNode(3, None))))
    3
    """
    # If head is NULL, return 0.
    if head is None:
        return 0
    # The length is 1 + length of remaining list.
    return 1 + length(head.ref)


def find_max(head: ListNode) -> int:
    """
    Return the highest integer in the given linked list. Assume the linked list
    is not empty.

    >>> find_max(ListNode(2, ListNode(3, ListNode(4, ListNode(1, None)))))
    4
    """

    if head.ref is None:
        return head.val
    else:
        return max(head.val, find_max(head.ref))


def reverse(head: Optional[ListNode],
            acc: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the reverse of the given linked list.

    Use the accumulator to build the reversed list as an argument to the
    recursive calls, instead of building the reversed list after each recursive
    call returns.

    >>> reverse(ListNode(1, ListNode(2, ListNode(3, None))), None)
    ListNode(3, ListNode(2, ListNode(1, None)))
    """
    if head is None:
        return acc

    first = head
    rest = first.ref

    if rest is None:
        head_ref = first
        return head_ref

    head_ref = reverse(rest, acc)

    rest.ref = first
    first.ref = None

    return head_ref


class NestingDoll:

    def __init__(self, count: int) -> None:
        """
        Representation of a nesting (Matryoshka) doll, with count specifying
        how many dolls are to be created. Each NestingDoll should have exactly
        one attribute, inner, which is either a NestingDoll or, if it is the
        innermost doll, None. Do not add an attribute for the count parameter.

        >>> doll = NestingDoll(3)
        >>> doll.inner.inner.inner == None
        True
        """
        if count == 1:
            self.inner = None
        else:
            self.inner = NestingDoll(count - 1)

    def __eq__(self, other: "NestingDoll") -> bool:
        """
        Return True if both NestingDoll objects have the same number of nested
        dolls and False otherwise.

        >>> NestingDoll(1) == NestingDoll(1)
        True
        >>> NestingDoll(1) == NestingDoll(2)
        False
        """
        if self.inner is None and other.inner is None:
            return True

        elif self.inner is None or other.inner is None:
            return False

        else:
            return self.inner == other.inner

    def __repr__(self) -> str:
        """
        Return a string representing the structure of the NestingDoll, using
        nested parentheses for each outer doll and 8 (the number eight) for the
        innermost doll.

        >>> doll = NestingDoll(3)
        >>> str(doll)
        "((8))"
        """
        doll = self
        if doll.inner is None:
            return str(8)
        return "(" + str(doll.inner) + ")"
