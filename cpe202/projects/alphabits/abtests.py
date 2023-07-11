# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

import unittest

import alphabits
from alphabits import HuffmanNode as H  # only allowed use of from ... import


class TestCreateTree(unittest.TestCase):
    def test_create_tree_1(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFE"), root)

    def test_create_tree_2(self):
        root = H('E', 4, H('E', 2, None, None), H('F', 2, H('F', 1, None, \
                                        None), H('R', 1, None, None)))
        self.assertEqual(alphabits.create_tree('FREE'), root)

    def test_create_tree_3(self):
        root = H('A', 4, H('A', 2, H('A', 1, None, None), H('E' \
                                 , 1, None, None)), H('R', 2, H('R', \
                                  1, None, None),
                               H('T', 1, None, None)))
        self.assertEqual(alphabits.create_tree('TREA'), root)

    def test_create_tree_4(self):
        root = H('A', 4, H('A', 2, H('A', 1, None, None), H('E', 1, \
                                    None, None)), H('F', 2, H('F', 1, None, \
                                  None), H('L', 1, None, None)))
        self.assertEqual(alphabits.create_tree('FLEA'), root)

    def test_create_tree_5(self):
        root = H('A', 4, H('A', 2, None, None), H('B', 2, H('B', \
               1, None, None), H('N', 1, None, None)))
        self.assertEqual(alphabits.create_tree('BANA'), root)
    def test_create_tree_6(self):
        root = None
        self.assertEqual(alphabits.create_tree(""), root)

class TestEncode(unittest.TestCase):

    def test_encode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BE", root), "10100")

    def test_encode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("FA", root), "111100")

    def test_encode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BAA", root), "1010100100")

    def test_encode_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BEBEBE",\
                                          root), "101001010010100")

    def test_encode_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("CEBE", root), "1011010100")

class TestFrequency(unittest.TestCase):

    def test_frequency_1(self):
        chars = "DEADBEEFCAFE"
        self.assertEqual(alphabits.frequency(chars), \
                         [H("A", 2, None, None), H("B", 1, None, None),
                            H("C", 1, None, None), H("D", 2, None, None),
                            H("E", 4, None, None), H("F", 2, None, None)])

    def test_frequency_2(self):
        chars = "TEST"
        self.assertEqual(alphabits.frequency(chars), \
                         [H("E", 1, None, None), H("S", 1, None, None),
                                        H("T", 2, None, None)])

    def test_frequency_3(self):
        chars = "HEY"
        self.assertEqual(alphabits.frequency(chars), \
                         [H("E", 1, None, None), H("H", 1, None, None),
                                         H("Y", 1, None, None)])

    def test_frequency_4(self):
        chars = "EEE"
        self.assertEqual(alphabits.frequency(chars), [H("E", 3, None, None)])

    def test_frequency_5(self):
        chars = "AAA"
        self.assertEqual(alphabits.frequency(chars), [H("A", 3, None, None)])


class TestRemoveTwo(unittest.TestCase):
    def test_remove_two_11(self):
        heap_list = [H("D", 12, None, None), H("F", 12, None, None), \
                     H("E", 12, None, None)]

        self.assertEqual(alphabits.remove_two1(heap_list),
                         ([H("F", 12, None, None)], H("D", 12, \
                                                      None, None), H("E", 12, None, None)))


class TestRemoveTwo(unittest.TestCase):

    def test_remove_two_1(self):
        heap_list = [H("D", 12, None, None), H("F", 12, None, None), \
                     H("E", 12, None, None)]

        self.assertEqual(alphabits.remove_two(heap_list),
                         ([H("F", 12, None, None)], H("D", 12,\
                    None, None), H("E", 12, None, None)))

    def test_remove_two_2(self):
        heap_list = [H("A", 12, None, None), H("F", 12, \
                    None, None), H("C", 12, None, None)]

        self.assertEqual(alphabits.remove_two(heap_list),
                         ([H("F", 12, None, None)], H("A", 12,\
                        None, None), H("C", 12, None, None)))

    def test_remove_two_3(self):
        heap_list = [H("R", 12, None, None), H("F", 12, None, \
                        None), H("C", 12, None, None)]

        self.assertEqual(alphabits.remove_two(heap_list),
                         ([H("R", 12, None, None)], H("C", 12,\
                    None, None), H("F", 12, None, None)))

    def test_remove_two_4(self):
        heap_list = [H("E", 12, None, None), H("F", 12, \
                None, None), H("C", 12, None, None)]

        self.assertEqual(alphabits.remove_two(heap_list),
                         ([H("E", 12, None, None)], H("C", 12, \
                None, None), H("F", 12, None, None)))

    def test_remove_two_5(self):
        heap_list = [H("Q", 12, None, None), H("F", 12,\
                    None, None), H("C", 12, None, None)]

        self.assertEqual(alphabits.remove_two(heap_list),
                         ([H("Q", 12, None, None)], H("C",\
                        12, None, None), H("F", 12, None, None)))


class TestEncodeHelper(unittest.TestCase):

    def test_encode_helper_1(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode_helper("B", root), "1010")

    def test_encode_helper_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode_helper("F", root), "111")

    def test_encode_helper_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode_helper("A", root), "100")

    def test_encode_helper_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode_helper("E", root), "0")

    def test_encode_helper_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode_helper("C", root), "1011")


class TestDecode(unittest.TestCase):

    def test_decode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BE")

    def test_decode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("111100", root), "FA")

    def test_decode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("1010100100", root), "BAA")

    def test_decode_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("101001010010100", root), "BEBEBE")

    def test_decode_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("1011010100", root), "CEBE")


if __name__ == "__main__":
    unittest.main()
