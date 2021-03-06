"""
Test file `lc263_ugly_number.py`
"""
# pylint: disable=no-self-use

import random

import pytest

from leetcode.math.lc263_ugly_number import is_ugly_number


class TestIsUglyNumber(object):
    """ The mighty test suite to the mighty solution. """

    PRIMES = [2, 3, 5]

    @pytest.mark.parametrize('test_input', [
        0,
        -1234
    ])
    def test_non_positive(self, test_input):
        assert not is_ugly_number(test_input)

    def test_one(self):
        assert is_ugly_number(1)

    @pytest.mark.parametrize("test_input", PRIMES)
    def test_primes(self, test_input):
        assert is_ugly_number(test_input)

    def test_multiple_of_primes(self):
        turns = random.randint(0, 20)
        number = 1
        for _ in range(turns):
            number *= random.choice(self.PRIMES)
            assert is_ugly_number(number)

    def test_ugly_factor(self):
        the_uglies = [7, 11, 13, 17, 29]
        turns = random.randint(0, 20)
        number = random.choice(the_uglies)
        for _ in range(turns):
            number *= random.choice(self.PRIMES)
            assert not is_ugly_number(number)
