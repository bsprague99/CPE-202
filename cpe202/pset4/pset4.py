# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Winter 2021

from typing import Optional, Tuple


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


class TreeNode:

    def __init__(self, val: int, l_ref: Optional["TreeNode"],
                 r_ref: Optional["TreeNode"]) -> None:
        self.val = val
        self.l_ref = l_ref
        self.r_ref = r_ref

    def __eq__(self, other: Optional["TreeNode"]) -> bool:
        if other is None:
            return False
        return (self.val == other.val
                and self.l_ref == other.l_ref and self.r_ref == other.r_ref)

    def __repr__(self) -> str:
        s = str(self.val)
        if self.l_ref is not None:
            s += " " + str(self.l_ref)
        if self.r_ref is not None:
            s += " " + str(self.r_ref)
        return s


def binary_search(ints: Tuple[int, ...], n: int, srt: int, stop: int) -> int:
    """
    Using binary search, return the index of the given integer or -1 if it is
    not in the tuple. Assume the tuple is already sorted.

    >>> binary_search((2, 4, 6, 8, 10), 8, 0, 5)
    3
    >>> binary_search((2, 4, 6, 8, 10), 7, 0, 5)
    -1
    """

    mid = (stop - srt) // 2 + srt
    if srt == mid:
        if n == ints[mid]:
            return mid

        return -1
    elif n == ints[mid]:
        return mid

    elif n < ints[mid]:
        return binary_search(ints, n, srt, mid)

    elif n > ints[mid]:
        return binary_search(ints, n, mid, stop)

    return -1


def sum_tree(root: Optional[TreeNode]) -> int:
    """
    Return the sum of all integers in each TreeNode in the tree. If the tree is
    empty, return 0.

    >>> sum_tree(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)))
    6
    """
    if root is None:
        return 0
    return root.val + sum_tree(root.l_ref) + sum_tree(root.r_ref)


def all_binary(root: Optional[TreeNode]) -> bool:
    """
    Return True if every node in the given tree is either a leaf or an interior
    node with exactly two children (or if the tree is empty). Otherwise, return
    False if there is at least one node with only one child.

    >>> root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), \
                           TreeNode(4, None, None))
    >>> all_binary(root)
    False
    """
    if root is None:
        return True

    if root.l_ref is None and root.r_ref is None:
        return True

    if root.l_ref is not None and root.r_ref is not None:
        return all_binary(root.l_ref) and all_binary(root.r_ref)

    return False


def find_range(root: TreeNode) -> Tuple[int, int]:
    """
    Return a 2-tuple containing the minimum and maximum integers (in that order)
    contained in the tree. Assume the tree is non-empty.

    >>> root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    >>> find_range(root)
    (1, 3)
    """
    max_value = root.val
    min_value = root.val

    if root.l_ref is None and root.r_ref is None:
        return min_value, max_value
    elif root.l_ref is not None:

        matching = find_range(root.l_ref)
        max_match = matching[1]
        min_match = matching[0]
        if matching[1] > max_value:
            max_value = max_match
        elif matching[0] < min_value:
            min_value = min_match
    if root.r_ref is not None:
        matching = find_range(root.r_ref)
        max_match = matching[1]
        min_match = matching[0]
        if max_match > min_value:
            max_value = max_match
        elif min_match < min_value:
            min_value = min_match

    return min_value, max_value


def is_bst(root: Optional[TreeNode]) -> bool:
    """
    Return True if the given binary tree has the BST property and False
    otherwise. Assume the tree has no duplicate values.

    A binary tree is a BST if, for any node, all nodes in its left subtree
    contain values lower than its value, and all nodes in its right subtree
    contain values greater than its value.

    >>> is_bst(TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None)))
    False
    """
    if root is None:
        return True
    elif root.l_ref is not None and \
            find_range(root.l_ref)[1] > \
        root.val or root.r_ref is \
            not None and find_range\
                (root.r_ref)[0] < root.val:
        return False
    elif root.l_ref is not None \
            and root.r_ref is not None:
        return is_bst(root.l_ref) and is_bst(root.r_ref)
    return True


def to_bst(head: Optional[ListNode],
           root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Return a BST constructed from values in the given linked list, adding
    TreeNodes with values in the same order as the list. Use the root argument
    as an accumulator for the BST being constructed.

    >>> head = ListNode(2, ListNode(3, ListNode(1, None)))
    >>> to_bst(head, None)
    TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    """
    if head is None:
        return root
    if head is not None:
        root = insert(root, head.val)
    return to_bst(head.ref, root)


def insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Return the root of a BST with a TreeNode containing val in its correctly
    sorted position. Assume val is not already in the tree.

    >>> root = TreeNode(2, None, None)
    >>> insert(root, 1)
    TreeNode(2, TreeNode(1, None, None), None)
    >>> insert(root, 3)
    TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    """
    if root is None:
        return TreeNode(val, None, None)
    if val < root.val:
        root.l_ref = insert(root.l_ref, val)
    else:
        root.r_ref = insert(root.r_ref, val)
    return root


def remove(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Return the root of a BST with the TreeNode containing the given integer
    removed. If such a node does not exist, raise a ValueError. Assume no more
    than one node contains this integer.

    If the node to be removed has two children, replace its value with the
    maximum value of its left subtree and remove that node in the left subtree.

    >>> root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    >>> remove(root, 1)
    TreeNode(2, None, TreeNode(3, None, None))
    """
    if root is None:
        raise ValueError
    elif val < root.val:
        if root.l_ref:
            root.l_ref = remove(root.l_ref, val)
        else:
            raise ValueError
    elif val > root.val:
        if root.r_ref:
            root.r_ref = remove(root.r_ref, val)
        else:
            raise ValueError
    elif val == root.val:
        if root.r_ref is None:
            node = root.l_ref
            root = None
            return node

        elif root.l_ref is None:
            node = root.r_ref
            root = None
            return node

        node = root.l_ref
        root.val = node.val
        root.l_ref = remove(root.l_ref, node.val)
    else:
        raise ValueError
    return root


def rake_leaves(root: Optional[TreeNode],
                head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return a linked list of ListNode objects, matching the order of the leaves
    of the given tree, from left to right.

    Construct the linked list in reverse, starting with the right-most leaf and
    building the list backward, using the given head argument as an accumulator.

    >>> rake_leaves(TreeNode(1, TreeNode(2, TreeNode(4, None, None), \
                                            TreeNode(5, None, None)), \
                                TreeNode(3, None, None)), \
                    None)
    ListNode(4, ListNode(5, ListNode(3, None)))
    """
    if root is None:
        return head
    if root.l_ref is None and root.r_ref is None:
        new_list = ListNode(root.val, None)
        new_list.ref = head
        head = new_list
        return head
    head = rake_leaves(root.r_ref, head)
    head = rake_leaves(root.l_ref, head)
    return head

def order_list(root: Optional[TreeNode], order: str,
               head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return a linked list in which the integers in the list were retrieved from
    the tree according to the given order. Assume the order is one of
    "preorder", "inorder", or "postorder".

    >>> root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    >>> order_list(root, "inorder", None)
    ListNode(2, ListNode(1, ListNode(3, None)))
    """

    if root is None:
        return None

    if order == 'preorder':
        if root.r_ref is not None:
            head = order_list(root.r_ref, order, head)
        if root.l_ref is not None:
            head = order_list(root.l_ref, order, head)
        head = ListNode(root.val, head)
    if order == 'inorder':
        if root.r_ref is not None:
            head = order_list(root.r_ref, order, head)
        head = ListNode(root.val, head)
        if root.l_ref is not None:
            head = order_list(root.l_ref, order, head)
    if order == 'postorder':
        head = ListNode(root.val, head)
        if root.r_ref is not None:
            head = order_list(root.r_ref, order, head)
        if root.l_ref is not None:
            head = order_list(root.l_ref, order, head)
    return head
