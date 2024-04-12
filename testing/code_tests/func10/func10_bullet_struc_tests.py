import coverage # pragma: no cover

def func10(a, b, c):
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

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: c = 0, common characters in a and b, a is shorter than b
        a1 = "abc"
        b1 = "defghi"
        c1 = 0
        assert func10(a1, b1, c1) == 'abcdefghi'
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: c = 1, common characters in a and b, b is shorter than a
        a2 = "def"
        b2 = "abc"
        c2 = 1
        assert func10(a2, b2, c2) == 'bcadef'
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: c = 2, common characters in a and b, a and b are equal length
        a3 = "ghi"
        b3 = "jkl"
        c3 = 2
        assert func10(a3, b3, c3) == 'gijlm'
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: c = 3, common characters in a and b, a and b are equal length
        a4 = "abc"
        b4 = "def"
        c4 = 3
        assert func10(a4, b4, c4) == 'dgj'
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: c = 4, common characters in a and b, a is shorter than b
        a5 = "abcd"
        b5 = "efghijkl"
        c5 = 4
        assert func10(a5, b5, c5) == 'efghijklmnopq'
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: c = 5, common characters in a and b, b is shorter than a
        a6 = "lmnop"
        b6 = "ijkl"
        c6 = 5
        assert func10(a6, b6, c6) == 'ijklopqr'
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: c = 0, no common characters in a and b
        a7 = "abc"
        b7 = "def"
        c7 = 0
        assert func10(a7, b7, c7) == 'abc'
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: c = 1, no common characters in a and b
        a8 = "abc"
        b8 = "def"
        c8 = 1
        assert func10(a8, b8, c8) == 'defabc'
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: c = 2, no common characters in a and b
        a9 = "abc"
        b9 = "def"
        c9 = 2
        assert func10(a9, b9, c9) == 'fgh'
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: c = 3, no common characters in a and b
        a10 = "abc"
        b10 = "def"
        c10 = 3
        assert func10(a10, b10, c10) == 'ghi'
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

failed_ratio = bullet_struc_test_cases()/10 # pragma: no cover

# Stop measuring coverage
cov.stop() # pragma: no cover

# Generate coverage report
cov.save() # pragma: no cover

cov.combine() # pragma: no cover

cov.save() # pragma: no cover

# Load coverage report
cov.load() # pragma: no cover

# Get coverage results
coverage_percentage = cov.report() * 0.01 # pragma: no cover