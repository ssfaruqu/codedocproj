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

#PARA STRUC TESTS
def para_struc_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Basic test case with player 1 having consecutive pieces horizontally
        player_number1 = 1
        board1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1]
        ]
        row1 = 4
        col1 = 2
        expected_score1 = 3
        score1 = func5(player_number1, board1, row1, col1)
        assert score1 == expected_score1

        count += 1 # Test 2: Test case with player 2 having consecutive pieces diagonally
        player_number2 = 2
        board2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 2]
        ]
        row2 = 3
        col2 = 3
        expected_score2 = -3
        score2 = func5(player_number2, board2, row2, col2)
        assert score2 == expected_score2

        count += 1 # Test 3: Test case with no consecutive pieces
        player_number3 = 1
        board3 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row3 = 2
        col3 = 2
        expected_score3 = 0
        score3 = func5(player_number3, board3, row3, col3)
        assert score3 == expected_score3

        count += 1 # Test 4: Test case with player 2 having consecutive pieces vertically
        player_number4 = 2
        board4 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 2, 0, 0]
        ]
        row4 = 2
        col4 = 2
        expected_score4 = -2
        score4 = func5(player_number4, board4, row4, col4)
        assert score4 == expected_score4

        count += 1 # Test 5: Test case with player 1 having consecutive pieces diagonally
        player_number5 = 1
        board5 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        row5 = 3
        col5 = 3
        expected_score5 = 2
        score5 = func5(player_number5, board5, row5, col5)
        assert score5 == expected_score5

        count += 1 # Test 6: Test case with player 1 having consecutive pieces horizontally and diagonally
        player_number6 = 1
        board6 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0]
        ]
        row6 = 2
        col6 = 2
        expected_score6 = 5
        score6 = func5(player_number6, board6, row6, col6)
        assert score6 == expected_score6

        count += 1 # Test 7: Test case with player 2 having consecutive pieces horizontally and vertically
        player_number7 = 2
        board7 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [2, 2, 2, 0, 0],
            [0, 0, 2, 0, 0]
        ]
        row7 = 3
        col7 = 2
        expected_score7 = -7
        score7 = func5(player_number7, board7, row7, col7)
        assert score7 == expected_score7

        count += 1 # Test 8: Test case with player 1 having consecutive pieces horizontally, vertically, and diagonally
        player_number8 = 1
        board8 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        row8 = 2
        col8 = 2
        expected_score8 = 8
        score8 = func5(player_number8, board8, row8, col8)
        assert score8 == expected_score8

        count += 1 # Test 9: Test case with player 2 having consecutive pieces horizontally and diagonally
        player_number9 = 2
        board9 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 2, 2, 0, 0],
            [2, 0, 0, 0, 0]
        ]
        row9 = 3
        col9 = 2
        expected_score9 = -4
        score9 = func5(player_number9, board9, row9, col9)
        assert score9 == expected_score9

        count += 1 # Test 10: Test case with player 1 having consecutive pieces horizontally, vertically, and diagonally
        player_number10 = 1
        board10 = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0]
        ]
        row10 = 3
        col10 = 2
        expected_score10 = 12
        score10 = func5(player_number10,

        board10, row10, col10)
        assert score10 == expected_score10

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