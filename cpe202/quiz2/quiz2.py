# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz II
# Term:         Winter 2021


##############################################################################
# IMPORTANT: By taking this quiz, you agree not to discuss its contents with #
# any other student who has yet to take it, in this or future terms.         #
#                                                                            #
# Violation of this agreement will constitute cheating and may result in     #
# retroactive course failure, as well as other disciplinary action.          #
##############################################################################


##################################################
# Submit Command: /home/dkauffma/casey 202 quiz2 #  <- Don't ask me for this!
##################################################


from typing import Optional


# do not modify this class
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref


###############################################################################
# This quiz will assess your understanding of stacks and recursion.           #
# Do not write additional functions.                                          #
###############################################################################


def is_balanced(symbols: str) -> bool:
    """
    Given a string of symbols, return a Boolean value indicating whether or not
    the symbols in the string are balanced. For symbols to be balanced, a
    corresponding closing symbol must exist for every opening symbol with
    proper nesting order.

    Use a Python list as a stack to keep track of whether each symbol is
    properly nested. Do not use recursion; use loops instead.

    The only symbols that can be in the given string are: (){}[]

    Balance Rules:

    * For every opening symbol, there must be a corresponding closing symbol
      of the same type.
      e.g. in "(()" the second ( does not have a corresponding opening )

    * A closing symbol cannot come before the required number of corresponding
      opening symbols of the same type.
      e.g. in "())" the second ) does not have a corresponding opening (

    * A closing symbol of one type cannot come before a closing symbol of
      another type if the latter type opened more recently in the sequence.
      e.g. in "({)" the closing ) comes before the closing }

    >>> is_balanced("({[][]}[{}]())")
    True
    >>> is_balanced("({[)")
    False
    """
    balanced_stack = []
    i = True
    cnt = 0
    while cnt < len(symbols) and i:
        symbol = symbols[cnt]
        if symbol == "[" or symbol == "(" or symbol == "{":
            balanced_stack.append(symbol)
        else:
            if balanced_stack is None:
                i = False
            else:
                top = balanced_stack.pop()

                while top == "[" and \
                        symbol == "]" or top \
                        == "(" and symbol == ")" \
                        or top == "{" and \
                        symbol == "}":
                    return True
        cnt += 1
    return bool(balanced_stack is None)


def is_zero_sum(head: Optional[ListNode], acc: int) -> bool:
    """
    Return True if the integers in the linked list sum to zero and False
    otherwise. Assume the accumulator starts at zero.

    Do not use Python lists or loops.

    >>> is_zero_sum(ListNode(-3, ListNode(2, ListNode(1, None))), 0)
    True
    >>> is_zero_sum(ListNode(1, ListNode(-1, ListNode(-1, None))), 0)
    False
    """
    if head is None:
        return False

    x = head.val
    acc += x
    if head.ref is None:
        if acc == 0:
            return True
    if head.ref is None:
        if acc != 0:
            return False

    return bool(is_zero_sum(head.ref, acc))


def count_words(words: str, index: int) -> int:
    """
    Return the number of words in the given string. Words are defined as
    non-space text delimited by one space. Assume that all word delimiters are
    exactly one space and that the string never starts or ends with a space.
    Use the index argument to keep track of position, which starts at zero.

    Do not use Python lists or loops.

    >>> count_words("python", 0)
    1
    >>> count_words("computer science and software engineering", 0)
    5
    """
    x = 1
    if index == len(words) + x - x:
        return 0

    if index == len(words) - x:
        return 1

    elif words[index] == " ":
        return x + count_words(words, index + x)

    else:
        return count_words(words, index + x)
