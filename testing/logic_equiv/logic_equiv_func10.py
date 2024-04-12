import hypothesis
from hypothesis import given, strategies as st

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_para_flat_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    flat = para_flat_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == flat

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_para_struc_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    struc =  para_struc_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == struc

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_bullet_flat_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    flat = bullet_flat_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == flat

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_bullet_struc_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    struc =  bullet_struc_func10(a,b,c)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_psuedo_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    psuedo = psuedo_func10(a,b,c)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo

def orig_func10(a, b, c):
    char_vals = [ord(c) for c in a]

    match c:
        case 0:
            char_vals = [val << 1 for val in char_vals]
            b = b + 'a'
        case 1:
            char_vals = [val >> 1 for val in char_vals]
            b = 'b' + b
        case 2:
            char_vals = [val + 5 for val in char_vals]
            b = b + 'c'
        case _:
            char_vals = [val + 1 for val in char_vals]
            b = 'd' + b

    if len(a) > len(b):
        length = len(b)
    else:
        length = len(a)

    for i in range(length):
        b_val = ord(b[i])
                    
        if char_vals[i] > b_val:
            char_vals[i] -= b_val
        else:
            char_vals[i] += b_val

    ret = ""
    for x in char_vals:
        ret = ret + chr(x)

    if c > 0:
        repeat = int(abs(len(b)*len(b) - c*c)/(len(a)+1))
        ret = ret * repeat
    
    return ret

def para_flat_func10(a, b, c):
    """
    Operates on three parameters a, b, and c.

    Args:
    - a (str): The first string.
    - b (str): The second string.
    - c (int): A parameter determining operations on the strings.

    Returns:
    - str: The resulting string after performing operations based on the input parameters.
    """
    # Convert each character in string a into its ASCII value and store them in char_vals list
    char_vals = [ord(char) for char in a]

    # Perform different operations on char_vals and modify b based on the value of c
    if c == 0:
        char_vals = [val + 1 for val in char_vals]
        b += "!"
    elif c < 0:
        char_vals = [val - 1 for val in char_vals]
        b += "?"
    else:
        char_vals = [val * c for val in char_vals]
        b += "."

    # Determine the length of the shorter string between a and b
    min_length = min(len(a), len(b))

    # Iterate through the characters of both strings and perform arithmetic operations between corresponding ASCII values
    ret = ""
    for i in range(min_length):
        ret += chr(char_vals[i] + ord(b[i]))

    # Convert modified ASCII values back to characters and concatenate them to form a string ret
    ret += a[min_length:]  # Add remaining characters from string a

    # If c is greater than 0, calculate a repetition factor and repeat ret accordingly
    if c > 0:
        repetition_factor = len(b) * ((c + 1) * len(a) // len(b))
        ret *= repetition_factor

    return ret

def para_struc_func10(a, b, c):
    # Convert characters of string a to ASCII values
    char_vals = [ord(char) for char in a]

    # Perform operations based on the value of c
    if c % 4 == 0:
        char_vals = [val << c for val in char_vals]
    elif c % 4 == 1:
        char_vals = [val >> c for val in char_vals]
    elif c % 4 == 2:
        char_vals = [val + c for val in char_vals]
    else:
        char_vals = [val - c for val in char_vals]

    # Modify string b based on char_vals
    b = ''.join([chr(val) for val in char_vals]) + b

    # Determine the length of the shorter string
    min_len = min(len(a), len(b))

    # Construct the new string ret by performing arithmetic operations
    ret = ''.join([chr(ord(a[i]) + ord(b[i])) for i in range(min_len)])

    # Repeat ret based on a calculated repetition factor if c > 0
    if c > 0:
        repetition_factor = (len(b) * (c + len(a) // len(b))) // len(a)
        ret *= repetition_factor

    return ret


def bullet_flat_func10(a, b, c):
    """
    Perform operations on strings based on given parameters.

    Args:
    - a: A string.
    - b: A string.
    - c: An integer.

    Returns:
    - The resulting string after performing operations.
    """
    # Convert each character in string a to its ASCII value and store them in a list
    char_vals = [ord(char) for char in a]

    # Perform different operations based on the value of c
    match c:
        case 0:
            # Left-shift each value in char_vals by 1 and append 'a' to string b
            b += 'a' + ''.join(chr(val << 1) for val in char_vals)
        case 1:
            # Right-shift each value in char_vals by 1 and prepend 'b' to string b
            b = 'b' + ''.join(chr(val >> 1) for val in char_vals)
        case 2:
            # Add 5 to each value in char_vals and append 'c' to string b
            b += 'c' + ''.join(chr(val + 5) for val in char_vals)
        case _:
            # Add 1 to each value in char_vals and prepend 'd' to string b for any other value of c
            b = 'd' + ''.join(chr(val + 1) for val in char_vals)

    # Determine the length of the shortest string between a and b
    min_length = min(len(a), len(b))

    # Iterate over the common length of a and b characters and adjust char_vals based on comparison
    for i in range(min_length):
        if a[i] < b[i]:
            char_vals[i] -= 1
        elif a[i] > b[i]:
            char_vals[i] += 1

    # Convert the values in char_vals back to characters and concatenate them to form a string ret
    ret = ''.join(chr(val) for val in char_vals)

    # If c is greater than 0, calculate repetition factor and repeat the string ret
    if c > 0:
        repetition_factor = (len(b) * len(b) - c * c) // (len(a) + 1)
        ret *= repetition_factor

    return ret

def bullet_struc_func10(a, b, c):
    char_vals = [ord(char) for char in a]

    match c:
        case 0:
            char_vals = [(val << 1) for val in char_vals]
            b += 'a'
        case 1:
            char_vals = [(val >> 1) for val in char_vals]
            b = 'b' + b
        case 2:
            char_vals = [val + 5 for val in char_vals]
            b += 'c'
        case _:
            char_vals = [val + 1 for val in char_vals]
            b = 'd' + b

    min_len = min(len(a), len(b))

    for i in range(min_len):
        if a[i] > b[i]:
            char_vals[i] += 1
        elif a[i] < b[i]:
            char_vals[i] -= 1

    ret = ''.join(chr(val) for val in char_vals)

    if c > 0:
        rep_factor = (len(b)*len(b) - c*c) // (len(a) + 1)
        ret *= rep_factor

    return ret

def psuedo_func10(a, b, c):
    char_vals = [ord(char) for char in a]

    b_val = ord(b[0])

    case = c
    if case == 0:
        char_vals = [(val << 1) for val in char_vals]
        b = 'a' + b
    elif case == 1:
        char_vals = [(val >> 1) for val in char_vals]
        b = 'b' + b
    elif case == 2:
        char_vals = [val + 5 for val in char_vals]
        b = b + 'c'
    else:
        char_vals = [val + 1 for val in char_vals]
        b = 'd' + b

    length = min(len(a), len(b))

    for i in range(length):
        b_val = ord(b[i])
        if char_vals[i] > b_val:
            char_vals[i] -= b_val
        else:
            char_vals[i] += b_val

    ret = ''
    for val in char_vals:
        ret += chr(val)

    if c > 0:
        repeat = abs((len(b) ** 2 - c ** 2) // (len(a) + 1))
        ret *= repeat

    return ret


def try_test(test, test_fail_string, test_pass_string):
    try:
        test()
        print(test_pass_string)
        print("")
    except Exception as e:
        print(test_fail_string)
        print(repr(e))
        print("")

print("----- func10 LOGIC EQUIV TESTING -------")
try_test(test_para_flat_func10, "PARA FLAT FAIL", "PARA FLAT PASS")
try_test(test_para_struc_func10, "PARA STRUC FAIL", "PARA STRUC PASS")
try_test(test_bullet_flat_func10, "BULLET FLAT FAIL", "BULLET FLAT PASS")
try_test(test_bullet_struc_func10, "BULLET STRUC FAIL", "BULLET STRUC PASS")
try_test(test_psuedo_func10, "PSUEDO FAIL", "PSUEDO PASS")