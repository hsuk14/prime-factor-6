from unittest import TestCase

from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):
    def test_extract(self):
        expected_result = [2,2]
        sut = PrimeFactors()

        self.assertEqual(expected_result, sut.extract(4))
