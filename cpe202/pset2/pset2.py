# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Winter 2021

from typing import Optional, Tuple


# do not modify this class
class StackNode:
    """
    A StackNode is like a ListNode except that its ref attribute may only be
    accessed in the push or pop functions, to be defined below.
    """

    def __init__(self, val: int, ref: Optional["StackNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: "StackNode") -> bool:
        """
        Return True if the two given stacks have the same number of StackNodes
        and the same StackNode val at each respective position and False
        otherwise.

        >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
        >>> ys = StackNode(1, StackNode(2, StackNode(4, None)))
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
        Return a string representation of the stack. String representations of
        objects are useful for reading test suite errors.

        >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
        >>> str(xs)
        "1-2-3"
        """
        stack_str = str(self.val)
        while True:
            self = self.ref
            if self is None:
                return stack_str
            stack_str += "-" + str(self.val)


def push(top: Optional[StackNode], new: StackNode) -> StackNode:
    """
    Add the given new StackNode to the top of the stack and return a reference
    to it. Assume the new StackNode's ref attribute is None.

    >>> top = StackNode(2, StackNode(3, None))
    >>> push(top, StackNode(1, None))
    StackNode(1, StackNode(2, StackNode(3, None)))
    """
    if top is None:
        top = new
    else:
        pushed_node = top
        new.ref = pushed_node
        top = new
    return top


def pop(top: Optional[StackNode]) -> Tuple[StackNode, Optional[StackNode]]:
    """
    Remove the StackNode at the top of the stack and return the popped StackNode
    (with its ref set to None) and the reference to the new top of the stack. If
    the stack is initially empty, raise a ValueError.

    top = StackNode(1, StackNode(2, StackNode(3, None)))
     >>> pop(top)
    (StackNode(1, None), StackNode(2, StackNode(3, None)))
     """
    if top is None:
        raise ValueError
    else:
        popped_node = StackNode(top.val, None)
        rest_of_list = top.ref

    return popped_node, rest_of_list


def move(xs: StackNode,
         ys: Optional[StackNode]) -> Tuple[Optional[StackNode], StackNode]:
    """
    Pop the top StackNode from xs and push it to ys. Return references to the
    tops of both stacks.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = None
    >>> move(xs, ys)
    (StackNode(2, StackNode(3, None)), StackNode(1, None))
    """

    x = pop(xs)
    y = push(ys, x[0])
    return x[1], y


def flip_stack(top: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the reversal of the given stack by creating an empty stack and moving
    StackNodes onto it.

    >>> top = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> flip_stack(top)
    StackNode(3, StackNode(2, StackNode(1, None)))
"""

    if top is None:
        return None

    new_stack = StackNode(None, None)

    while top is not None:

        x = pop(top)

        top = x[1]

        if new_stack.val is None:
            new_stack = x[0]

        else:
            new_stack = push(new_stack, x[0])

    return new_stack





def concat(xs: Optional[StackNode],
           ys: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the top of a stack that represents the concatenation of the given
    stacks, such that xs comes before ys.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = StackNode(4, StackNode(5, None))
    >>> concat(xs, ys)
    StackNode(1, StackNode(2, StackNode(3, StackNode(4, StackNode(5, None)))))
    """
    temporary_list = flip_stack(xs)
    while ys is not None:
        newTop = pop(ys)
        ys = newTop[1]
        temporary_list = push(temporary_list, newTop[0])

    final_list = flip_stack(temporary_list)
    return final_list


def pop_all(top: Optional[StackNode], val: int) -> Optional[StackNode]:
    """
    Return a stack with all StackNodes containing the given integer value
    removed from the given stack.

    >>> top = StackNode(1, StackNode(2, StackNode(1, StackNode(3, None))))
    >>> pop_all(top, 1)
    StackNode(2, StackNode(3, None))
    """

    flippedStack = None
    while top != None:
        if top.val == val:
            updated_list = pop(top)
            top = updated_list[1]
        else:
            add_list = pop(top)
            top = add_list[1]
            flippedStack = push(flippedStack, add_list[0])
    final_stack = flip_stack(flippedStack)
    return final_stack


def zip_stacks(xs: Optional[StackNode],
               ys: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the top of a stack that represents the pair-wise combination of the
    given stacks. If one stack runs out of StackNodes, append the remainder of
    the other stack.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = StackNode(4, None)
    >>> zip_stacks(xs, ys)
    StackNode(1, StackNode(4, StackNode(2, StackNode(3, None))))
    """
    cnt = 0
    flippedStack = None
    while xs and ys is not None:
        if cnt % 2 == 0:
            x_stack = pop(xs)
            xs = x_stack[1]
            cnt += 1
            flippedStack = push(flippedStack, x_stack[0])
        else:
            y_stack = pop(ys)
            ys = y_stack[1]
            cnt += 1
            flippedStack = push(flippedStack, y_stack[0])
    if xs is None:
        while ys is not None:
            y2_stack = pop(ys)
            ys = y2_stack[1]
            flippedStack = push(flippedStack, y2_stack[0])
    elif ys is None:
        while xs is not None:
            x2_stack = pop(xs)
            xs = x2_stack[1]
            flippedStack = push(flippedStack, x2_stack[0])
    final_stack = flip_stack(flippedStack)
    return final_stack


def unzip_stack(top: Optional[StackNode]
                ) -> Tuple[Optional[StackNode], Optional[StackNode]]:
    """
    Return a 2-tuple of tops of stacks that represents the pair-wise separation
    of the given stacks. This operation is the inverse of zip_stacks.

    >>> top = StackNode(1, StackNode(4, StackNode(2, \
                                        StackNode(5, StackNode(3, None)))))
    >>> unzip_stack(top)
    (StackNode(1, StackNode(2, StackNode(3, None))), \
     StackNode(4, StackNode(5, None)))
    """
    cnt = 0
    stack_one = None
    stack_two = None
    while top is not None:
        if cnt % 2 == 0:
            new_stack_one = pop(top)
            top = new_stack_one[1]
            cnt += 1
            stack_one = push(stack_one, new_stack_one[0])
        else:
            new_stack_two = pop(top)
            top = new_stack_two[1]
            cnt += 1
            stack_two = push(stack_two, new_stack_two[0])
    final_stack_one = flip_stack(stack_one)
    final_stack_two = flip_stack(stack_two)
    return final_stack_one, final_stack_two


def sort_stack(top: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return a stack in with the StackNodes from the given stack are sorted in
    ascending order by their integer values.

    It is recommended to create two empty stacks: one to which StackNodes are
    temporarily moved, and another to store the sorted StackNodes.

    >>> top = StackNode(5, StackNode(2, StackNode(8, None)))
    >>> sort_stack(top)
    StackNode(2, StackNode(5, StackNode(8, None)))
    """
    if top is None:
        return None

    new_Stack = None
    while top is not None:
        Stack_value = top.val
        temp = pop(top)
        top = temp[1]

        while (new_Stack is not None) and (new_Stack.val > Stack_value):
            temp1 = pop(new_Stack)
            new_Stack = temp1[1]
            top = push(top, temp1[0])

        new_Stack = push(new_Stack, StackNode(Stack_value, None))

    final_stack = flip_stack(new_Stack)

    return final_stack
