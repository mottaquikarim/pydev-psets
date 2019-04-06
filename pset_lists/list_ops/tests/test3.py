# import io
# import pytest

# from unittest import TestCase
# from unittest.mock import patch


# SOLUTION - COOL RUNNINGS!

cool_runnings = [
	'Feel', 'the', 'rhythm.',
	'Feel', 'the', 'rhyme.',
	'Get', 'on', 'up.',
	'It\'s', 'bobsled', 'time!'
]

bobsled = cool_runnings.index('bobsled')
cool_runnings[bobsled] = 'YOLO'

l1 = cool_runnings[:3]
l1 = ' '.join(l1)

l2 = cool_runnings[3:6]
l2 = ' '.join(l2)

l3 = cool_runnings[6:9]
l3 = ' '.join(l3)

l4 = cool_runnings[9:12]
l4 = ' '.join(l4)

print(f'''
{l1}
{l2}
{l3}
{l4}
''')

@pytest.mark.describe('Cool Runnings! - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Cool Runnings! - XXX')
class TestPrint(TestCase):



@pytest.mark.describe('Cool Runnings! - XXX')
class TestPrint(TestCase):
