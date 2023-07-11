# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Winter 2021

import unittest

import pset1
from pset1 import ListNode  # only allowed use of from ... import


class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 4, 0),
                         ListNode(4, ListNode(1, ListNode(2, ListNode(3, None)))))

    def test_insert_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 3, 0),
                         ListNode(3, ListNode(1, ListNode(2, ListNode(3, None)))))

    def test_insert_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 4, 1),
                         ListNode(1, ListNode(4, ListNode(2, ListNode(3, None)))))

    def test_insert_4(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 4, 2),
                         ListNode(1, ListNode(2, ListNode(4, ListNode(3, None)))))

    def test_insert_5(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 4, 3),
                         ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))


class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 0),
                         ListNode(2, ListNode(3, None)))

    def test_remove_2(self):
        head = ListNode(1, ListNode(4, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 2),
                         ListNode(1, ListNode(4, None)))

    def test_remove_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 1),
                         ListNode(1, ListNode(3, None)))

    def test_remove_4(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 2),
                         ListNode(1, ListNode(2, None)))

    def test_remove_5(self):
        head = ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
        self.assertEqual(pset1.remove(head, 3),
                         ListNode(2, ListNode(3, ListNode(4, None))))


class TestIndex(unittest.TestCase):

    def test_index_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.index(head, 2), 1)

    def test_index_2(self):
        head = ListNode(5, ListNode(6, ListNode(7, None)))
        self.assertEqual(pset1.index(head, 7), 2)

    def test_index_3(self):
        head = ListNode(3, ListNode(5, ListNode(7, None)))
        self.assertEqual(pset1.index(head, 3), 0)

    def test_index_4(self):
        head = ListNode(8, ListNode(2, ListNode(2, ListNode(5, None))))
        self.assertEqual(pset1.index(head, 8), 0)

    def test_index_5(self):
        head = ListNode(1, ListNode(7, ListNode(4, ListNode(5, None))))
        self.assertEqual(pset1.index(head, 5), 3)


class TestConcat(unittest.TestCase):

    def test_concat_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, ListNode(5, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                                                      ListNode(5, None))))))

    def test_concat_2(self):
        xs = ListNode(2, ListNode(5, ListNode(6, None)))
        ys = ListNode(2, ListNode(4, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(2, ListNode(5, ListNode(6, ListNode(2,
                                                                      ListNode(4, None))))))

    def test_concat_3(self):
        xs = ListNode(10, ListNode(20, ListNode(30, None)))
        ys = ListNode(40, ListNode(50, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(10, ListNode(20, ListNode(30, ListNode(40,
                                                                         ListNode(50, None))))))

    def test_concat_4(self):
        xs = ListNode(11, ListNode(21, ListNode(31, None)))
        ys = ListNode(41, ListNode(51, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(11, ListNode(21, ListNode(31, ListNode(41,
                                                                         ListNode(51, None))))))

    def test_concat_5(self):
        xs = ListNode(4, ListNode(5, ListNode(6, None)))
        ys = ListNode(7, ListNode(8, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(4, ListNode(5, ListNode(6, ListNode(7,
                                                                      ListNode(8, None))))))


class TestSumList(unittest.TestCase):

    def test_sum_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.sum_list(head), 6)

    def test_sum_list_2(self):
        head = ListNode(2, ListNode(2, ListNode(2, None)))
        self.assertEqual(pset1.sum_list(head), 6)

    def test_sum_list_3(self):
        head = ListNode(2, ListNode(4, ListNode(8, None)))
        self.assertEqual(pset1.sum_list(head), 14)

    def test_sum_list_4(self):
        head = ListNode(1, ListNode(1, ListNode(1, None)))
        self.assertEqual(pset1.sum_list(head), 3)

    def test_sum_list_5(self):
        head = ListNode(0, ListNode(0, ListNode(1, None)))
        self.assertEqual(pset1.sum_list(head), 1)


class TestExpList(unittest.TestCase):

    def test_exp_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.exp_list(head, 3),
                         ListNode(1, ListNode(8, ListNode(27, None))))

    def test_exp_list_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.exp_list(head, 2),
                         ListNode(1, ListNode(4, ListNode(8, None))))

    def test_exp_list_3(self):
        head = ListNode(1, ListNode(1, ListNode(1, None)))
        self.assertEqual(pset1.exp_list(head, 3),
                         ListNode(1, ListNode(1, ListNode(1, None))))

    def test_exp_list_4(self):
        head = ListNode(1, ListNode(3, ListNode(4, None)))
        self.assertEqual(pset1.exp_list(head, 3),
                         ListNode(1, ListNode(8, ListNode(64, None))))

    def test_exp_list_5(self):
        head = ListNode(-1, ListNode(1, ListNode(-1, None)))
        self.assertEqual(pset1.exp_list(head, 5),
                         ListNode(-1, ListNode(1, ListNode(-1, None))))


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2,
                                                            ListNode(3, None)))))
        self.assertEqual(pset1.fibonacci(5), head)

    def test_fibonacci_2(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2, None))))
        self.assertEqual(pset1.fibonacci(4), head)

    def test_fibonacci_3(self):
        head = ListNode(0, ListNode(1, ListNode(1, None)))
        self.assertEqual(pset1.fibonacci(3), head)

    def test_fibonacci_4(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2,
                                                            ListNode(3, ListNode(5, ListNode(8, None)))))))
        self.assertEqual(pset1.fibonacci(7), head)

    def test_fibonacci_5(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2,
                                                            ListNode(3, ListNode(5, None))))))
        self.assertEqual(pset1.fibonacci(6), head)



class TestZipLists(unittest.TestCase):

    def test_zip_lists_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(4, ListNode(2,
                                  ListNode(3, None)))))

    def test_zip_lists_2(self):
        xs = ListNode(1, ListNode(2, None))
        ys = ListNode(5, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(5, ListNode(2, None))))

    def test_zip_lists_3(self):
        xs = ListNode(6, ListNode(2, ListNode(3, None)))
        ys = ListNode(1, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(6, ListNode(1, ListNode(2,
                                                          ListNode(3, None)))))

    def test_zip_lists_4(self):
        xs = ListNode(6, ListNode(1, ListNode(3, None)))
        ys = ListNode(4, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(6, ListNode(4, ListNode(1,
                                                          ListNode(3, None)))))

    def test_zip_lists_5(self):
        xs = ListNode(5, ListNode(1, ListNode(2, None)))
        ys = ListNode(4, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(5, ListNode(4, ListNode(1,
                                                          ListNode(2, None)))))



class TestUnzipList(unittest.TestCase):

    def test_unzip_list_1(self):
        head = ListNode(1, ListNode(4, ListNode(2, ListNode(5, ListNode(3, None)))))

        unzipped = (ListNode(1, ListNode(2, ListNode(3, None))), ListNode(4, ListNode(5, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_2(self):
        head = ListNode(2, ListNode(5, ListNode(3, ListNode(6, ListNode(4, None)))))

        unzipped = (ListNode(2, ListNode(3, ListNode(4, None))), ListNode(5, ListNode(6, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_3(self):
        head = ListNode(3, ListNode(6, ListNode(4, ListNode(7, ListNode(5, None)))))

        unzipped = (ListNode(3, ListNode(4, ListNode(5, None))), ListNode(6, ListNode(7, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_4(self):
        head = ListNode(4, ListNode(7, ListNode(5, ListNode(8, ListNode(6, None)))))

        unzipped = (ListNode(4, ListNode(5, ListNode(6, None))), ListNode(7, ListNode(8, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_5(self):
        head = ListNode(5, ListNode(8, ListNode(6, ListNode(9, ListNode(7, None)))))

        unzipped = (ListNode(5, ListNode(6, ListNode(7, None))), ListNode(8, ListNode(9, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)


if __name__ == "__main__":
    unittest.main()
