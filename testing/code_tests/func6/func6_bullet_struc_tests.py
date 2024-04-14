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

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Empty list input
        assert func6([]) == []
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Single element list input
        assert func6([5]) == [10]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: List with two elements
        assert func6([3, 7]) == [6, 14]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: List with multiple even number of elements
        assert func6([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 8, 10, 12]
    except Exception as e:
        print(f"{repr(e)} on test csae 4")
        count += 1

    try:
        # Test 5: List with multiple odd number of elements
        assert func6([2, 4, 6, 8, 10]) == [4, 8, 12, 16, 20]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: List with all elements as negative numbers
        assert func6([-2, -4, -6, -8]) == [-4, -8, -12, -16]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: List with all elements as positive numbers
        assert func6([1, 2, 3, 4]) == [2, 4, 6, 8]
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: List with a mix of positive and negative numbers
        assert func6([-1, 2, -3, 4, -5]) == [-2, 4, -6, 8, -10]
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: List with floating-point numbers
        assert func6([1.5, 2.5, 3.5]) == [3.0, 5.0, 7.0]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: List with string elements
        assert func6(['a', 'b', 'c']) == ['aa', 'bb', 'cc']
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

failed_ratio = bullet_struc_test_cases() # pragma: no cover

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