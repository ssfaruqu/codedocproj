import coverage # pragma: no cover
import math # pragma: no cover

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

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
    try:
        count = 1 # Test case 1: Empty list
        assert func6([]) == []

        count += 1 # Test case 2: Single-element list
        assert func6([1]) == [2]

        count += 1 # Test case 3: Two-element list
        assert func6([2, 3]) == [4, 6]

        count += 1 # Test case 4: Three-element list
        assert func6([4, 5, 6]) == [8, 10, 12]

        count += 1 # Test case 5: Four-element list
        assert func6([7, 8, 9, 10]) == [14, 16, 18, 20]

        count += 1 # Test case 6: Odd-length list
        assert func6([11, 12, 13, 14, 15]) == [22, 24, 26, 28, 30]

        count += 1 # Test case 7: Large list with even length
        assert func6(list(range(100))) == list(range(0, 200, 2))

        count += 1 # Test case 8: Large list with odd length
        assert func6(list(range(101))) == list(range(0, 202, 2))

        count += 1 # Test case 9: List of strings
        assert func6(["a", "b", "c"]) == ["aa", "bb", "cc"]

        count += 1 # Test case 10: List of mixed types
        assert func6([1, "two", [3, 4], {"five": 6}]) == [2, "twotwo", [6, 8], {"five": 6}]

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