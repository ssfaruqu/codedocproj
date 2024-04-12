import coverage # pragma: no cover
import numpy as np # pragma: no cover

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

def func5(player_number, board, row, col):
    score = 1 
    uv_score, lh_score, rh_score = 1, 1, 1
        
    our_piece = board[row][col]
    if int(our_piece) != player_number: 
        sign = -1
    else: sign = 1

    max_col = len(board[0]) - 1
    max_row = len(board) - 1
        
    for i in range(1, 4):
        if row+i > max_row:
            break

        if board[row+i][col] == our_piece:
            if(i == 3): return sign*10000
            else: uv_score *= 2
        elif board[row+i][col] == 0:          
            break
        else:                                  
            uv_score = 0
            break
   
    for i in range(1, 4):
        if col-i < 0:
            break

        if board[row][col-i] == our_piece:    
            if(i == 3): return sign*10000
            else: lh_score *= 2
        elif board[row][col-i] == 0:         
            break
        else:                                 
            lh_score = 0
            break
    
    for i in range(1, 4):
        if col+i > max_col:
            break

        if board[row][col+i] == our_piece:    
            if(i == 3): return sign*10000
            else: rh_score *= 2
        elif board[row][col+i] == 0:           
            break
        else:                                 
            rh_score = 0
            break

    score = uv_score + lh_score + rh_score
         
    return sign*score

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    try:
        
        count = 1 # Test 1: All empty board
        board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        assert func5(1, 1, 1, board) == 1

        count += 1 # Test 2: Player's piece in the center with no opponent pieces nearby
        board = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        assert func5(1, 1, 1, board) == 10000

        count += 1 # Test 3: Player's piece on the edge with no opponent pieces nearby
        board = [[1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        assert func5(1, 0, 0, board) == 10000

        count += 1 # Test 4: Player's piece in the center with opponent piece nearby in all directions
        board = [[2, 2, 2],
                [2, 1, 2],
                [2, 2, 2]]
        assert func5(1, 1, 1, board) == 1

        count += 1 # Test 5: Player's piece with 3 consecutive pieces horizontally
        board = [[2, 1, 0],
                [2, 1, 0],
                [2, 1, 0]]
        assert func5(1, 0, 1, board) == 10000

        count += 1 # Test 6: Player's piece with 3 consecutive pieces vertically
        board = [[2, 2, 2],
                [1, 1, 1],
                [0, 0, 0]]
        assert func5(1, 1, 0, board) == 10000

        count += 1 # Test 7: Player's piece with 3 consecutive pieces diagonally left
        board = [[2, 0, 0],
                [1, 2, 0],
                [1, 1, 2]]
        assert func5(1, 1, 1, board) == 10000

        count += 1 # Test 8: Player's piece with 3 consecutive pieces diagonally right
        board = [[0, 0, 2],
                [0, 2, 1],
                [2, 1, 1]]
        assert func5(1, 1, 1, board) == 10000

        count += 1 # Test 9: Player's piece with 2 consecutive pieces diagonally right and 1 empty cell
        board = [[0, 0, 1],
                [0, 1, 0],
                [1, 0, 0]]
        assert func5(1, 1, 1, board) == 20000

        count += 1 # Test 10: Player's piece in the corner with 2 consecutive pieces horizontally and 1 empty cell
        board = [[1, 0, 0],
                [1, 1, 0],
                [0, 0, 0]]
        assert func5(1, 0, 0, board) == 20000

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