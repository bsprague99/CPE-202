# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Winter 2021

import unittest

import pset3
from pset3 import ListNode  # only allowed use of from ... import


class TestMul(unittest.TestCase):

    def test_mul_1(self):
        self.assertEqual(pset3.mul(-2, -3), 6)

    def test_mul_2(self):
        self.assertEqual(pset3.mul(2, 2), 4)

    def test_mul_3(self):
        self.assertEqual(pset3.mul(1, 4), 4)

    def test_mul_4(self):
        self.assertEqual(pset3.mul(6, 10), 60)

    def test_mul_5(self):
        self.assertEqual(pset3.mul(-2, 10), -20)


class TestExp(unittest.TestCase):

    def test_exp_1(self):
        self.assertEqual(pset3.exp(-2, 3), -8)

    def test_exp_2(self):
        self.assertEqual(pset3.exp(3, 3), 27)

    def test_exp_3(self):
        self.assertEqual(pset3.exp(2, 4), 16)

    def test_exp_4(self):
        self.assertEqual(pset3.exp(-2, 6), 64)

    def test_exp_5(self):
        self.assertEqual(pset3.exp(-2, 1), -2)


class TestFac(unittest.TestCase):

    def test_fac_1(self):
        self.assertEqual(pset3.fac(5), 120)

    def test_fac_2(self):
        self.assertEqual(pset3.fac(4), 24)

    def test_fac_3(self):
        self.assertEqual(pset3.fac(3), 6)

    def test_fac_4(self):
        self.assertEqual(pset3.fac(6), 720)

    def test_fac_5(self):
        self.assertEqual(pset3.fac(7), 5040)


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        self.assertEqual(pset3.fibonacci(8, 0, 1), 13)

    def test_fibonacci_2(self):
        self.assertEqual(pset3.fibonacci(8, 0, 2), 26)

    def test_fibonacci_3(self):
        self.assertEqual(pset3.fibonacci(7, 0, 1), 8)

    def test_fibonacci_4(self):
        self.assertEqual(pset3.fibonacci(1, 0, 1), 0)

    def test_fibonacci_5(self):
        self.assertEqual(pset3.fibonacci(2, 0, 1), 1)

    def test_fibonacci_6(self):
        self.assertEqual(pset3.fibonacci(3, 0, 1), 1)


class TestMakeSubstring(unittest.TestCase):

    def test_make_substring_1(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 3), "CPE")

    def test_make_substring_2(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 2), "CMUE")

    def test_make_substring_3(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 1), "COMPUTER")

    def test_make_substring_4(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 4), "CU")

    def test_make_substring_5(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 5), "CT")


class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_1(self):
        self.assertEqual(pset3.is_palindrome("tacocat"), True)

    def test_is_palindrome_2(self):
        self.assertEqual(pset3.is_palindrome("palindrome"), False)

    def test_is_palindrome_3(self):
        self.assertEqual(pset3.is_palindrome("llllooollll"), True)

    def test_is_palindrome_4(self):
        self.assertEqual(pset3.is_palindrome("teset"), True)

    def test_is_palindrome_5(self):
        self.assertEqual(pset3.is_palindrome("test"), False)


class TestSwapChars(unittest.TestCase):

    def test_swap_chars_1(self):
        self.assertEqual(pset3.swap_chars("AaBbCcD"), "aAbBcCD")

    def test_swap_chars_2(self):
        self.assertEqual(pset3.swap_chars("asdfgh"), "safdhg")

    def test_swap_chars_3(self):
        self.assertEqual(pset3.swap_chars("zxcvb"), "xzvcb")

    def test_swap_chars_4(self):
        self.assertEqual(pset3.swap_chars("edcrfv"), "dercvf")

    def test_swap_chars_5(self):
        self.assertEqual(pset3.swap_chars("weBbCcD"), "ewbBcCD")




class TestLength(unittest.TestCase):

    def test_length_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        self.assertEqual(pset3.length(head), 4)

    def test_length_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.length(head), 3)

    def test_length_3(self):
        head = ListNode(1, ListNode(2, None))
        self.assertEqual(pset3.length(head), 2)

    def test_length_4(self):
        head = ListNode(1, None)
        self.assertEqual(pset3.length(head), 1)

    def test_length_5(self):
        head = ListNode(1, ListNode(2, \
                                    ListNode(3, \
                                             ListNode(4, \
                                                      ListNode(5, None)))))
        self.assertEqual(pset3.length(head), 5)


class TestFindMax(unittest.TestCase):

    def test_find_max_1(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(1, None))))
        self.assertEqual(pset3.find_max(head), 2)

    def test_find_max_2(self):
        head = ListNode(2, ListNode(3, ListNode(4, \
                                                ListNode(1, \
                                                         ListNode(5, None)))))
        self.assertEqual(pset3.find_max(head), 5)

    def test_find_max_3(self):
        head = ListNode(2, ListNode(3, None))
        self.assertEqual(pset3.find_max(head), 3)

    def test_find_max_4(self):
        head = ListNode(2, ListNode(3, ListNode(4, None)))
        self.assertEqual(pset3.find_max(head), 4)

    def test_find_max_5(self):
        head = ListNode(2, ListNode(3, ListNode(6, ListNode(1, None))))
        self.assertEqual(pset3.find_max(head), 6)




class TestReverse(unittest.TestCase):

    def test_reverse_1(self):
        head = ListNode(2, ListNode(3, None))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(3, ListNode(2, None)))

    def test_reverse_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(3, ListNode(2, ListNode(1, None))))

    def test_reverse_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(4, \
                                  ListNode(3, \
                                           ListNode(2, \
                                                    ListNode(1, None)))))

    def test_reverse_4(self):
        head = ListNode(1, ListNode(2,
                                    ListNode(3,
                                             ListNode(4,
                                                      ListNode(5,
                                                               None)))))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(5,
                                  ListNode(4,
                                           ListNode(3,
                                                    ListNode(2,
                                                             ListNode(1,
                                                                      None))))))
    def test_reverse_5(self):
        head = ListNode(1, None)
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(1, None))


class TestNestingDollConstructor(unittest.TestCase):

    def test_nesting_doll_constructor_1(self):
        doll = pset3.NestingDoll(3)
        self.assertEqual(doll.inner.inner.inner, None)

    def test_nesting_doll_constructor_2(self):
        doll = pset3.NestingDoll(1)
        self.assertEqual(doll.inner, None)

    def test_nesting_doll_constructor_3(self):
        doll = pset3.NestingDoll(2)
        self.assertEqual(doll.inner.inner, None)

    def test_nesting_doll_constructor_4(self):
        doll = pset3.NestingDoll(5)
        self.assertEqual(doll.inner.inner.inner.inner.inner, None)

    def test_nesting_doll_constructor_5(self):
        doll = pset3.NestingDoll(4)
        self.assertEqual(doll.inner.inner.inner.inner, None)


class TestNestingDollEquals(unittest.TestCase):

    def test_nesting_doll_equals_1(self):
        self.assertEqual(pset3.NestingDoll(1), pset3.NestingDoll(1))

    def test_nesting_doll_equals_2(self):
        self.assertNotEqual(pset3.NestingDoll(1), pset3.NestingDoll(2))

    def test_nesting_doll_equals_3(self):
        self.assertEqual(pset3.NestingDoll(8), pset3.NestingDoll(8))

    def test_nesting_doll_equals_4(self):
        self.assertNotEqual(pset3.NestingDoll(1), pset3.NestingDoll(3))

    def test_nesting_doll_equals_5(self):
        self.assertEqual(pset3.NestingDoll(4), pset3.NestingDoll(4))


class TestNestingDollString(unittest.TestCase):

    def test_nesting_doll_string_1(self):
        self.assertEqual(str(pset3.NestingDoll(3)), "((8))")

    def test_nesting_doll_string_2(self):
        self.assertEqual(str(pset3.NestingDoll(4)), "(((8)))")

    def test_nesting_doll_string_3(self):
        self.assertEqual(str(pset3.NestingDoll(5)), "((((8))))")

    def test_nesting_doll_string_4(self):
        self.assertEqual(str(pset3.NestingDoll(6)), "(((((8)))))")

    def test_nesting_doll_string_5(self):
        self.assertEqual(str(pset3.NestingDoll(7)), "((((((8))))))")


if __name__ == "__main__":
    unittest.main()
