import hypothesis
from hypothesis import given, strategies as st

#PASS
@given(st.text())
def test_para_func1(string):
    print(string, orig_func1(string), para_flat_func1(string), para_struc_func1(string))
    assert orig_func1(string) == para_flat_func1(string) == para_struc_func1(string)
    print("PASS")

#PASS
@given(st.text())
def test_bullet_func1(string):
    print(string, orig_func1(string), bullet_flat_func1(string), bullet_struc_func1(string))
    assert orig_func1(string) == bullet_flat_func1(string) == bullet_struc_func1(string)
    print("PASS")

#PASS
@given(st.text())
def test_psuedo_func1(string):
    print(string, orig_func1(string), psuedo_func1(string))
    assert orig_func1(string) == psuedo_func1(string)
    print("PASS")

def orig_func1(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

def para_flat_func1(string):
    """
    Checks if a given string is a palindrome.

    Args:
    - string (str): The input string.

    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    """
    # Initialize left and right pointers
    left = 0
    right = len(string) - 1

    # Iterate over the string, comparing characters at symmetric positions
    while left < right:
        # If any pair of characters doesn't match, return False
        if string[left] != string[right]:
            return False
        # Move the pointers towards each other
        left += 1
        right -= 1

    # If all characters match, return True
    return True

def para_struc_func1(string):
    """
    Checks whether the input string is a palindrome.

    Args:
    - string (str): The string to be checked for palindrome property.

    Returns:
    - bool: True if the input string is a palindrome, False otherwise.
    """
    # Initialize left and right pointers
    left = 0
    right = len(string) - 1

    # Iterate over the string, comparing characters at symmetric positions
    while left < right:
        # If any pair of characters doesn't match, return False
        if string[left] != string[right]:
            return False
        # Move the pointers towards each other
        left += 1
        right -= 1

    # If all characters match, return True
    return True

def bullet_flat_func1(string):
    """
    Check if the input string is a palindrome.

    Args:
    - string: A string to be checked.

    Returns:
    - True if the string is a palindrome, False otherwise.
    """
    # Initialize variables
    left = 0
    right = len(string) - 1

    # Iterate while the condition holds true
    while right >= left:
        # Check if characters at left and right indices are equal
        if string[left] != string[right]:
            return False
        # Move towards the center of the string
        left += 1
        right -= 1

    # If loop completes without finding any non-matching characters, return True
    return True

def bullet_struc_func1(string):
    """
    Check if the input string is a palindrome.

    Args:
    - string: A string to be checked.

    Returns:
    - True if the string is a palindrome, False otherwise.
    """
    # Initialize variables
    left = 0
    right = len(string) - 1

    # Iterate while the condition holds true
    while right >= left:
        # Check if characters at left and right indices are equal
        if string[left] != string[right]:
            return False
        # Move towards the center of the string
        left += 1
        right -= 1

    # If loop completes without finding any non-matching characters, return True
    return True

def psuedo_func1(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

#EXECUTE TEST
test_bullet_func1()