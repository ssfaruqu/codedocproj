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

#PARA FLAT TESTS
def para_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Basic test with reverse=False
        grid1 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        processed_grid1 = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
        assert func11(grid1, reverse=False) == processed_grid1
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Basic test with reverse=True
        grid2 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        processed_grid2 = [[3, 2, 1],
                        [6, 5, 4],
                        [9, 8, 7]]
        assert func11(grid2, reverse=True) == processed_grid2
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Empty grid, no processing
        grid3 = []
        assert func11(grid3, reverse=False) == []
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Single row grid, no processing
        grid4 = [[1, 2, 3]]
        assert func11(grid4, reverse=False) == [[1, 2, 3]]
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Single element grid, no processing
        grid5 = [[1]]
        assert func11(grid5, reverse=False) == [[1]]
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Large grid, reverse=False
        grid6 = [[i for i in range(1, 6)] for _ in range(5)]
        processed_grid6 = [[1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5]]
        assert func11(grid6, reverse=False) == processed_grid6
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Large grid, reverse=True
        grid7 = [[i for i in range(1, 6)] for _ in range(5)]
        processed_grid7 = [[5, 4, 3, 2, 1],
                        [5, 4, 3, 2, 1],
                        [5, 4, 3, 2, 1],
                        [5, 4, 3, 2, 1],
                        [5, 4, 3, 2, 1]]
        assert func11(grid7, reverse=True) == processed_grid7
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Grid with negative numbers, reverse=False
        grid8 = [[-1, -2, -3],
                [-4, -5, -6],
                [-7, -8, -9]]
        processed_grid8 = [[-1, -2, -3],
                        [-4, -5, -6],
                        [-7, -8, -9]]
        assert func11(grid8, reverse=False) == processed_grid8
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: Grid with duplicate rows, reverse=True
        grid9 = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
        processed_grid9 = [[3, 2, 1],
                        [3, 2, 1],
                        [3, 2, 1]]
        assert func11(grid9, reverse=True) == processed_grid9
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Grid with mixed types, reverse=False
        grid10 = [[1, 'a', True],
                [False, 2, 'b'],
                ['c', 3, None]]
        processed_grid10 = [[1, 'a', True],
                            [False, 2, 'b'],
                            ['c', 3, None]]
        assert func11(grid10, reverse=False) == processed_grid10
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

failed_ratio = para_flat_test_cases() / 10 # pragma: no cover

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