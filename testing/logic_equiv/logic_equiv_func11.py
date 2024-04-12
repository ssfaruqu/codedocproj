import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

x = np.random.randint(1, 7)
y = np.random.randint(1, 7)
rand_grid = list(np.random.randint(-10, 10, size=[x, y]))
print(rand_grid)

@given(reverse= st.integers(min_value=0, max_value=1))
def test_para_flat_func11(reverse):
    orig =  orig_func11(reverse)
    flat = para_flat_func11(reverse)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(reverse= st.integers(min_value=0, max_value=1))
def test_para_struc_func11(reverse):
    orig =  orig_func11(reverse)
    struc =  para_struc_func11(reverse)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(reverse= st.integers(min_value=0, max_value=1))
def test_bullet_flat_func11(reverse):
    orig =  orig_func11(reverse)
    flat = bullet_flat_func11(reverse)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(reverse= st.integers(min_value=0, max_value=1))
def test_bullet_struc_func11(reverse):
    orig =  orig_func11(reverse)
    struc =  bullet_struc_func11(reverse)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(reverse= st.integers(min_value=0, max_value=1))
def test_psuedo_func11(reverse):
    orig =  orig_func11(reverse)
    psuedo = psuedo_func11(reverse)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo

def orig_func11(reverse, grid= rand_grid):
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

def para_flat_func11(reverse, grid=rand_grid):
    """
    Processes a 2D grid by rearranging its elements.

    Args:
    - grid (list of lists): The 2D grid to be processed.
    - reverse (bool, optional): A flag indicating whether to reverse the elements of each row. Default is False.

    Returns:
    - list of lists: The processed 2D grid.
    """
    def process_row(row):
        """
        Processes a single row of the grid by rearranging its elements.

        Args:
        - row (list): The row to be processed.

        Returns:
        - list: The processed row.
        """
        # Rearrange elements of the row (example: sorting, reversing, etc.)
        row.sort()  # Example: sorting the elements of the row
        if reverse:
            row.reverse()  # Reverse the elements of the row if reverse parameter is True
        return row

    # Iterate over each row of the grid and apply process_row function
    processed_grid = [process_row(row) for row in grid]

    return processed_grid

#PART OF para_struc_func11
def process_row(row):
    if len(row) <= 1:
        return row
    else:
        return [row[-1]] + process_row(row[:-1]) + [row[0]]

def para_struc_func11(reverse, grid= rand_grid):
    modified_grid = []
    for row in grid:
        processed_row = process_row(row)
        if reverse:
            processed_row = processed_row[::-1]
        modified_grid.append(processed_row)
    return modified_grid


def bullet_flat_func11(reverse, grid= rand_grid):
    """
    Process the rows of a 2D grid based on certain conditions.

    Args:
    - grid: A 2D list representing a grid.
    - reverse: A boolean indicating whether to reverse the rows of the grid.

    Returns:
    - The modified grid after processing the rows.
    """

    def process_row(row):
        """
        Process each row of the grid based on certain conditions.

        Args:
        - row: A list representing a row of the grid.

        Returns:
        - The processed row.
        """
        # If the length of the row is 1, return a list with the element repeated twice
        if len(row) == 1:
            return [row[0], row[0]]
        # If the length of the row is 2, return a list with elements swapped
        elif len(row) == 2:
            return [row[1], row[0]]
        # If the length of the row is 0, return the row as it is
        elif len(row) == 0:
            return row
        # Otherwise, divide the row into two halves, recursively process each half, and concatenate the results
        else:
            mid = len(row) // 2
            left_half = process_row(row[:mid])
            right_half = process_row(row[mid:])
            return left_half + right_half

    # Iterate over each row of the grid
    for i in range(len(grid)):
        # Apply the process_row function to each row and update the row with the processed result
        grid[i] = process_row(grid[i])
        # If reverse is True, reverse the elements of each row
        if reverse:
            grid[i] = grid[i][::-1]

    return grid

def bullet_struc_func11(reverse=False, grid= rand_grid):
    def process_row(row):
        if len(row) == 1:
            return [row[0]] * 2
        elif len(row) == 2:
            return [row[1], row[0]]
        elif len(row) == 0:
            return row
        else:
            mid = len(row) // 2
            left_half = process_row(row[:mid])
            right_half = process_row(row[mid:])
            return left_half + right_half

    for i in range(len(grid)):
        grid[i] = process_row(grid[i])
        if reverse:
            grid[i] = grid[i][::-1]

    return grid


def psuedo_func11(reverse, grid= rand_grid):
    def process_row(row):
        if len(row) == 1:
            return [row[0], row[0]]
        elif len(row) == 2:
            return [row[1], row[0]]
        elif len(row) == 0:
            return row

        mid = len(row) // 2
        lower_half = process_row(row[:mid])
        upper_half = process_row(row[mid:])
        return lower_half + upper_half

    for i in range(len(grid)):
        grid[i] = process_row(grid[i])

        if reverse:
            low = 0
            high = len(grid[i]) - 1
            while low < high:
                grid[i][low], grid[i][high] = grid[i][high], grid[i][low]
                low += 1
                high -= 1

    return grid


def try_test(test, test_fail_string, test_pass_string):
    try:
        test()
        print(test_pass_string)
        print("")
        return 1
    except Exception as e:
        print(test_fail_string)
        print(repr(e))
        print("")
        return 0

def getPassArr():
    return pass_arr

print("----- func11 LOGIC EQUIV TESTING -------")
pass_arr = [0,0,0,0,0]
pass_arr[0] = try_test(test_para_flat_func11, "PARA FLAT FAIL", "PARA FLAT PASS")
pass_arr[1] = try_test(test_para_struc_func11, "PARA STRUC FAIL", "PARA STRUC PASS")
pass_arr[2] = try_test(test_bullet_flat_func11, "BULLET FLAT FAIL", "BULLET FLAT PASS")
pass_arr[3] = try_test(test_bullet_struc_func11, "BULLET STRUC FAIL", "BULLET STRUC PASS")
pass_arr[4] = try_test(test_psuedo_func11, "PSUEDO FAIL", "PSUEDO PASS")
