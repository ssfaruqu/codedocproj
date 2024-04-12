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

#BULLET FLAT TESTS
def bullet_flat_test_cases(): # pragma: no cover
    try:
        count = 1
        # Test case 1: c = 0, left-shifts characters in a, appends 'a' to b
        assert func10("abc", "", 0) == "aaa"
        count += 1
        # Test case 2: c = 1, right-shifts characters in a, prepends 'b' to b
        assert func10("abc", "", 1) == "bbb"
        count += 1
        # Test case 3: c = 2, adds 5 to characters in a, appends 'c' to b
        assert func10("abc", "", 2) == "ccc"
        count += 1
        # Test case 4: c > 2, adds 1 to characters in a, prepends 'd' to b
        assert func10("abc", "", 3) == "ddd"
        count += 1
        # Test case 5: a and b have equal length, characters in a are greater, c = 0
        assert func10("xyz", "uvw", 0) == "vvv"
        # Test case 6: a and b have equal length, characters in b are greater, c = 1
        assert func10("abc", "def", 1) == "aaa"
        count += 1
        # Test case 7: a is shorter than b, c = 2
        assert func10("hi", "abcdefgh", 2) == "hhh"
        count += 1
        # Test case 8: b is shorter than a, c > 2
        assert func10("abcdefgh", "hi", 3) == "hiiiiiii"
        count += 1
        # Test case 9: a and b have equal length, characters in a are smaller, c = 0
        assert func10("abc", "def", 0) == "ddd"
        count += 1
        # Test case 10: a and b have equal length, characters in b are smaller, c = 1
        assert func10("def", "abc", 1) == "aaa"
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("BULLET FLAT TEST CASE FAILED\n")

bullet_flat_test_cases() # pragma: no cover

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