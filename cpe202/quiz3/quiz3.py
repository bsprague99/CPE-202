# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz III
# Term:         Winter 2021


##############################################################################
# IMPORTANT: By taking this quiz, you agree not to discuss its contents with #
# any other student who has yet to take it, in this or future terms.         #
#                                                                            #
# Violation of this agreement will constitute cheating and may result in     #
# retroactive course failure, as well as other disciplinary action.          #
##############################################################################


##################################################
# Submit Command: /home/dkauffma/casey 202 quiz3 #  <- Don't ask me for this!
##################################################


from typing import Optional


# do not modify this class
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


###############################################################################
# This quiz will assess your understanding of trees and heaps.                #
# Do not use Python lists or loops.                                           #
# You may write additional helper functions.                                  #
###############################################################################


def add_trees(xs: TreeNode, ys: TreeNode) -> TreeNode:
    """
    Given two binary trees of the same shape, return a new binary tree of the
    same shape that represents the pairwise sum of every two nodes in the same
    position in the original two trees. Assume both trees are non-empty.

    Do not modify either of the original trees in-place; instead, create a new
    tree with the added values.

    >>> xs = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), \

                         TreeNode(4, None, TreeNode(5, None, None)))
    >>> ys = TreeNode(2, TreeNode(3, TreeNode(4, None, None), None), \
                         TreeNode(5, None, TreeNode(6, None, None)))
    >>> add_trees(xs, ys)
    TreeNode(3, TreeNode(5, TreeNode(7, None, None), None), \
                TreeNode(9, None, TreeNode(11, None, None)))
    """
    if xs is None:
        return None
    return TreeNode(xs.val + ys.val, add_trees \
        (xs.l_ref, ys.l_ref), add_trees(xs.r_ref, ys.r_ref))


def sift_down(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Return the given binary tree with the root node sifted down to its correct
    position (as in a max-heap). Do not sift down every node in the tree; only
    sift down the root of the original tree. Assume the tree satisfies the
    Shape Property.

    >>> root = TreeNode(1, TreeNode(7, TreeNode(5, None, None),  \
                                       TreeNode(4, None, None)), \
                           TreeNode(6, TreeNode(3, None, None),  \
                                       TreeNode(2, None, None)))
    >>> sift_down(root)
    TreeNode(7, TreeNode(5, TreeNode(1, None, None),  \
                            TreeNode(4, None, None)), \
                TreeNode(6, TreeNode(3, None, None),  \
                            TreeNode(2, None, None)))
    """

    if root.r_ref is None and root.l_ref is None:
        return None
    if root.val > root.r_ref.val and root.val > root.l_ref.val:
        return None
    if root.r_ref.val < root.l_ref.val:
        temp = root.val
        root.val = root.l_ref.val
        root.l_ref.val = temp
        sift_down(root.l_ref)
        return root
    else:
        temp = root.val
        root.val = root.r_ref.val
        root.r_ref.val = temp
        sift_down(root.r_ref)
        return root
