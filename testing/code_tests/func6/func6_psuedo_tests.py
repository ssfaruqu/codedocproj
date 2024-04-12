import coverage # pragma: no cover
import math # pragma: no cover

# Create a coverage object
cov = coverage.Coverage() # pragma: no cover

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

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Single-element list
        n = [5]
        assert func6(n) == [10]

        count += 1 # Test 2: List with even number of elements
        n = [1, 2, 3, 4]
        assert func6(n) == [2, 4, 6, 8]

        count += 1 # Test 3: List with odd number of elements
        n = [1, 2, 3, 4, 5]
        assert func6(n) == [2, 4, 6, 8, 10]

        count += 1 # Test 4: Empty list
        n = []
        assert func6(n) == []

        count += 1 # Test 5: List with negative numbers
        n = [-1, -2, -3, -4, -5]
        assert func6(n) == [-2, -4, -6, -8, -10]

        count += 1 # Test 6: List with all elements as zeros
        n = [0, 0, 0, 0]
        assert func6(n) == [0, 0, 0, 0]

        count += 1 # Test 7: List with all elements as ones
        n = [1, 1, 1, 1]
        assert func6(n) == [2, 2, 2, 2]

        count += 1 # Test 8: List with mix of positive and negative numbers
        n = [1, -2, 3, -4, 5]
        assert func6(n) == [2, -4, 6, -8, 10]

        count += 1 # Test 9: List with duplicate elements
        n = [2, 2, 3, 3, 4, 4]
        assert func6(n) == [4, 4, 6, 6, 8, 8]

        count += 1 # Test 10: List with large number of elements
        n = list(range(1000))
        expected_result = [i * 2 for i in range(1000)]
        assert func6(n) == expected_result

        print("All tests passed successfully!")
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("PSUEDO TEST CASE FAILED\n")

psuedo_test_cases() # pragma: no cover

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

print("Psuedo Coverage Percentage:", coverage_percentage) # pragma: no cover