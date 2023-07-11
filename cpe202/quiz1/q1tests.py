# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Quiz I
# Term:         Winter 2021

import unittest

import quiz1
from quiz1 import ListNode  # only allowed use of from ... import


class TestCreateRing(unittest.TestCase):
    """
    Because ListNode.__eq__ is not provided, do not compare ListNode objects
    directly. Instead, as in the example, you may compare the integer values of
    the head node and that of the tail's reference, which should be equal.
    """

    def test_create_ring_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        tail = quiz1.create_ring(head)
        self.assertEqual(head.val, tail.ref.val)

    def test_create_ring_2(self):
        head = ListNode(1, ListNode(2,\
                                    ListNode(3, \
                                             ListNode(4, None))))
        tail = quiz1.create_ring(head)
        self.assertEqual(head.val, tail.ref.val)

    def test_create_ring_3(self):
        head = ListNode(1, ListNode(2, ListNode(3,\
                                                ListNode(4, \
                                                         ListNode(5,\
                                                                  None)))))
        head = quiz1.create_ring(head).ref
        tail = quiz1.create_ring(head)
        self.assertEqual(head.val, tail.ref.val)

    def test_create_ring_4(self):
        head = ListNode(1, \
                        ListNode(2, \
                                 ListNode(3,\
                                        ListNode(4,\
                                                ListNode(5,\
                                                        ListNode(6,\
                                                                None))))))
        tail = quiz1.create_ring(head)
        self.assertEqual(head.val, tail.ref.val)

    def test_create_ring_5(self):  # Don't forget to check if Ring is empty!
        tail = quiz1.create_ring(None)
        self.assertEqual(None, tail)


class TestAreRingsEqual(unittest.TestCase):

    def test_are_rings_equal_1(self):
        xs = quiz1.create_ring(ListNode(1, ListNode(2, None))).ref
        ys = quiz1.create_ring(ListNode(1, ListNode(3, None))).ref
        self.assertFalse(quiz1.are_rings_equal(xs, ys))

    def test_are_rings_equal_2(self):
        xs = quiz1.create_ring(ListNode(1, ListNode(2, ListNode(3, None)))).ref
        ys = quiz1.create_ring(ListNode(1, ListNode(2, None))).ref
        self.assertFalse(quiz1.are_rings_equal(xs, ys))

    def test_are_rings_equal_3(self):
        xs = quiz1.create_ring(ListNode(1, ListNode(2, None))).ref
        ys = quiz1.create_ring(ListNode(1, ListNode(2, None))).ref
        self.assertTrue(quiz1.are_rings_equal(xs, ys))

    def test_are_rings_equal_4(self):
        xs = quiz1.create_ring(ListNode(1, ListNode(3, ListNode(3, None)))).ref
        ys = quiz1.create_ring(ListNode(1, ListNode(3, ListNode(3, None)))).ref
        self.assertTrue(quiz1.are_rings_equal(xs, ys))

    def test_are_rings_equal_5(self):
        xs = quiz1.create_ring(ListNode(1, ListNode(2, None))).ref
        ys = quiz1.create_ring(ListNode(2, ListNode(2, None))).ref
        self.assertFalse(quiz1.are_rings_equal(xs, ys))

    def test_are_rings_equal_6(self):
        xs = quiz1.create_ring(ListNode(None, None)).ref
        ys = quiz1.create_ring(ListNode(None, None)).ref
        self.assertTrue(quiz1.are_rings_equal(xs, ys))

if __name__ == "__main__":
    unittest.main()
