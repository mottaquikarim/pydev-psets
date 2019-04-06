# import io
# import pytest

# from unittest import TestCase
# from unittest.mock import patch


# SOLUTION - MERGING LISTS WITH DUPLICATES

list1, list2 = [2, 8, 6], [10, 4, 12]

list3 = list1*2 # [2, 8, 6, 2, 8, 6]

####

list4 = list1 + list2 # [2, 8, 6, 10, 4, 12]

####

list3[:2] = [2, 12, 6] # [2, 12, 6, 6, 2, 8, 6]

####

set1 = set().union(list3, list4)

list5 = (list(set1)) # {2, 4, 6, 8, 10, 12}

print(list5) # [2, 4, 6, 8, 10, 12]


@pytest.mark.describe('Merging Lists with Duplicates - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Merging Lists with Duplicates - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Merging Lists with Duplicates - XXX')
class TestPrint(TestCase):
