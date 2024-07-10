from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):

    def setUp(self):
        super().setUp()
        self.sut = PrimeFactors()

    def test_of_1(self):
        expected_result = []
        self.assertEqual(expected_result, self.sut.of(1))

    def test_of_2(self):
        expected_result = [2]
        self.assertEqual(expected_result, self.sut.of(2))

    def test_of_3(self):
        expected_result = [3]
        self.assertEqual(expected_result, self.sut.of(3))

    def test_of_4(self):
        expected_result = [2, 2]
        self.assertEqual(expected_result, self.sut.of(4))

    def test_of_6(self):
        expected_result = [2, 3]
        self.assertEqual(expected_result, self.sut.of(6))

    def test_of_9(self):
        expected_result = [3, 3]
        self.assertEqual(expected_result, self.sut.of(9))

    def test_of_15(self):
        expected_result = [3, 5]
        self.assertEqual(expected_result, self.sut.of(15))

    def test_of_2730(self):
        expected_result = [2, 3, 5, 7, 13]
        self.assertEqual(expected_result, self.sut.of(2730))