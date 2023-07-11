# Name:         Brenden Sprague
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021

import unittest
import postfixit


class TestPostFixEval(unittest.TestCase):
    def test_postfix_eval_1(self):
        xs = ["1 ", "2", "+", "3", "*"]
        self.assertEqual(postfixit.postfix_eval(xs), "9.000")

    def test_postfix_eval_2(self):
        xs = ["1", "4", "+", "3", "*", "2", "3", "+"]
        self.assertEqual(postfixit.postfix_eval(xs), "5.000")

    def test_postfix_eval_3(self):
        xs = ["1.0", "2.0", "^"]
        self.assertEqual(postfixit.postfix_eval(xs), "1.000")

    def test_postfix_eval_4(self):
        xs = ["1", "2", "+", "3", "/", "2", "+"]
        self.assertEqual(postfixit.postfix_eval(xs), "3.000")

    def test_postfix_eval_5(self):
        xs = ["1", "4", "4", "*", "-"]
        self.assertEqual(postfixit.postfix_eval(xs), "-15.000")


class PemdasTest(unittest.TestCase):
    def test_pemdas_1(self):
        self.assertEqual(postfixit.pemdas("*"), 2)

    def test_pemdas_2(self):
        self.assertEqual(postfixit.pemdas("^"), 3)

    def test_pemdas_3(self):
        self.assertEqual(postfixit.pemdas("+"), 1)

    def test_pemdas_4(self):
        self.assertEqual(postfixit.pemdas("-"), 1)

    def test_pemdas_5(self):
        self.assertEqual(postfixit.pemdas(")"), 4)


class OperatorFinderTest(unittest.TestCase):
    def test_operator_finder_1(self):
        self.assertEqual(postfixit.operator_finder(3, 3, "*"), 9)

    def test_operator_finder_2(self):
        self.assertEqual(postfixit.operator_finder(3, 3, "-"), 0)

    def test_operator_finder_3(self):
        self.assertEqual(postfixit.operator_finder(12, 3, "/"), .25)

    def test_operator_finder_4(self):
        self.assertEqual(postfixit.operator_finder(10, 20, "+"), 30)

    def test_operator_finder_5(self):
        self.assertEqual(postfixit.operator_finder(20, 4, "-"), -16)


class TestInfixEval(unittest.TestCase):
    def test_infix_eval_1(self):
        stack = ["(", "1", "+", "2", ")", "*", "3"]
        out = ["1", "2", "+", "3", "*"]
        self.assertEqual(postfixit.infix_eval(stack), out)

    def test_infix_eval_2(self):
        stack = ["8", "/", "4", "^", "3"]
        out = ["8", "4", "3", "^", "/"]
        self.assertEqual(postfixit.infix_eval(stack), out)

    def test_infix_eval_3(self):
        stack = ["20", "*", "4", "+", "4", "-", "3"]
        out = ["20", "4", "*", "4", "+", "3", "-"]
        self.assertEqual(postfixit.infix_eval(stack), out)

    def test_infix_eval_4(self):
        stack = ["(", "30", "-", "10", ")"]
        out = ["30", "10", "-"]
        self.assertEqual(postfixit.infix_eval(stack), out)

    def test_infix_eval_5(self):
        stack = ["3", "3", "*", "3", "*", "3", "*"]
        out = ["3", "3", "3", "*", "3", "*", "*"]
        self.assertEqual(postfixit.infix_eval(stack), out)


class TestNumberChecker(unittest.TestCase):
    def test_number_check_1(self):
        self.assertEqual(postfixit.number_check("2"), True)

    def test_number_check_2(self):
        self.assertEqual(postfixit.number_check("a"), False)

    def test_number_check_3(self):
        self.assertEqual(postfixit.number_check("1"), True)

    def test_number_check_4(self):
        self.assertEqual(postfixit.number_check("b"), False)

    def test_number_check_5(self):
        self.assertEqual(postfixit.number_check("c"), False)


if __name__ == "__main__":
    unittest.main()
