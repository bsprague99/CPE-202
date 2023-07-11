# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2021

import unittest

import pset5
from pset5 import ListNode  # only allowed uses of from ... import

class TestQueueConstructor(unittest.TestCase):

    def test_queue_constructor_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_constructor_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(4, None))))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(4, None))))
        self.assertEqual(queue.tail, ListNode(4, None))

    def test_queue_constructor_3(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(5, None))))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(5, None))))
        self.assertEqual(queue.tail, ListNode(5, None))

    def test_queue_constructor_4(self):
        queue = pset5.Queue(ListNode(2, ListNode(4, ListNode(6, None))))
        self.assertEqual(queue.head,
                         ListNode(2, ListNode(4, ListNode(6, None))))
        self.assertEqual(queue.tail, ListNode(6, None))

    def test_queue_constructor_5(self):
        queue = pset5.Queue(ListNode(10, ListNode(20, ListNode(30, None))))
        self.assertEqual(queue.head,
                         ListNode(10, ListNode(20, ListNode(30, None))))
        self.assertEqual(queue.tail, ListNode(30, None))


class TestQueueEquals(unittest.TestCase):

    def test_queue_equals_1(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        qy = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(qx, qy)

    def test_queue_equals_2(self):
        qx = pset5.Queue(ListNode(11, ListNode(22, ListNode(33, None))))
        qy = pset5.Queue(ListNode(33, ListNode(22, ListNode(11, None))))
        self.assertNotEqual(qx, qy)

    def test_queue_equals_3(self):
        qx = pset5.Queue(ListNode(10, ListNode(20, ListNode(30, None))))
        qy = pset5.Queue(ListNode(10, ListNode(20, ListNode(30, None))))
        self.assertEqual(qx, qy)

    def test_queue_equals_4(self):
        qx = pset5.Queue(ListNode(12, ListNode(22, ListNode(32, None))))
        qy = pset5.Queue(ListNode(32, ListNode(22, ListNode(12, None))))
        self.assertNotEqual(qx, qy)

    def test_queue_equals_5(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode \
            (3, ListNode(4, None)))))
        qy = pset5.Queue(ListNode(1, ListNode(2, ListNode \
            (3, ListNode(4, None)))))
        self.assertEqual(qx, qy)

class TestQueueEnqueue(unittest.TestCase):

    def test_queue_enqueue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(3)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_enqueue_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(30)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(30, None))))
        self.assertEqual(queue.tail, ListNode(30, None))

    def test_queue_enqueue_3(self):
        queue = pset5.Queue(ListNode(12, ListNode(22, None)))
        queue.enqueue(32)
        self.assertEqual(queue.head,
                         ListNode(12, ListNode(22, ListNode(32, None))))
        self.assertEqual(queue.tail, ListNode(32, None))

    def test_queue_enqueue_4(self):
        queue = pset5.Queue(ListNode(13, ListNode(23, None)))
        queue.enqueue(33)
        self.assertEqual(queue.head,
                         ListNode(13, ListNode(23, ListNode(33, None))))
        self.assertEqual(queue.tail, ListNode(33, None))

    def test_queue_enqueue_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        queue.enqueue(4)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, \
                                                          ListNode(4, None)))))
        self.assertEqual(queue.tail, ListNode(4, None))


class TestQueueDequeue(unittest.TestCase):

    def test_queue_dequeue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_dequeue_2(self):
        queue = pset5.Queue(ListNode(11, ListNode(21, ListNode(31, None))))
        self.assertEqual(queue.dequeue(), ListNode(11, None))
        self.assertEqual(queue.head, ListNode(21, ListNode(31, None)))
        self.assertEqual(queue.tail, ListNode(31, None))

    def test_queue_dequeue_3(self):
        queue = pset5.Queue(ListNode(10, ListNode(20, ListNode(30, None))))
        self.assertEqual(queue.dequeue(), ListNode(10, None))
        self.assertEqual(queue.head, ListNode(20, ListNode(30, None)))
        self.assertEqual(queue.tail, ListNode(30, None))

    def test_queue_dequeue_4(self):
        queue = pset5.Queue(ListNode(12, ListNode(22, ListNode(32, None))))
        self.assertEqual(queue.dequeue(), ListNode(12, None))
        self.assertEqual(queue.head, ListNode(22, ListNode(32, None)))
        self.assertEqual(queue.tail, ListNode(32, None))

    def test_queue_dequeue_5(self):
        queue = pset5.Queue(ListNode(13, ListNode(23, ListNode \
            (33, ListNode(43, None)))))
        self.assertEqual(queue.dequeue(), ListNode(13, None))
        self.assertEqual(queue.head, ListNode(23, ListNode(33, \
                                                        ListNode(43, None))))
        self.assertEqual(queue.tail, ListNode(43, None))


class TestSize(unittest.TestCase):

    def test_size_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(pset5.size(queue), 3)

    def test_size_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        self.assertEqual(pset5.size(queue), 2)

    def test_size_3(self):
        queue = pset5.Queue(ListNode(1, None))
        self.assertEqual(pset5.size(queue), 1)

    def test_size_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, \
                                        ListNode(3, ListNode(4, None)))))
        self.assertEqual(pset5.size(queue), 4)

    def test_size_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, \
                                ListNode(3, ListNode(4, ListNode(5, None))))))
        self.assertEqual(pset5.size(queue), 5)


class TestDequeueAll(unittest.TestCase):

    def test_dequeue_all_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 1), 2)
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))

    def test_dequeue_all_2(self):
        queue = pset5.Queue(ListNode(14, ListNode(24, ListNode(14,
                                                    ListNode(34, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 24), 1)
        self.assertEqual(queue.head, ListNode(14, ListNode(14, \
                                                          ListNode(34, None))))

    def test_dequeue_all_3(self):
        queue = pset5.Queue(ListNode(11, ListNode(21, ListNode(11,
                                                 ListNode(31, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 11), 2)
        self.assertEqual(queue.head, ListNode(21, ListNode(31, None)))

    def test_dequeue_all_4(self):
        queue = pset5.Queue(ListNode(10, ListNode(2, ListNode(10,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 10), 2)
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))

    def test_dequeue_all_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                             None))))
        self.assertEqual(pset5.dequeue_all(queue, 1), 2)
        self.assertEqual(queue.head, ListNode(2, None))


class TestQueueFlip(unittest.TestCase):

    def test_flip_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_flip_2(self):
        queue = pset5.Queue(ListNode(11, ListNode(21, ListNode(31, None))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(31, ListNode(21, ListNode(11, None))))
        self.assertEqual(queue.tail, ListNode(11, None))

    def test_flip_3(self):
        queue = pset5.Queue(ListNode(11, ListNode(12, ListNode(13, None))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(13, ListNode(12, ListNode(11, None))))
        self.assertEqual(queue.tail, ListNode(11, None))

    def test_flip_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(2, ListNode(1, None)))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_flip_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, \
                                                ListNode(4, None)))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(4, ListNode(3, ListNode(2,\
                                                    ListNode(1, None)))))
        self.assertEqual(queue.tail, ListNode(1, None))


class TestSiftUp(unittest.TestCase):

    def test_sift_up_1(self):
        self.assertEqual(pset5.sift_up([7, 6, 5, 4, 3, 2, 8], 6),
                         [8, 6, 7, 4, 3, 2, 5])

    def test_sift_up_2(self):
        self.assertEqual(pset5.sift_up([7, 6, 5, 4, 3, 2, 8], 2),
                         [7, 6, 5, 4, 3, 2, 8])

    def test_sift_up_3(self):
        self.assertEqual(pset5.sift_up([7, 6, 5, 4, 3, 2], 3),
                         [7, 6, 5, 4, 3, 2])

    def test_sift_up_4(self):
        self.assertEqual(pset5.sift_up([5, 4, 3, 2, 8], 1),
                         [5, 4, 3, 2, 8])

    def test_sift_up_5(self):
        self.assertEqual(pset5.sift_up([7, 6, 10, 4, 3, 2], 4),
                         [7, 6, 10, 4, 3, 2])


class TestSiftDown(unittest.TestCase):

    def test_sift_down_1(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 0),
                         [7, 5, 6, 1, 4, 3, 2])

    def test_sift_down_2(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 1),
                         [1, 7, 6, 5, 4, 3, 2])

    def test_sift_down_3(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 2),
                         [1, 7, 6, 5, 4, 3, 2])

    def test_sift_down_4(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 3),
                         [1, 7, 6, 5, 4, 3, 2])

    def test_sift_down_5(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 4),
                         [1, 7, 6, 5, 4, 3, 2])


class TestHeapify(unittest.TestCase):

    def test_heapify_1(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 7]),
                         [7, 5, 6, 4, 2, 1, 3])

    def test_heapify_2(self):
        self.assertEqual(pset5.heapify([2, 4, 6, 8, 9, 10]),
                         [10, 9, 6, 8, 4, 2])

    def test_heapify_3(self):
        self.assertEqual(pset5.heapify([10, 20, 30, 40, 50, 60, 70]),
                         [70, 50, 60, 40, 20, 10, 30])

    def test_heapify_4(self):
        self.assertEqual(pset5.heapify([11, 21, 31, 41, 51, 61, 71]),
                         [71, 51, 61, 41, 21, 11, 31])

    def test_heapify_5(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4]),
                         [4, 2, 3, 1])


class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 7),
                         [7, 5, 6, 3, 2, 1, 4])

    def test_insert_2(self):
        self.assertEqual(pset5.insert([61, 51, 41, 31, 21, 11], 71),
                         [71, 51, 61, 31, 21, 11, 41])

    def test_insert_3(self):
        self.assertEqual(pset5.insert([62, 52, 42, 32, 22, 12], 72),
                         [72, 52, 62, 32, 22, 12, 42])

    def test_insert_4(self):
        self.assertEqual(pset5.insert([4, 3, 2, 1], 8),
                         [8, 4, 2, 1, 3])

    def test_insert_5(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2], 2),
                         [6, 5, 4, 3, 2, 2])


class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        self.assertEqual(pset5.remove([7, 6, 5, 4, 3, 2, 1]),
                         (7, [6, 4, 5, 1, 3, 2]))

    def test_remove_2(self):
        self.assertEqual(pset5.remove([71, 61, 51, 41, 31, 21, 11]),
                         (71, [61, 41, 51, 11, 31, 21]))

    def test_remove_3(self):
        self.assertEqual(pset5.remove([72, 62, 52, 42, 32, 22, 12]),
                         (72, [62, 42, 52, 12, 32, 22]))

    def test_remove_4(self):
        self.assertEqual(pset5.remove([7, 6, 5, 4, 3]),
                         (7, [6, 4, 5, 3]))

    def test_remove_5(self):
        self.assertEqual(pset5.remove([9, 6, 5, 2, 1]),
                         (9, [6, 2, 5, 1]))


if __name__ == "__main__":
    unittest.main()
