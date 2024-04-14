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

#BULLET FLAT TESTS
def bullet_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Grid with single-element rows, reverse=False
        grid1 = [[1], [2], [3]]
        assert func11(grid1, False) == [[1, 1], [2, 2], [3, 3]]
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Grid with single-element rows, reverse=True
        grid2 = [[1], [2], [3]]
        assert func11(grid2, True) == [[1, 1], [2, 2], [3, 3]]
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Grid with two-element rows, reverse=False
        grid3 = [[1, 2], [3, 4], [5, 6]]
        assert func11(grid3, False) == [[2, 1], [4, 3], [6, 5]]
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Grid with two-element rows, reverse=True
        grid4 = [[1, 2], [3, 4], [5, 6]]
        assert func11(grid4, True) == [[2, 1], [4, 3], [6, 5]]
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Grid with empty rows, reverse=False
        grid5 = [[], [], []]
        assert func11(grid5, False) == [[], [], []]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Grid with empty rows, reverse=True
        grid6 = [[], [], []]
        assert func11(grid6, True) == [[], [], []]
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Grid with mixed-length rows, reverse=False
        grid7 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        assert func11(grid7, False) == [[1, 1], [3, 2], [6, 5, 4, 5, 6], [10, 9, 8, 7, 8, 9, 10]]
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Grid with mixed-length rows, reverse=True
        grid8 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        assert func11(grid8, True) == [[1, 1], [3, 2], [6, 5, 4, 5, 6], [10, 9, 8, 7, 8, 9, 10]]
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: Grid with nested lists, reverse=False
        grid9 = [[[1]], [[2], [3]], [[4, 5], [6, 7, 8]], [[]]]
        assert func11(grid9, False) == [[[1, 1]], [[3, 2], [3, 2]], [[5, 4, 5], [8, 7, 6, 7, 8]], [[]]]
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Grid with nested lists, reverse=True
        grid10 = [[[1]], [[2], [3]], [[4, 5], [6, 7, 8]], [[]]]
        assert func11(grid10, True) == [[[1, 1]], [[3, 2], [3, 2]], [[5, 4, 5], [8, 7, 6, 7, 8]], [[]]]
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

failed_ratio = bullet_flat_test_cases() / 10 # pragma: no cover

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