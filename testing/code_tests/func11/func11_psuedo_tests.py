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

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Regular grid with reverse False
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        reverse = False
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Regular grid with reverse True
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        reverse = True
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Empty grid with reverse False
        grid = []
        reverse = False
        expected_output = []
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Empty grid with reverse True
        grid = []
        reverse = True
        expected_output = []
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Grid with one row with reverse False
        grid = [[1, 2, 3]]
        reverse = False
        expected_output = [[3, 2, 1]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Grid with one row with reverse True
        grid = [[1, 2, 3]]
        reverse = True
        expected_output = [[3, 2, 1]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Grid with one column with reverse False
        grid = [[1], [2], [3]]
        reverse = False
        expected_output = [[1], [2], [3]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Grid with one column with reverse True
        grid = [[1], [2], [3]]
        reverse = True
        expected_output = [[1], [2], [3]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Grid with odd-sized rows with reverse False
        grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        reverse = False
        expected_output = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [15, 14, 13, 12, 11]]
        assert func11(grid, reverse) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Grid with even-sized rows with reverse True
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        reverse = True
        expected_output = [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]
        assert func11(grid, reverse) == expected_output
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