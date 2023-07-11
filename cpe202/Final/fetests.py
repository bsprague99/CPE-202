# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Final Exam
# Term:         Winter 2021

import unittest

import final
from final import ListNode as LN  # only allowed uses of from ... import


class TestBitwiseAnd(unittest.TestCase):

    def test_bitwise_and_1(self):
        xs = LN(0, LN(1, LN(1, LN(0, None))))
        ys = LN(1, LN(1, LN(0, LN(0, None))))
        zs = LN(0, LN(1, LN(0, LN(0, None))))
        self.assertEqual(final.bitwise_and(xs, ys), zs)

    def test_bitwise_and_2(self):
        xs = LN(1, LN(1, LN(1, LN(0, None))))
        ys = LN(1, LN(0, LN(0, LN(0, None))))
        zs = LN(1, LN(0, LN(0, LN(0, None))))
        self.assertEqual(final.bitwise_and(xs, ys), zs)

    def test_bitwise_and_3(self):
        xs = LN(0, LN(1, LN(1, LN(0, None))))
        ys = LN(0, LN(1, LN(0, LN(0, None))))
        zs = LN(0, LN(1, LN(0, LN(0, None))))
        self.assertEqual(final.bitwise_and(xs, ys), zs)

    def test_bitwise_and_4(self):
        xs = LN(0, LN(0, LN(1, LN(0, None))))
        ys = LN(1, LN(1, LN(0, LN(1, None))))
        zs = LN(0, LN(0, LN(0, LN(0, None))))
        self.assertEqual(final.bitwise_and(xs, ys), zs)

    def test_bitwise_and_5(self):
        xs = LN(1, LN(1, LN(1, LN(1, None))))
        ys = LN(0, LN(1, LN(0, LN(1, None))))
        zs = LN(0, LN(1, LN(0, LN(1, None))))
        self.assertEqual(final.bitwise_and(xs, ys), zs)




class TestHasTriangle(unittest.TestCase):

    def test_has_triangle_01(self):
        graph = (LN(1, LN(2, None)),
                 LN(0, LN(3, LN(4, None))),
                 LN(0, LN(5, None)),
                 LN(1, LN(4, None)),
                 LN(1, LN(3, LN(5, None))),
                 LN(2, LN(4, None)))
        self.assertTrue(final.has_triangle(graph))

    def test_has_triangle_02(self):
        graph = (LN(1, LN(2, None)),
                 LN(0, LN(3, None)),
                 LN(0, LN(5, None)),
                 LN(1, LN(4, None)),
                 LN(3, LN(5, None)),
                 LN(2, LN(4, None)))
        self.assertFalse(final.has_triangle(graph))




if __name__ == "__main__":
    unittest.main()
