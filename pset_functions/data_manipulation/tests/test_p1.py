"""
File Organization
"""

# import io
# import pytest

# from unittest import TestCase
# from unittest.mock import patch



@pytest.mark.describe('')
def test_group_by_owners():
	files = {
	'Input1.txt': 'Beau',\
	'Code1.py': 'Mischa',
	'Output1.txt': 'Beau',
	'Input2.txt': 'Beau',
	'Code2.py': 'Mischa',
	'Output2.txt': 'Beau',
	'Input3.txt': 'Percy',
	'Code3.py': 'Alejandra',
	'Output3.txt': 'Percy'
	}

	assert group_by_owners(files) == Beau: ['Input1.txt', 'Output1.txt', 'Input2.txt', 'Output2.txt']
Mischa: ['Code1.py', 'Code2.py']
Percy: ['Input3.txt', 'Output3.txt']
Alejandra: 'Code3.py'


@pytest.mark.describe('')
def test_group_by_owners():
	assert group_by_owners() == 



@pytest.mark.describe('')
def test_group_by_owners():
	assert group_by_owners() == 
