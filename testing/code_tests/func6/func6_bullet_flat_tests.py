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

#BULLET FLAT TESTS
def bullet_flat_test_cases(): # pragma: no cover
    try:
        count = 1 # Test case 1: Single-element list
        assert func6([5]) == [10]

        count += 1 # Test case 2: Two-element list
        assert func6([3, 7]) == [6, 14]

        count += 1 # Test case 3: Three-element list
        assert func6([2, 4, 6]) == [4, 8, 12]

        count += 1 # Test case 4: Four-element list
        assert func6([1, 2, 3, 4]) == [2, 4, 6, 8]

        count += 1 # Test case 5: Five-element list
        assert func6([5, 10, 15, 20, 25]) == [10, 20, 30, 40, 50]

        count += 1 # Test case 6: Large list
        assert func6(list(range(1, 11))) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

        count += 1 # Test case 7: List with negative numbers
        assert func6([-2, -4, -6, -8]) == [-4, -8, -12, -16]

        count += 1 # Test case 8: List with zeros
        assert func6([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

        count += 1 # Test case 9: List with mixed positive and negative numbers
        assert func6([-3, 5, -7, 9, -11]) == [-6, 10, -14, 18, -22]

        count += 1 # Test case 10: Empty list
        assert func6([]) == []

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