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

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Empty list input
        assert func6([]) == []

        count += 1 # Test 2: Single element list input
        assert func6([5]) == [10]

        count += 1 # Test 3: List with two elements
        assert func6([3, 7]) == [6, 14]

        count += 1 # Test 4: List with multiple even number of elements
        assert func6([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 8, 10, 12]

        count += 1 # Test 5: List with multiple odd number of elements
        assert func6([2, 4, 6, 8, 10]) == [4, 8, 12, 16, 20]

        count += 1 # Test 6: List with all elements as negative numbers
        assert func6([-2, -4, -6, -8]) == [-4, -8, -12, -16]

        count += 1 # Test 7: List with all elements as positive numbers
        assert func6([1, 2, 3, 4]) == [2, 4, 6, 8]

        count += 1 # Test 8: List with a mix of positive and negative numbers
        assert func6([-1, 2, -3, 4, -5]) == [-2, 4, -6, 8, -10]

        count += 1 # Test 9: List with floating-point numbers
        assert func6([1.5, 2.5, 3.5]) == [3.0, 5.0, 7.0]

        count += 1 # Test 10: List with string elements
        assert func6(['a', 'b', 'c']) == ['aa', 'bb', 'cc']

        print("All tests passed!")
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("BULLET STRUC TEST CASE FAILED\n")

bullet_struc_test_cases() # pragma: no cover

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