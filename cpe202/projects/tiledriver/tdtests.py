# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import unittest

import tiledriver
from tiledriver import PuzzleState as PS  # only allowed use of from ... import


class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((1, 2, 3, 0, 4, 5, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 2, 3, 6, 4, 5, 0, 7, 8), "K"),
                          PS((0, 2, 3, 1, 4, 5, 6, 7, 8), "J"),
                          PS((1, 2, 3, 4, 0, 5, 6, 7, 8), "H")])

    def test_make_adjacent_2(self):
        state = PS((1, 2, 3, 5, 4, 0, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 2, 3, 5, 0, 4, 6, 7, 8), "L"),
                          PS((1, 2, 3, 5, 4, 8, 6, 7, 0), "K"),
                          PS((1, 2, 0, 5, 4, 3, 6, 7, 8), "J")])

    def test_make_adjacent_3(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((0, 1, 2, 3, 4, 5, 6, 7, 8), "L"),
                          PS((1, 4, 2, 3, 0, 5, 6, 7, 8), "K"),
                          PS((1, 2, 0, 3, 4, 5, 6, 7, 8), "H")])

    def test_make_adjacent_4(self):
        state = PS((1, 2, 3, 4, 0, 5, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 2, 3, 0, 4, 5, 6, 7, 8), "L"),
                          PS((1, 2, 3, 4, 7, 5, 6, 0, 8), "K"),
                          PS((1, 0, 3, 4, 2, 5, 6, 7, 8), "J"),
                          PS((1, 2, 3, 4, 5, 0, 6, 7, 8), "H"),
                          ])

    def test_make_adjacent_5(self):
        state = PS((9, 2, 3, 5, 4, 0, 6, 7, 8), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((9, 2, 3, 5, 0, 4, 6, 7, 8), "L"),
                          PS((9, 2, 3, 5, 4, 8, 6, 7, 0), "K"),
                          PS((9, 2, 0, 5, 4, 3, 6, 7, 8), "J")])


class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3)))

    def test_is_solvable_3(self):
        self.assertTrue(tiledriver.is_solvable((3, 7, 1, 4, 0, 2, 6, 8, 5)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((2, 3, 0, 1)))

    def test_is_solvable_5(self):
        self.assertTrue(tiledriver.is_solvable((3, 0, 1, 2)))


class TestGetShortest(unittest.TestCase):

    def test_get_shortest_1(self):
        frontier = [PS((0, 2, 3, 1), "L"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.get_shortest(frontier), \
                         PS((0, 2, 3, 1), "L"))

    def test_get_shortest_2(self):
        frontier = [PS((0, 2, 3, 1), "K"), PS((0, 2, 3, 1), "JK")]
        self.assertEqual(tiledriver.get_shortest(frontier), \
                         PS((0, 2, 3, 1), "K"))

    def test_get_shortest_3(self):
        frontier = [PS((0, 2, 3, 1), "J"), PS((0, 2, 3, 1), "JK")]
        self.assertEqual(tiledriver.get_shortest(frontier), \
                         PS((0, 2, 3, 1), "J"))

    def test_get_shortest_4(self):
        frontier = [PS((1, 2, 3, 0), "J"), PS((1, 2, 3, 0), "JH")]
        self.assertEqual(tiledriver.get_shortest(frontier), \
                         PS((1, 2, 3, 0), "J"))

    def test_get_shortest_5(self):
        frontier = [PS((3, 2, 0, 1), "JH"), PS((3, 2, 0, 1), "J")]
        self.assertEqual(tiledriver.get_shortest(frontier), \
                         PS((3, 2, 0, 1), "J"))


class TestRemoveUnsolvable(unittest.TestCase):

    def test_remove_unsolvable_1(self):
        frontier = [PS((0, 2, 3, 1), "L"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.remove_unsolvable(frontier) \
                         , [PS((0, 2, 3, 1), "L"), PS((0, 2, 3, 1), "J")])

    def test_remove_unsolvable_2(self):
        frontier = [PS((0, 2, 1, 3), "L"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.remove_unsolvable(frontier) \
                         , [PS((0, 2, 3, 1), "J")])

    def test_remove_unsolvable_3(self):
        frontier = [PS((0, 2, 1, 3), "K"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.remove_unsolvable(frontier) \
                         , [PS((0, 2, 3, 1), "J")])

    def test_remove_unsolvable_4(self):
        frontier = [PS((0, 2, 1, 3), "H"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.remove_unsolvable(frontier) \
                         , [PS((0, 2, 3, 1), "J")])

    def test_remove_unsolvable_5(self):
        frontier = [PS((0, 2, 1, 3), "J"), PS((0, 2, 3, 1), "J")]
        self.assertEqual(tiledriver.remove_unsolvable(frontier) \
                         , [PS((0, 2, 3, 1), "J")])


class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)) \
                         , "LJHKLJ")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 0, 1)) \
                         , "JHKLJ")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 7, 1, 4, \
                                                  0, 2, 6, 8, 5)), "JHKKLJLJ")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 0, 1, 2)) \
                         , "LKHJL")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 7, 1, 4, \
                                                  2, 0, 6, 8, 5)), "LJHKKLJLJ")


class TestStateGenerator(unittest.TestCase):

    def test_state_generator_1(self):
        self.assertEqual(tiledriver.state_generator(0, -2, "K", \
                                        (0, 1, 2, 3)), PS((2, 1, 0, 3), "K"))

    def test_state_generator_2(self):
        self.assertEqual(tiledriver.state_generator(0, +1, "H",\
                                        (0, 1, 2, 3)), PS((1, 0, 2, 3), "H"))

    def test_state_generator_3(self):
        self.assertEqual(tiledriver.state_generator(0, -2, "KJ",\
                                            (0, 1, 2, 3)), None)

    def test_state_generator_4(self):
        self.assertEqual(tiledriver.state_generator(0, -2, "JK",\
                                            (0, 1, 2, 3)), None)

    def test_state_generator_5(self):
        self.assertEqual(tiledriver.state_generator(0, -2, "LH",\
                                            (0, 1, 2, 3)), None)


if __name__ == "__main__":
    unittest.main()
