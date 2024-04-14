import coverage # pragma: no cover
import math # pragma: no cover

def func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0]*2]
    
    new_n = []
    i = math.floor(len(n)/2)

    new_n = new_n + func6(n[0:i])
    new_n = new_n + func6(n[i:])

    return new_n

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Single-element list
        n1 = [5]
        assert func6(n1) == [10]
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: List with even number of elements
        n2 = [1, 2, 3, 4]
        assert func6(n2) == [2, 4, 6, 8]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: List with odd number of elements
        n3 = [1, 2, 3, 4, 5]
        assert func6(n3) == [2, 4, 6, 8, 10]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Empty list
        n4 = []
        assert func6(n4) == []
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: List with negative numbers
        n5 = [-1, -2, -3, -4, -5]
        assert func6(n5) == [-2, -4, -6, -8, -10]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: List with all elements as zeros
        n6 = [0, 0, 0, 0]
        assert func6(n6) == [0, 0, 0, 0]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: List with all elements as ones
        n7 = [1, 1, 1, 1]
        assert func6(n7) == [2, 2, 2, 2]
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: List with mix of positive and negative numbers
        n8 = [1, -2, 3, -4, 5]
        assert func6(n8) == [2, -4, 6, -8, 10]
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: List with duplicate elements
        n9 = [2, 2, 3, 3, 4, 4]
        assert func6(n9) == [4, 4, 6, 6, 8, 8]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: List with large number of elements
        n10 = list(range(1000))
        expected_result = [i * 2 for i in range(1000)]
        assert func6(n10) == expected_result
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

cov = coverage.Coverage() # pragma: no cover
# start coverage
cov.start() # pragma: no cover

failed_ratio = psuedo_test_cases() / 10 # pragma: no cover

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