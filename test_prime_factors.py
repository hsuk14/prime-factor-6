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

