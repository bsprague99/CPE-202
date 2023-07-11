# Name:         Brneden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz III
# Term:         Winter 2021

import unittest

import quiz3
from quiz3 import TreeNode  # only allowed use of from ... import


class TestAddTrees(unittest.TestCase):

    def test_add_trees_1(self):
        xs = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None),
                      TreeNode(4, None, TreeNode(5, None, None)))
        ys = TreeNode(2, TreeNode(3, TreeNode(4, None, None), None),
                      TreeNode(5, None, TreeNode(6, None, None)))
        sum_tree = TreeNode(3, TreeNode(5, TreeNode(7, None, None), None),
                            TreeNode(9, None, TreeNode(11, None, None)))
        self.assertEqual(quiz3.add_trees(xs, ys), sum_tree)

    def test_add_trees_2(self):
        xs = TreeNode(10, TreeNode(20, TreeNode(30, None, None), None),
                      TreeNode(40, None, TreeNode(50, None, None)))
        ys = TreeNode(20, TreeNode(30, TreeNode(40, None, None), None),
                      TreeNode(50, None, TreeNode(60, None, None)))
        sum_tree = TreeNode(30, TreeNode(50, TreeNode(70, None, None), None),
                            TreeNode(90, None, TreeNode(110, None, None)))
        self.assertEqual(quiz3.add_trees(xs, ys), sum_tree)

    def test_add_trees_3(self):
        xs = TreeNode(11, TreeNode(21, TreeNode(31, None, None), None),
                      TreeNode(41, None, TreeNode(51, None, None)))
        ys = TreeNode(21, TreeNode(31, TreeNode(41, None, None), None),
                      TreeNode(51, None, TreeNode(61, None, None)))
        sum_tree = TreeNode(32, TreeNode(52, TreeNode(72, None, None), None),
                            TreeNode(92, None, TreeNode(112, None, None)))
        self.assertEqual(quiz3.add_trees(xs, ys), sum_tree)

    def test_add_trees_4(self):
        xs = TreeNode(12, TreeNode(22, TreeNode(32, None, None), None),
                      TreeNode(42, None, TreeNode(52, None, None)))
        ys = TreeNode(22, TreeNode(32, TreeNode(42, None, None), None),
                      TreeNode(52, None, TreeNode(62, None, None)))
        sum_tree = TreeNode(34, TreeNode(54, TreeNode(74, None, None), None),
                            TreeNode(94, None, TreeNode(114, None, None)))
        self.assertEqual(quiz3.add_trees(xs, ys), sum_tree)

    def test_add_trees_5(self):
        xs = TreeNode(2, TreeNode(2, TreeNode(2, None, None), None),
                      TreeNode(2, None, TreeNode(2, None, None)))
        ys = TreeNode(2, TreeNode(2, TreeNode(2, None, None), None),
                      TreeNode(2, None, TreeNode(2, None, None)))
        sum_tree = TreeNode(4, TreeNode(4, TreeNode(4, None, None), None),
                            TreeNode(4, None, TreeNode(4, None, None)))
        self.assertEqual(quiz3.add_trees(xs, ys), sum_tree)


class TestSiftDown(unittest.TestCase):

    def test_sift_down_1(self):
        root = TreeNode(1, TreeNode(7, TreeNode(5, None, None),
                                    TreeNode(4, None, None)),
                        TreeNode(6, TreeNode(3, None, None),
                                 TreeNode(2, None, None)))
        self.assertEqual(quiz3.sift_down(root),
                         TreeNode(7, TreeNode(5, TreeNode(1, None, None),
                                              TreeNode(4, None, None)),
                                  TreeNode(6, TreeNode(3, None, None),
                                           TreeNode(2, None, None))))

    def test_sift_down_2(self):
        root = TreeNode(1, TreeNode(6, TreeNode(5, None, None),
                                    TreeNode(4, None, None)),
                        TreeNode(6, TreeNode(3, None, None),
                                 TreeNode(2, None, None)))
        self.assertEqual(quiz3.sift_down(root),
                         TreeNode(6, TreeNode(6, TreeNode(5, None, None),
                                              TreeNode(4, None, None)),
                                  TreeNode(3, TreeNode(1, None, None),
                                           TreeNode(2, None, None))))

    def test_sift_down_3(self):
        root = TreeNode(1, TreeNode(6, None, None),
                        TreeNode(6, None, None))
        self.assertEqual(quiz3.sift_down(root),
                         TreeNode(6, TreeNode(6, None, None),
                                  TreeNode(1, None, None)))

    def test_sift_down_4(self):
        root = TreeNode(1, TreeNode(2, None, None),
                        TreeNode(3, None, None))
        self.assertEqual(quiz3.sift_down(root),
                         TreeNode(3, TreeNode(2, None, None),
                                  TreeNode(1, None, None)))

    def test_sift_down_5(self):
        root = TreeNode(10, TreeNode(60, None, None),
                        TreeNode(60, None, None))
        self.assertEqual(quiz3.sift_down(root),
                         TreeNode(60, TreeNode(60, None, None),
                                  TreeNode(10, None, None)))


if __name__ == "__main__":
    unittest.main()
