# This is just a test, disregard
import unittest
import re

def eq_numbers(string):

    eq = {}

    var_list = re.findall(r'[a-zA-Z]', string)

    for var in var_list:
        eq[var] = find_coef(var, string)

    eq['result'] = find_result(string)

    return eq

def find_result(string):
    return int(string.split('=')[-1].strip())

def find_coef(var, string):
    var = var.strip()
    string = string.replace(' ', '')

    # https://regex101.com/r/WqK4bP/3
    pattern = r'([\d|\-|\+]*?%s)' % (re.escape(var))
    result = re.search(pattern, string)

    # No match = no coefficient
    if not result:
        return 0

    result = result.group(0)
    result = result.replace('+', '')

    if result == var: # ie. 'x'
        coef = 1
    elif result == '-' + var: # ie. '-x'
        coef = -1
    else:
        coef = int(result[:-1])
    return coef



def test_find_coef():
    assert find_coef('x', '-2x + 7y + 3z = 4') == -2
    assert find_coef('x', '-x + 7y + 3z = 4') == -1
    assert find_coef('x', '7x + 7y + 3z = 4') == 7

    assert find_coef('y', '3x + 7y + 3z = 4') == 7
    assert find_coef('y', '7x + -y + 3z = 4') == -1
    assert find_coef('y', '7x + y + 3z = 4') == 1

    assert find_coef('z', '7x + 3y + 3z = 4') == 3
    assert find_coef('z', '7x + y + -3z = 4') == -3
    assert find_coef('z', '7x + y + z = 4') == 1
    assert find_coef('z', '7x + y + -z = 4') == -1


def test_find_result():
    assert find_result('3 + 3 = 6') == 6
    assert find_result('3 + -4 = -1') == -1

def test_eq_numbers():
    assert eq_numbers('2x + 7y + 3z = 4') == {
        'x': 2,
        'y': 7,
        'z': 3,
        'result': 4
    }

    assert eq_numbers('x + 6y + 4z = 2') == {
        'x': 1,
        'y': 6,
        'z': 4,
        'result': 2
    }

    assert eq_numbers('6y - 4z = 2') == {
        'y': 6,
        'z': -4,
        'result': 2
    }

    assert eq_numbers('4z = -2') == {
        'z': 4,
        'result': -2
    }

    assert eq_numbers('3x + 4z = -2') == {
        'x': 3,
        'z': 4,
        'result': -2
    }


if __name__ == '__main__':
    test_find_coef()
