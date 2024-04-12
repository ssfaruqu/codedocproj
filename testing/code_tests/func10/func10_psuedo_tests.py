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

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Case 0 with non-empty strings
        a = "hello"
        b = ""
        c = 0
        expected_output = 'gknnq'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Case 1 with non-empty strings
        a = "world"
        b = ""
        c = 1
        expected_output = 'vaokn'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Case 2 with non-empty strings
        a = "python"
        b = ""
        c = 2
        expected_output = 'grutus'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Default case with non-empty strings
        a = "example"
        b = ""
        c = 3
        expected_output = 'cftwnz'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Case 0 with empty strings
        a = ""
        b = ""
        c = 0
        expected_output = ''
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Case 1 with empty strings
        a = ""
        b = ""
        c = 1
        expected_output = ''
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Case 2 with empty strings
        a = ""
        b = ""
        c = 2
        expected_output = ''
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Default case with empty strings
        a = ""
        b = ""
        c = 3
        expected_output = ''
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Case 0 with a single character
        a = "x"
        b = ""
        c = 0
        expected_output = 'y'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Case 1 with a single character
        a = "z"
        b = ""
        c = 1
        expected_output = 'y'
        assert func10(a, b, c) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

# Create a coverage object
cov = coverage.Coverage() # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

failed_ratio = psuedo_test_cases()/10 # pragma: no cover

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