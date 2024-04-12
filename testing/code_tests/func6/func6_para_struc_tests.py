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

#PARA STRUC TESTS
def para_struc_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Basic test case with a list of integers
        input_list1 = [1, 2, 3, 4, 5]
        expected_output1 = [2, 4, 6, 8, 10]
        output1 = func6(input_list1)
        assert output1 == expected_output1

        count += 1 # Test 2: Test with an empty list
        input_list2 = []
        expected_output2 = []
        output2 = func6(input_list2)
        assert output2 == expected_output2

        count += 1 # Test 3: Test with a list containing only one element
        input_list3 = [7]
        expected_output3 = [14]
        output3 = func6(input_list3)
        assert output3 == expected_output3

        count += 1 # Test 4: Test with a list containing negative numbers
        input_list4 = [-2, -4, -6]
        expected_output4 = [-4, -8, -12]
        output4 = func6(input_list4)
        assert output4 == expected_output4

        count += 1 # Test 5: Test with a list containing floats
        input_list5 = [0.5, 1.5, 2.5]
        expected_output5 = [1.0, 3.0, 5.0]
        output5 = func6(input_list5)
        assert output5 == expected_output5

        count += 1 # Test 6: Test with a list containing strings
        input_list6 = ["hello", "world"]
        expected_output6 = ["hellohello", "worldworld"]
        output6 = func6(input_list6)
        assert output6 == expected_output6

        count += 1 # Test 7: Test with a list of mixed types
        input_list7 = [1, "abc", 3.5]
        expected_output7 = [2, "abcabc", 7.0]
        output7 = func6(input_list7)
        assert output7 == expected_output7

        count += 1 # Test 8: Test with a list of boolean values
        input_list8 = [True, False, True]
        expected_output8 = [2, 0, 2]
        output8 = func6(input_list8)
        assert output8 == expected_output8

        count += 1 # Test 9: Test with a longer list
        input_list9 = list(range(1, 11))
        expected_output9 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        output9 = func6(input_list9)
        assert output9 == expected_output9

        count += 1 # Test 10: Test with a list containing repeating elements
        input_list10 = [2, 2, 2, 2]
        expected_output10 = [4, 4, 4, 4]
        output10 = func6(input_list10)
        assert output10 == expected_output10

        print("All tests passed!")
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("PARA STRUC TEST CASE FAILED\n")

para_struc_test_cases() # pragma: no cover

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

print("Para Struc Coverage Percentage:", coverage_percentage) # pragma: no cover