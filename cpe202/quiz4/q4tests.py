# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz IV
# Term:         Winter 2021

import unittest
import quiz4


class TestIsTree(unittest.TestCase):

    def test_is_tree_1(self):
        """
             2
           /   \
          0     1
         /|\     \
        3 4 5     6
        """
        adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
        self.assertTrue(quiz4.is_tree(adj_list))

    def test_is_tree_2(self):
        adj_list = [[3, 4, 1], [6], [0, 1], [], [], [], []]
        self.assertFalse(quiz4.is_tree(adj_list))

    def test_is_tree_3(self):
        adj_list = [[30, 40, 10], [60], [0, 10], [], [], [], []]
        self.assertFalse(quiz4.is_tree(adj_list))

    def test_is_tree_4(self):
        adj_list = [[3, 4, 1], [6], [0, 1], [3, 9], [4, 1], [], []]
        self.assertFalse(quiz4.is_tree(adj_list))

    def test_is_tree_5(self):
        """
                     2
                   /   \
                  2  -  2
                 /       \
                0         1
               /|\         \
             3 4 5          6
        """
        adj_list = [[3, 4, 5], [6], [0, 1], [2, 2], [2, 2], [], []]
        self.assertFalse(quiz4.is_tree(adj_list))


class TestGetHeight(unittest.TestCase):

    def test_get_height_1(self):
        """
             2
           /   \
          0     1
         /|\     \
        3 4 5     6
        """
        adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
        self.assertEqual(quiz4.get_height(adj_list), 7)

    def test_get_height_2(self):
        adj_list = []
        self.assertEqual(quiz4.get_height(adj_list), -1)

    def test_get_height_3(self):
        adj_list = [[3, 4, 5], [6], [], [], [], [], []]
        self.assertEqual(quiz4.get_height(adj_list), 4)

    def test_get_height_4(self):
        adj_list = [[3, 4], [6], [0, 1], [3], [], [], []]
        self.assertEqual(quiz4.get_height(adj_list), 6)

    def test_get_height_5(self):
        """
                     2
                   /   \
                  2  -  2
                 /       \
                0         1
               /|\         \
             3 4 5          6
        """
        adj_list = [[]]
        self.assertEqual(quiz4.get_height(adj_list), 0)


class TestFindRoot(unittest.TestCase):

    def test_find_root_1(self):
        adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
        self.assertEqual(quiz4.find_root(adj_list, 3), 2)

    def test_find_root_2(self):
        adj_list = [[3, 4, 5], [6], [], [], [], [], []]
        self.assertEqual(quiz4.find_root(adj_list, 3), 0)

    def test_find_root_3(self):
        """
                     2
                   /   \
                  0     1
                 /|\     \
                3 4 5     6
        """
        adj_list = [[3, 4], [7], [0, 2], [], [], []]
        self.assertEqual(quiz4.find_root(adj_list, 1), 1)

    def test_find_root_4(self):
        adj_list = [[3], [6], [1, 2], [], [], [], []]
        self.assertEqual(quiz4.find_root(adj_list, 3), 0)

    def test_find_root_5(self):
        adj_list = [[3, 4, 5], [5], [], [], [], [], []]
        self.assertEqual(quiz4.find_root(adj_list, 3), 0)


class TestOrderDfs(unittest.TestCase):

    def test_order_dfs_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(quiz4.order_dfs(adj_list, 2, []), [2, 0, 1, 3])

    def test_order_dfs_2(self):
        adj_list = []
        self.assertEqual(quiz4.order_dfs(adj_list, 2, []), [])

    def test_order_dfs_3(self):
        adj_list = [[3, 4, 5], [6], [0, 1], [], [], [], []]
        self.assertEqual(quiz4.order_dfs(adj_list, 2, []), [2,\
                                                0, 3, 4, 5, 1, 6])

    def test_order_dfs_4(self):
        adj_list = [[3], [6], [1, 2], [], [], [], []]
        self.assertEqual(quiz4.order_dfs(adj_list, 2, []), [2, 1, 6])

    def test_order_dfs_5(self):
        adj_list = [[3, 4], [7], [0, 2], [], [], []]
        self.assertEqual(quiz4.order_dfs(adj_list, 2, []), [2, 0, 3, 4])


if __name__ == "__main__":
    unittest.main()
