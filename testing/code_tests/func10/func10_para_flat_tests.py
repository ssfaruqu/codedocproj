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

#PARA FLAT TESTS
def para_flat_test_cases(): # pragma: no cover
    try:
        count = 1
        # Test case 1: c is 0, simple arithmetic operation
        assert func10("abc", "def", 0) == "hfn"
        count += 1
        # Test case 2: c is negative, no repetition
        assert func10("hello", "world", -2) == "c`c["
        count += 1
        # Test case 3: c is positive, repetition applied
        assert func10("hello", "world", 3) == "cccfkkkoxthhxhhh"
        count += 1
        # Test case 4: a is empty, result is empty
        assert func10("", "world", 2) == ""
        count += 1
        # Test case 5: b is empty, result is empty
        assert func10("hello", "", 2) == ""
        count += 1
        # Test case 6: a and b have different lengths, shorter length is considered
        assert func10("hello", "wo", 2) == "c`"
        count += 1
        # Test case 7: c is 1, no repetition
        assert func10("hello", "world", 1) == "c`c["
        count += 1
        # Test case 8: c is 0, a and b are equal
        assert func10("abc", "abc", 0) == "hfh"
        count += 1
        # Test case 9: c is 2, repetition applied
        assert func10("abc", "def", 2) == "hfnhfn"
        count += 1
        # Test case 10: c is negative, a and b are equal
        assert func10("hello", "hello", -2) == "eaeaa@Y@Y"
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("PARA FLAT TEST CASE FAILED\n")

para_flat_test_cases() # pragma: no cover

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

print("Para Flat Coverage Percentage:", coverage_percentage) # pragma: no cover