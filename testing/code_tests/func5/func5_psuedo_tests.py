import coverage # pragma: no cover
import numpy as np # pragma: no cover

# Create a coverage object
cov = coverage.Coverage() # pragma: no cover

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

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Horizontal win for player 1
        player_number = 1
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 2
        col = 0
        assert func5(player_number, board, row, col) == 10000

        count += 1 # Test 2: Vertical win for player 2
        player_number = 2
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0]
        ]
        row = 2
        col = 0
        assert func5(player_number, board, row, col) == -10000

        count += 1 # Test 3: Diagonal win for player 1
        player_number = 1
        board = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 0
        col = 0
        assert func5(player_number, board, row, col) == 10000

        count += 1 # Test 4: No win
        player_number = 1
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 2
        col = 0
        assert func5(player_number, board, row, col) == 2

        count += 1 # Test 5: Player 2 with no available moves
        player_number = 2
        board = [
            [1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1]
        ]
        row = 0
        col = 0
        assert func5(player_number, board, row, col) == -6

        count += 1 # Test 6: Empty board
        player_number = 1
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 0
        col = 0
        assert func5(player_number, board, row, col) == 3

        count += 1 # Test 7: Player 1 with a nearly winning move
        player_number = 1
        board = [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 0
        col = 0
        assert func5(player_number, board, row, col) == 2

        count += 1 # Test 8: Player 2 with a nearly winning move
        player_number = 2
        board = [
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 1
        col = 0
        assert func5(player_number, board, row, col) == -2

        count += 1 # Test 9: Player 1 with multiple winning possibilities
        player_number = 1
        board = [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 2
        col = 1
        assert func5(player_number, board, row, col) == 10000

        count += 1 # Test 10: Player 2 with multiple winning possibilities
        player_number = 2
        board = [
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row = 2
        col = 1
        assert func5(player_number, board, row, col) == -10000

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