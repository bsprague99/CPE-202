# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VI
# Term:         Winter 2021

import unittest

import pset6
from pset6 import Entry  # only allowed use of from ... import


class TestHashKey(unittest.TestCase):

    def test_hash_key_1(self):
        self.assertEqual(pset6.hash_key(3, 3), 0)

    def test_hash_key_2(self):
        self.assertEqual(pset6.hash_key(6, 5), 1)

    def test_hash_key_3(self):
        self.assertEqual(pset6.hash_key(10, 7), 3)

    def test_hash_key_4(self):
        self.assertEqual(pset6.hash_key(0, 1), 0)

    def test_hash_key_5(self):
        with self.assertRaises(ZeroDivisionError):
            pset6.hash_key(1, 0)


class TestGetLoadFactor(unittest.TestCase):

    def test_get_load_factor_1(self):
        table = [None, Entry(1, "A", Entry(5, "B", None)), None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.5)

    def test_get_load_factor_2(self):
        table = [Entry(0, "A", None), Entry(5, "B", None), Entry(1,\
                                            "A", None), None, None]
        self.assertEqual(pset6.get_load_factor(table), 0.6)

    def test_get_load_factor_3(self):
        table = [None, Entry(1, "A", Entry(5, "B", None)), \
                 Entry(0, "G", None), None]
        self.assertEqual(pset6.get_load_factor(table), 0.75)

    def test_get_load_factor_4(self):
        table = [Entry(0, "A", None), Entry(5, "B", None), Entry(2,\
                                        "D", None), Entry(4, "F", None), None]
        self.assertEqual(pset6.get_load_factor(table), 0.8)

    def test_get_load_factor_5(self):
        table = [None, Entry(1, "A", None), Entry(0, "A", \
                                                  None), Entry(0, "A", None)]
        self.assertEqual(pset6.get_load_factor(table), 0.75)


class TestResize(unittest.TestCase):

    def test_resize_1(self):
        table = [Entry(0, "A", Entry(3, "B", Entry(6, "C", None))),
                 Entry(7, "D", Entry(1, "E", None)), None]
        resized = [Entry(7, "D", Entry(0, "A", None)), Entry(1, "E", None),
                   None, Entry(3, "B", None), None, None, Entry(6, "C", None)]
        self.assertEqual(pset6.resize(table, "chain"), resized)

    def test_resize_2(self):
        table = [Entry(0, "F", None), Entry(3, "G", None), Entry(8, "C", None)]
        resized = [Entry(0, "F", None), Entry(8, "C", None), None,
                   Entry(3, "G", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_3(self):
        table = [Entry(0, "A", None), Entry(3, "D", None), Entry(8, "G", None)]
        resized = [Entry(0, "A", None), Entry(8, "G", None), None,
                   Entry(3, "D", None), None, None, None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_4(self):
        table = [Entry(0, "B", None), Entry(8, "C", None)]
        resized = [Entry(0, "B", None), None, None, Entry(8, "C", None), None]
        self.assertEqual(pset6.resize(table, "probe"), resized)

    def test_resize_5(self):
        table = [Entry(2, "C", None)]
        resized = [None, None, Entry(2, "C", None)]
        self.assertEqual(pset6.resize(table, "probe"), resized)


class TestChainGet(unittest.TestCase):

    def test_chain_get_1(self):
        table = [Entry(3, "B", Entry(0, "A", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "A")

    def test_chain_get_2(self):
        table = [Entry(3, "X", Entry(0, "B", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 0), "B")

    def test_chain_get_3(self):
        table = [Entry(3, "D", Entry(0, "A", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 3), "D")

    def test_chain_get_4(self):
        table = [Entry(3, "I", Entry(0, "F", None)), None, None]
        self.assertEqual(pset6.chain_get(table, 3), "I")

    def test_chain_get_5(self):
        table = [Entry(4, "B", Entry(0, "A", None)), None, None, None]
        self.assertEqual(pset6.chain_get(table, 4), "B")


class TestChainInsert(unittest.TestCase):

    def test_chain_insert_1(self):
        table = [Entry(3, "C", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "A", None), Entry(8, "E", Entry(1, "B", None)),
                    None, Entry(3, "C", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)

    def test_chain_insert_2(self):
        table = [Entry(3, "W", Entry(0, "A", None)),
                 Entry(4, "D", Entry(1, "S", None)), None]
        inserted = [Entry(7, "E", Entry(0, "A", None)), Entry(1, "S", None)
            , None,
                    Entry(3, "W", None), Entry(4, "D", None), None, None]
        self.assertEqual(pset6.chain_insert(table, 7, "E"), inserted)

    def test_chain_insert_3(self):
        table = [Entry(0, "Z", None), Entry(1, "S", None)]
        inserted = [Entry(8, "E", Entry(0, "Z", None)), Entry(1, "S", None)]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)

    def test_chain_insert_4(self):
        table = [Entry(2, "Q", Entry(0, "C", None)),
                 Entry(3, "D", Entry(1, "B", None)), None]
        inserted = [Entry(0, "C", None), Entry(8, "E", Entry(1, "B", None)),
                    Entry(2, "Q", None), Entry(3, "D", None), None, None, None]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)

    def test_chain_insert_5(self):
        table = [Entry(0, "Z", None)]
        inserted = [Entry(0, "Z", None), None, Entry(8, "E", None)]
        self.assertEqual(pset6.chain_insert(table, 8, "E"), inserted)


class TestChainRemove(unittest.TestCase):

    def test_chain_remove_1(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "A", None)), None, None])

    def test_chain_remove_2(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 6),
                         [Entry(3, "B", Entry(0, "A", None)), None, None])

    def test_chain_remove_3(self):
        table = [Entry(6, "C", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 0),
                         [Entry(6, "C", Entry(3, "B", None)), None, None])

    def test_chain_remove_4(self):
        table = [Entry(6, "F", Entry(3, "B", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 6),
                         [Entry(3, "B", Entry(0, "A", None)), None, None])

    def test_chain_remove_5(self):
        table = [Entry(6, "C", Entry(3, "F", Entry(0, "A", None))), None, None]
        self.assertEqual(pset6.chain_remove(table, 3),
                         [Entry(6, "C", Entry(0, "A", None)), None, None])


class TestProbeGet(unittest.TestCase):

    def test_probe_get_1(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), None]
        self.assertEqual(pset6.probe_get(table, 3), "B")

    def test_probe_get_2(self):
        table = [Entry(0, "A", None), Entry(3, "B", None), None]
        self.assertEqual(pset6.probe_get(table, 0), "A")

    def test_probe_get_3(self):
        table = [Entry(0, "A", None), Entry(6, "F", None), None, None]
        self.assertEqual(pset6.probe_get(table, 6), "F")

    def test_probe_get_4(self):
        table = [Entry(1, "A", None), Entry(3, "B", None), None]
        self.assertEqual(pset6.probe_get(table, 1), "A")

    def test_probe_get_5(self):
        table = [Entry(0, "A", None), Entry(8, "l", None), None, None, \
                 None]
        self.assertEqual(pset6.probe_get(table, 8), "l")


class TestProbeInsert(unittest.TestCase):

    def test_probe_insert_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        inserted = [Entry(0, "A", None), Entry(1, "B", None),
                    Entry(2, "C", None), None, None, None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "C"), inserted)

    def test_probe_insert_2(self):
        table = [Entry(0, "A", None), Entry(2, "B", None), None]
        inserted = [Entry(0, "A", None), None, Entry(2, "B", None),
                    Entry(3, "f", None), None, None, None]
        self.assertEqual(pset6.probe_insert(table, 3, "f"), inserted)

    def test_probe_insert_3(self):
        table = [Entry(0, "A", None), None]
        inserted = [Entry(0, "A", None), None,
                    Entry(2, "A", None), None, None]
        self.assertEqual(pset6.probe_insert(table, 2, "A"), inserted)

    def test_probe_insert_4(self):
        table = [Entry(1, "B", None), None]
        inserted = [None, Entry(1, "B", None),
                    None, Entry(3, "C", None), None]
        self.assertEqual(pset6.probe_insert(table, 3, "C"), inserted)

    def test_probe_insert_5(self):
        table = [Entry(2, "A", None), None]
        inserted = [None, None, Entry(2, "A", None),
                    None, Entry(4, "5", None)]
        self.assertEqual(pset6.probe_insert(table, 4, "5"), inserted)


class TestProbeRemove(unittest.TestCase):

    def test_probe_remove_1(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "B", None), None])

    def test_probe_remove_2(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), None]
        self.assertEqual(pset6.probe_remove(table, 1),
                         [Entry(0, "A", None), Entry(None, None, None), None])

    def test_probe_remove_3(self):
        table = [Entry(0, "A", None), Entry(1, "B", None), Entry(3, "F", None)]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "B", None), \
                          Entry(3, "F", None)])

    def test_probe_remove_4(self):
        table = [Entry(0, "A", None), Entry(1, "C", None)]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "C", None)])

    def test_probe_remove_5(self):
        table = [Entry(0, "A", None), Entry(1, "D", None), None]
        self.assertEqual(pset6.probe_remove(table, 0),
                         [Entry(None, None, None), Entry(1, "D", None), None])

if __name__ == "__main__":
    unittest.main()
