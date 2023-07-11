# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz II
# Term:         Winter 2021

import unittest

import quiz2
from quiz2 import ListNode  # only allowed use of from ... import


class TestIsBalanced(unittest.TestCase):

    def test_is_balanced_1(self):
        self.assertTrue(quiz2.is_balanced("({[][]}[{}]())"))

    def test_is_balanced_2(self):
        self.assertFalse(quiz2.is_balanced("({[)"))

    def test_is_balanced_3(self):
        self.assertFalse(quiz2.is_balanced("(({[})"))

    def test_is_balanced_4(self):
        self.assertTrue(quiz2.is_balanced("({{[}}])"))

    def test_is_balanced_5(self):
        self.assertTrue(quiz2.is_balanced("((({{[]}})))"))


class TestIsZeroSum(unittest.TestCase):

    def test_is_zero_sum_1(self):
        head = ListNode(-3, ListNode(2, ListNode(1, None)))
        self.assertTrue(quiz2.is_zero_sum(head, 0))

    def test_is_zero_sum_2(self):
        head = ListNode(1, ListNode(-1, ListNode(-1, None)))
        self.assertFalse(quiz2.is_zero_sum(head, 0))

    def test_is_zero_sum_3(self):
        head = ListNode(3, ListNode(-3, ListNode(-1, None)))
        self.assertFalse(quiz2.is_zero_sum(head, 0))

    def test_is_zero_sum_4(self):
        head = ListNode(3, ListNode(-1, ListNode(-2, None)))
        self.assertTrue(quiz2.is_zero_sum(head, 0))

    def test_is_zero_sum_5(self):
        head = ListNode(5, ListNode(-5, ListNode(0, None)))
        self.assertTrue(quiz2.is_zero_sum(head, 0))


class TestCountWords(unittest.TestCase):

    def test_count_words_1(self):
        self.assertEqual(quiz2.count_words("python", 0), 1)

    def test_count_words_2(self):
        words = "computer science and software engineering"
        self.assertEqual(quiz2.count_words(words, 0), 5)

    def test_count_words_3(self):
        words = "If this test passes I will give Brenden 100%"
        self.assertEqual(quiz2.count_words(words, 0), 9)

    def test_count_words_4(self):
        words = "If you are reading this"
        self.assertEqual(quiz2.count_words(words, 0), 5)

    def test_count_words_5(self):
        words = "You are cool"
        self.assertEqual(quiz2.count_words(words, 0), 3)

    def test_count_words_6(self):
        words = ""
        self.assertEqual(quiz2.count_words(words, 0), 0)


if __name__ == "__main__":
    unittest.main()
