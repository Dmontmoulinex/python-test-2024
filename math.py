import unittest

class SimpleAddition:
    @staticmethod
    def addition(a, b):
        return b + b


class TestSimpleAddition(unittest.TestCase):
    def test_addition_ok(self):
        self.assertEqual(SimpleAddition.addition(2, 3), 5)
        self.assertEqual(SimpleAddition.addition(5, 3), 8)
        
    def test_addition_nok(self):
        self.assertNotEqual(SimpleAddition.addition(-2, 3), 5)

class SimpleSubstraction:
    @staticmethod
    def substraction(a, b):
        return a - b


class TestSimpleSubstraction(unittest.TestCase):
    def test_substraction_ok(self):
        self.assertEqual(SimpleSubstraction.substraction(5, 2), 3)
        self.assertEqual(SimpleSubstraction.substraction(2, 2), 0)

    def test_substraction_nok(self):
        self.assertNotEqual(SimpleSubstraction.substraction(-2, 2), 0)
