import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

def test_para_flat_func6():
    arr = np.random.randint(10, size=7)
    orig = orig_func6(arr)
    flat = para_flat_func6(arr)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

def test_para_struc_func6():
    arr = np.random.randint(10, size=7)
    orig = orig_func6(arr)
    struc = para_struc_func6(arr)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

def test_bullet_flat_func6():
    arr = np.random.randint(10, size=7)
    orig = orig_func6(arr)
    flat = bullet_struc_func6(arr)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

def test_bullet_struc_func6():
    arr = np.random.randint(10, size=7)
    orig = orig_func6(arr)
    struc = bullet_struc_func6(arr)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

def test_psuedo_func6():
    arr = np.random.randint(10, size=7)
    orig = orig_func6(arr)
    psuedo = psuedo_func6(arr)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert orig == psuedo

def orig_func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0]*2]
    
    new_n = []
    i = math.floor(len(n)/2)

    new_n = new_n + orig_func6(n[0:i])
    new_n = new_n + orig_func6(n[i:])

    return new_n

def para_flat_func6(n):
    """
    Doubles each element of the input list recursively until reaching the base cases.

    Args:
    - n (list): The input list.

    Returns:
    - list: The modified version of the input list.
    """
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0] * 2]
    else:
        mid = len(n) // 2
        left_half = para_flat_func6(n[:mid])
        right_half = para_flat_func6(n[mid:])
        return left_half + right_half

    
def para_struc_func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0] * 2]
    else:
        mid = len(n) // 2
        left_half = para_struc_func6(n[:mid])
        right_half = para_struc_func6(n[mid:])
        return left_half + right_half
    
def bullet_flat_func6(n):
    # If the length of the input list is 0, return an empty list
    if len(n) == 0:
        return []
    # If the length of the input list is 1, return a new list containing the first element doubled
    elif len(n) == 1:
        return [n[0] * 2]
    else:
        # Split the input list into two halves
        midpoint = len(n) // 2
        left_half = n[:midpoint]
        right_half = n[midpoint:]
        
        # Recursively call func6 on each half of the list
        left_result = bullet_flat_func6(left_half)
        right_result = bullet_flat_func6(right_half)
        
        # Concatenate the results of the recursive calls into a new list
        new_n = left_result + right_result
        
        # Return the concatenated list
        return new_n

def bullet_struc_func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0] * 2]
    else:
        mid = len(n) // 2
        left_half = bullet_struc_func6(n[:mid])
        right_half = bullet_struc_func6(n[mid:])
        new_n = left_half + right_half
        return new_n

    
def psuedo_func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0] * 2]
    
    new_n = []
    i = len(n) // 2

    first_half = psuedo_func6(n[:i])
    second_half = psuedo_func6(n[i:])
    
    new_n.extend(first_half)
    new_n.extend(second_half)

    return new_n

def try_test(test, test_fail_string, test_pass_string):
    try:
        test()
        print(test_pass_string)
        print("")
    except Exception as e:
        print(test_fail_string)
        print(repr(e))
        print("")

print("----- func6 LOGIC EQUIV TESTING -------")
try_test(test_para_flat_func6, "PARA FLAT FAIL", "PARA FLAT PASS")
try_test(test_para_struc_func6, "PARA STRUC FAIL", "PARA STRUC PASS")
try_test(test_bullet_flat_func6, "BULLET FLAT FAIL", "BULLET FLAT PASS")
try_test(test_bullet_struc_func6, "BULLET STRUC FAIL", "BULLET STRUC PASS")
try_test(test_psuedo_func6, "PSUEDO FAIL", "PSUEDO PASS")