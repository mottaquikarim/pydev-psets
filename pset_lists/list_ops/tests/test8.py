# import io
# import pytest

# from unittest import TestCase
# from unittest.mock import patch


# SOLUTION - TUPLE SORTING

tuples1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sorted(tuples1))
[(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]


tuples2 = sorted(tuples1, key=lambda s : s[1])
print(tuples2)
[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


@pytest.mark.describe('Tuple Sorting - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Tuple Sorting - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Tuple Sorting - XXX')
class TestPrint(TestCase):
