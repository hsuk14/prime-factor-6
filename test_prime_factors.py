from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_of_1(self):
        expected_result = 1
        sut = PrimeFactors()

        self.assertEqual(expected_result, sut.of(1))
