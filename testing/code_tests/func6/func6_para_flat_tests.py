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

#PARA FLAT TESTS
def para_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Empty list
        assert func6([]) == []
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Single-element list
        assert func6([1]) == [2]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Two-element list
        assert func6([2, 3]) == [4, 6]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Three-element list
        assert func6([4, 5, 6]) == [8, 10, 12]
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Four-element list
        assert func6([7, 8, 9, 10]) == [14, 16, 18, 20]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Odd-length list
        assert func6([11, 12, 13, 14, 15]) == [22, 24, 26, 28, 30]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Large list with even length
        assert func6(list(range(100))) == list(range(0, 200, 2))
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Large list with odd length
        assert func6(list(range(101))) == list(range(0, 202, 2))
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: List of strings
        assert func6(["a", "b", "c"]) == ["aa", "bb", "cc"]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: List of mixed types
        assert func6([1, "two", [3, 4], {"five": 6}]) == [2, "twotwo", [6, 8], {"five": 6}]
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

failed_ratio = para_flat_test_cases() / 10 # pragma: no cover

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