import coverage # pragma: no cover

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

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
    try:
        count = 1 # Test 1: c = 0, common characters in a and b, a is shorter than b
        a = "abc"
        b = "defghi"
        c = 0
        assert func10(a, b, c) == 'abcdefghi'

        count += 1 # Test 2: c = 1, common characters in a and b, b is shorter than a
        a = "def"
        b = "abc"
        c = 1
        assert func10(a, b, c) == 'bcadef'

        count += 1 # Test 3: c = 2, common characters in a and b, a and b are equal length
        a = "ghi"
        b = "jkl"
        c = 2
        assert func10(a, b, c) == 'gijlm'

        count += 1 # Test 4: c = 3, common characters in a and b, a and b are equal length
        a = "abc"
        b = "def"
        c = 3
        assert func10(a, b, c) == 'dgj'

        count += 1 # Test 5: c = 4, common characters in a and b, a is shorter than b
        a = "abcd"
        b = "efghijkl"
        c = 4
        assert func10(a, b, c) == 'efghijklmnopq'

        count += 1 # Test 6: c = 5, common characters in a and b, b is shorter than a
        a = "lmnop"
        b = "ijkl"
        c = 5
        assert func10(a, b, c) == 'ijklopqr'

        count += 1 # Test 7: c = 0, no common characters in a and b
        a = "abc"
        b = "def"
        c = 0
        assert func10(a, b, c) == 'abc'

        count += 1 # Test 8: c = 1, no common characters in a and b
        a = "abc"
        b = "def"
        c = 1
        assert func10(a, b, c) == 'defabc'

        count += 1 # Test 9: c = 2, no common characters in a and b
        a = "abc"
        b = "def"
        c = 2
        assert func10(a, b, c) == 'fgh'

        count += 1 # Test 10: c = 3, no common characters in a and b
        a = "abc"
        b = "def"
        c = 3
        assert func10(a, b, c) == 'ghi'

        print("All tests passed!")
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("BULLET STRUC TEST CASE FAILED\n")

bullet_struc_test_cases() # pragma: no cover

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

print("Bullet Struc Coverage Percentage:", coverage_percentage) # pragma: no cover