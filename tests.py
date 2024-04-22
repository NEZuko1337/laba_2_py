import unittest
from polynomial import Polynomial


class TestCase(unittest.TestCase):
    poly1 = Polynomial(1, 2, 3)  # многочлен 3x^2 + 2x + 1
    poly2 = Polynomial(4, 5, 6)  # многочлен 6x^2 + 5x + 4
    poly3 = Polynomial(-1, -2, -3)  # многочлен -3x^2 - 2x - 1
    poly4 = Polynomial(-1, 0, 1)  # x^2 - 1
    poly5 = Polynomial(0, 0, 0)  # 0

    def test_addition(self):
        self.assertEqual(self.poly1 + self.poly2, Polynomial(5, 7, 9), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 + self.poly3, Polynomial(0, 0, 0), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 + self.poly4, Polynomial(0, 2, 4), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 + self.poly5, self.poly1, msg="Тест завалился, фикси")

    def test_subtraction(self):
        self.assertEqual(self.poly1 - self.poly2, Polynomial(-3, -3, -3), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 - self.poly3, Polynomial(2, 4, 6), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 - self.poly5, self.poly1, msg="Тест завалился, фикси")

    def test_unary_minus(self):
        self.assertEqual(-self.poly1, Polynomial(-1, -2, -3), msg="Тест завалился, фикси")
        self.assertEqual(-self.poly3, Polynomial(1, 2, 3), msg="Тест завалился, фикси")
        self.assertEqual(-self.poly5, Polynomial(0, 0, 0), msg="Тест завалился, фикси")

    def test_comparison(self):
        self.assertTrue(self.poly1 == Polynomial(1, 2, 3), msg="Тест завалился, фикси")
        self.assertTrue(self.poly1 != Polynomial(3, 2, 1), msg="Тест завалился, фикси")
        self.assertTrue(self.poly5 == Polynomial(0, 0, 0), msg="Тест завалился, фикси")

    def test_arithmetic_operations_with_numbers(self):
        self.assertEqual(self.poly1 + 1, Polynomial(2, 2, 3), msg="Тест завалился, фикси")
        self.assertEqual(self.poly2 - 2, Polynomial(2, 5, 6), msg="Тест завалился, фикси")
        self.assertEqual(self.poly1 * 2, Polynomial(2, 4, 6), msg="Тест завалился, фикси")
        self.assertEqual(self.poly4 + 1, Polynomial(0, 0, 1), msg="Тест завалился, фикси")

    def test_poly_degree(self):
        self.assertEqual(self.poly1.degree(), 2, msg="Тест завалился, чини")
        self.assertEqual(self.poly2.degree(), 2, msg="Тест завалился, чини")
        self.assertEqual(self.poly4.degree(), 2, msg="Тест завалился, чини")
        self.assertEqual(self.poly5.degree(), 0, msg="Тест завалился, чини")

    def test_v_tochke(self):
        self.assertEqual(self.poly1(1), 6, msg="Тест сломался, чини")
        self.assertEqual(self.poly1(2), 17, msg="Тест сломался, чини")
        self.assertEqual(self.poly2(2), 38, msg="Тест сломался, чини")
        self.assertEqual(self.poly5(2), 0, msg="Тест сломался, чини")

    def test_derivide(self):
        self.assertEqual(self.poly1.der(), Polynomial(2, 6), msg="Тест сломался, чини")
        self.assertEqual(self.poly1.der(2), 6, msg="Тест сломался, чини")
        self.assertEqual(self.poly4.der(), Polynomial(0, 2), msg="Тест сломался, чини")
        self.assertEqual(self.poly4.der(2), 2, msg="Тест сломался, чини")
        self.assertEqual(self.poly4.der(3), Polynomial([]), msg="Тест сломался, чини")

    def test_iter_next(self):
        needed = []
        for el in self.poly1:
            needed.append(el)
        self.assertEqual(needed, [(0, 1), (1, 2), (2, 3)], msg="Тест сломался")

        needed.clear()
        for el in self.poly2:
            needed.append(el)
        self.assertEqual(needed, [(0, 4), (1, 5), (2, 6)], msg="Тест сломался")

        needed.clear()
        for el in self.poly5:
            needed.append(el)
        self.assertEqual(needed, [(0, 0), (1, 0), (2, 0)], msg="Тест сломался")
        needed.clear()
