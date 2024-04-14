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

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Empty grid
        grid = []
        assert func11(grid, False) == []
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Single-element grid
        grid = [[1]]
        assert func11(grid, False) == [[1, 1]]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Grid with two elements
        grid = [[1, 2]]
        assert func11(grid, False) == [[2, 1]]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Grid with three elements
        grid = [[1, 2, 3]]
        assert func11(grid, False) == [[1, 2, 3, 1, 2, 3]]
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Grid with four elements
        grid = [[1, 2],
                [3, 4]]
        assert func11(grid, False) == [[2, 1],
                                        [4, 3]]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Grid with five elements
        grid = [[1, 2, 3],
                [4, 5, 6]]
        assert func11(grid, False) == [[1, 2, 3, 1, 2, 3],
                                        [4, 5, 6, 4, 5, 6]]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Grid with rows reversed
        grid = [[1, 2],
                [3, 4]]
        assert func11(grid, True) == [[4, 3],
                                        [2, 1]]
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Grid with elements swapped and rows reversed
        grid = [[1, 2, 3],
                [4, 5, 6]]
        assert func11(grid, True) == [[6, 5, 4, 3, 2, 1],
                                        [3, 2, 1, 6, 5, 4]]
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Grid with multiple rows and columns
        grid = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]]
        assert func11(grid, False) == [[1, 2, 3, 4, 1, 2, 3, 4],
                                        [5, 6, 7, 8, 5, 6, 7, 8],
                                        [9, 10, 11, 12, 9, 10, 11, 12]]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Grid with multiple rows and columns, rows reversed
        grid = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]]
        assert func11(grid, True) == [[4, 3, 2, 1, 4, 3, 2, 1],
                                        [8, 7, 6, 5, 8, 7, 6, 5],
                                        [12, 11, 10, 9, 12, 11, 10, 9]]
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

failed_ratio = bullet_struc_test_cases() / 10 # pragma: no cover

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