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

#PARA STRUC TESTS
def para_struc_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Basic test case with c=0
        a1 = "hello"
        b1 = "world"
        c1 = 0
        expected_output1 = "wzcz`"
        output1 = func10(a1, b1, c1)
        assert output1 == expected_output1
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Basic test case with c=1
        a2 = "hello"
        b2 = "world"
        c2 = 1
        expected_output2 = "wzcz`wzcz`wzcz`wzcz`wzcz`"
        output2 = func10(a2, b2, c2)
        assert output2 == expected_output2
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Test with empty strings and c=2
        a3 = ""
        b3 = ""
        c3 = 2
        expected_output3 = ""
        output3 = func10(a3, b3, c3)
        assert output3 == expected_output3
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Test with c=10
        a4 = "abc"
        b4 = "defg"
        c4 = 10
        expected_output4 = "efghijpoxy"
        output4 = func10(a4, b4, c4)
        assert output4 == expected_output4
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Test with c=-3
        a5 = "xyz"
        b5 = "abc"
        c5 = -3
        expected_output5 = "[]_"
        output5 = func10(a5, b5, c5)
        assert output5 == expected_output5
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Test with c=5 and longer strings
        a6 = "abcdefghi"
        b6 = "jklmnopqr"
        c6 = 5
        expected_output6 = "jmfoqszfmv"
        output6 = func10(a6, b6, c6)
        assert output6 == expected_output6
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Test with c=3 and special characters
        a7 = "!@#$%"
        b7 = "&*()_"
        c7 = 3
        expected_output7 = "'*+,-"
        output7 = func10(a7, b7, c7)
        assert output7 == expected_output7
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Test with c=1 and one empty string
        a8 = "abc"
        b8 = ""
        c8 = 1
        expected_output8 = "cdf"
        output8 = func10(a8, b8, c8)
        assert output8 == expected_output8
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Test with c=2 and different lengths of strings
        a9 = "1234"
        b9 = "56789"
        c9 = 2
        expected_output9 = "5785"
        output9 = func10(a9, b9, c9)
        assert output9 == expected_output9
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Test with c=4 and strings with repeating characters
        a10 = "aaabbb"
        b10 = "cccd"
        c10 = 4
        expected_output10 = "cccdcccddcccdcccddcccdcccdd"
        output10 = func10(a10, b10, c10)
        assert output10 == expected_output10
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

cov = coverage.Coverage(data_suffix=True) # pragma: no cover
# start coverage
cov.start() # pragma: no cover

failed_ratio = para_struc_test_cases() / 10 # pragma: no cover

# stop coverage
cov.stop() # pragma: no cover
# make report
cov.save() # pragma: no cover
cov.combine() # pragma: no cover
cov.save() # pragma: no cover
# load report
cov.load() # pragma: no cover

# print report
coverage_percentage = cov.report() * 0.01 # pragma: no cover