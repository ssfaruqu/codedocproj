import coverage # pragma: no cover
import math # pragma: no cover

def func11(grid, reverse):
    def process_row(row):
        if len(row) == 1:
            return [row[0], row[0]]
        elif len(row) == 2:
            return [row[1], row[0]]
        elif len(row) == 0:
            return row
    
        mid = math.floor(len(row)/2)
        lower = row[0:mid]
        upper = row[mid:]

        ret = process_row(lower) + process_row(upper)

        return ret
    
    for i in range(len(grid)):
        grid[i] = process_row(grid[i])

        if reverse:
            low = 0
            high = len(grid[i]) - 1
            while low < high:
                temp = grid[i][low]
                grid[i][low] = grid[i][high]
                grid[i][high] = temp
                low += 1
                high -= 1

    return grid

#PARA STRUC TESTS
def para_struc_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Basic test case with reverse=False
        grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output1 = func11(grid1, False)
        assert output1 == expected_output1
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Basic test case with reverse=True
        grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        output2 = func11(grid2, True)
        assert output2 == expected_output2
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Test with empty grid
        grid3 = []
        expected_output3 = []
        output3 = func11(grid3, False)
        assert output3 == expected_output3
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Test with grid containing one row
        grid4 = [[1, 2, 3]]
        expected_output4 = [[3, 2, 1]]
        output4 = func11(grid4, False)
        assert output4 == expected_output4
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Test with grid containing one column
        grid5 = [[1], [2], [3]]
        expected_output5 = [[1], [2], [3]]
        output5 = func11(grid5, False)
        assert output5 == expected_output5
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Test with grid containing negative numbers
        grid6 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_output6 = [[-3, -2, -1], [-6, -5, -4], [-9, -8, -7]]
        output6 = func11(grid6, True)
        assert output6 == expected_output6
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Test with grid containing duplicate elements
        grid7 = [[1, 2, 3, 3], [4, 5, 5, 6], [7, 7, 8, 9]]
        expected_output7 = [[3, 3, 2, 1], [6, 5, 5, 4], [9, 8, 7, 7]]
        output7 = func11(grid7, False)
        assert output7 == expected_output7
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Test with large grid
        grid8 = [[i for i in range(100)] for _ in range(100)]
        expected_output8 = [[99, 98, 97, ..., 2, 1, 0] for _ in range(100)]
        output8 = func11(grid8, True)
        assert output8 == expected_output8
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Test with grid containing strings
        grid9 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        expected_output9 = [['c', 'b', 'a'], ['f', 'e', 'd'], ['i', 'h', 'g']]
        output9 = func11(grid9, True)
        assert output9 == expected_output9
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Test with grid containing mixed types
        grid10 = [[1, 'a', 3], ['b', 5, 'c'], [7, 'd', 9]]
        expected_output10 = [[3, 'a', 1], ['c', 5, 'b'], [9, 'd', 7]]
        output10 = func11(grid10, True)
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