# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Winter 2021

import unittest

import pset7


class TestToAdjMatrix(unittest.TestCase):

    def test_to_adj_matrix_1(self):
        self.assertEqual(pset7.to_adj_matrix([[1, 2], \
                                              [0, 2], \
                                              [0, 1]]),
                         [[0, 1, 1], \
                          [1, 0, 1], \
                          [1, 1, 0]])

    def test_to_adj_matrix_2(self):
        self.assertEqual(pset7.to_adj_matrix([[2, 2], \
                                              [1, 2], \
                                              [2, 1], \
                                              [3, 2]]),
                         [[0, 0, 1, 0], \
                          [0, 1, 1, 0], \
                          [0, 1, 1, 0], \
                          [0, 0, 1, 1]])

    def test_to_adj_matrix_3(self):
        self.assertEqual(pset7.to_adj_matrix([[3, 4], \
                                              [4, 7], \
                                              [2, 1], \
                                              [2, 2]]),
                         [[0, 0, 0, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 1],
                          [0, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0]])

    def test_to_adj_matrix_4(self):
        self.assertEqual(pset7.to_adj_matrix([[5, 5], \
                                              [3, 6], \
                                              [3, 2], \
                                              [5, 6], \
                                              [7, 8]]),
                         [[0, 0, 0, 0, 0, 1, 0, 0, 0], \
                          [0, 0, 0, 1, 0, 0, 1, 0, 0], \
                          [0, 0, 1, 1, 0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0, 1, 1, 0, 0], \
                          [0, 0, 0, 0, 0, 0, 0, 1, 1], \
                          [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]])

    def test_to_adj_matrix_5(self):
        self.assertEqual(pset7.to_adj_matrix([[10, 5], \
                                              [7, 7], \
                                              [7, 1], \
                                              [3, 2], \
                                              [6, 7], \
                                              [9, 3]]),
                         [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


class TestToAdjList(unittest.TestCase):

    def test_to_adj_list_1(self):
        matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertEqual(pset7.to_adj_list(matrix), [[1, 2], [0, 2], [0, 1]])

    def test_to_adj_list_2(self):
        matrix = [[0, 2, 2, 3], [2, 2, 1, 1], [1, 1, 0, 3]]
        self.assertEqual(pset7.to_adj_list(matrix), [[], [2], [0, 1]])

    def test_to_adj_list_3(self):
        matrix = [[2, 2, 2, 3], [2, 1, 5, 1, 6], [4, 6, 4, 3]]
        self.assertEqual(pset7.to_adj_list(matrix), [[], [1], []])

    def test_to_adj_list_4(self):
        matrix = [[4, 4, 4, 13], [7, 10, 6, 9], [1, 1, 0, 3]]
        self.assertEqual(pset7.to_adj_list(matrix), [[], [], [0, 1]])

    def test_to_adj_list_5(self):
        matrix = [[0, 2, 2, 3], [3, 3, 1], [1, 3, 0, 3]]
        self.assertEqual(pset7.to_adj_list(matrix), [[], [2], [0]])


class TestOrderBFS(unittest.TestCase):

    def test_order_bfs_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.order_bfs(adj_list, 3), [3, 1, 2, 0])

    def test_order_bfs_2(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2], [2, 1]]
        self.assertEqual(pset7.order_bfs(adj_list, 4), [4, 2, 1, 0, 3])

    def test_order_bfs_3(self):
        adj_list = [[3, 1], [1, 3], [1, 3], [0, 2], [4, 3], [0, 1]]
        self.assertEqual(pset7.order_bfs(adj_list, 5), [5, 0, 1, 3, 2])

    def test_order_bfs_4(self):
        adj_list = [[1, 2], [0, 1], [0, 2], [0, 2]]
        self.assertEqual(pset7.order_bfs(adj_list, 2), [2, 0, 1])

    def test_order_bfs_5(self):
        adj_list = [[0, 2], [0, 5], [2, 3], [2, 0]]
        self.assertEqual(pset7.order_bfs(adj_list, 2), [2, 3, 0])


class TestOrderDFS(unittest.TestCase):

    def test_order_dfs_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.order_dfs(adj_list, 2, []), [2, 0, 1, 3])

    def test_order_dfs_2(self):
        adj_list = [[3, 2], [1, 3], [1, 3], [0, 2], [4, 3], [0, 1]]

        self.assertEqual(pset7.order_dfs(adj_list, 5, []), [5, 0, 3, 2, 1])

    def test_order_dfs_3(self):
        adj_list = [[3, 2], [3, 6], [2, 3], [2, 2]]
        self.assertEqual(pset7.order_dfs(adj_list, 2, []), [2, 3])

    def test_order_dfs_4(self):
        adj_list = [[1, 2], [0, 3], [1, 3], [2, 2]]
        self.assertEqual(pset7.order_dfs(adj_list, 3, []), [3, 2, 1, 0])

    def test_order_dfs_5(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.order_dfs(adj_list, 3, []), [3, 1, 0, 2])


class TestHasCycle(unittest.TestCase):

    def test_has_cycle_1(self):
        adj_list = [[1, 2], [0, 3], [0, 3], [1, 2]]
        self.assertEqual(pset7.has_cycle(adj_list, 0, []), True)

    def test_has_cycle_2(self):
        adj_list = [[2, 3], [2, 3], [0, 4], [4, 3], [1, 2], [2, 0]]
        self.assertEqual(pset7.has_cycle(adj_list, 4, []), True)

    def test_has_cycle_3(self):
        adj_list = [[1, 2], [], []]
        self.assertEqual(pset7.has_cycle(adj_list, 0, []), False)

    def test_has_cycle_4(self):
        adj_list = [[1, 2], [2, 3], [0, 3]]
        self.assertEqual(pset7.has_cycle(adj_list, 1, []), True)

    def test_has_cycle_5(self):
        adj_list = [[3, 1], [2, 1], [], []]
        self.assertEqual(pset7.has_cycle(adj_list, 1, []), False)


class TestCountComponents(unittest.TestCase):

    def test_count_components_1(self):
        adj_list = [[1], [0], [3], [2], [5], [4]]
        self.assertEqual(pset7.count_components(adj_list), 3)

    def test_count_components_2(self):
        adj_list = [[4], [5], [4], [2], [0], [0]]
        self.assertEqual(pset7.count_components(adj_list), 4)

    def test_count_components_3(self):
        adj_list = [[1], [3], [4], [0], [4], [1]]
        self.assertEqual(pset7.count_components(adj_list), 3)

    def test_count_components_4(self):
        adj_list = [[5], [4], [3], [2], [2], [0]]
        self.assertEqual(pset7.count_components(adj_list), 2)

    def test_count_components_5(self):
        adj_list = [[3], [2], [0], [2], [3], [3]]
        self.assertEqual(pset7.count_components(adj_list), 4)


if __name__ == "__main__":
    unittest.main()
