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

#BULLET FLAT TESTS
def bullet_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Single-element list
        assert func6([5]) == [10]
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Two-element list
        assert func6([3, 7]) == [6, 14]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Three-element list
        assert func6([2, 4, 6]) == [4, 8, 12]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Four-element list
        assert func6([1, 2, 3, 4]) == [2, 4, 6, 8]
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Five-element list
        assert func6([5, 10, 15, 20, 25]) == [10, 20, 30, 40, 50]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Large list
        assert func6(list(range(1, 11))) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: List with negative numbers
        assert func6([-2, -4, -6, -8]) == [-4, -8, -12, -16]
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: List with zeros
        assert func6([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: List with mixed positive and negative numbers
        assert func6([-3, 5, -7, 9, -11]) == [-6, 10, -14, 18, -22]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Empty list
        assert func6([]) == []
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

failed_ratio = bullet_flat_test_cases()/10 # pragma: no cover

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
