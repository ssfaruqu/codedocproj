import coverage # pragma: no cover
import numpy as np # pragma: no cover

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

#BULLET FLAT TESTS
def bullet_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Empty board, player at position (0, 0)
        assert func5(1, 0, 0, [[' ']*3 for _ in range(3)]) == 1
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Player has 3 consecutive pieces vertically
        assert func5('X', 0, 0, [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', 'O']]) == 10000
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Player has 3 consecutive pieces horizontally
        assert func5('O', 1, 0, [['X', 'X', 'O'], [' ', 'O', 'O'], ['X', ' ', 'O']]) == -10000
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Player has 3 consecutive pieces diagonally (top-left to bottom-right)
        assert func5('X', 0, 0, [['X', 'O', ' '], [' ', 'X', ' '], ['O', 'O', 'X']]) == 10000
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Player has 3 consecutive pieces diagonally (top-right to bottom-left)
        assert func5('X', 0, 2, [[' ', 'O', 'X'], [' ', 'X', ' '], ['X', 'O', 'O']]) == 10000
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Player has 2 consecutive pieces in all directions
        assert func5('X', 1, 1, [['X', 'X', 'O'], ['O', 'X', ' '], ['O', ' ', 'O']]) == 4
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Player has 1 piece surrounded by opponents
        assert func5('X', 1, 1, [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']]) == 1
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Player has 3 consecutive pieces with some opponents in between
        assert func5('X', 0, 0, [['X', 'O', 'X'], ['O', 'X', ' '], ['X', 'O', 'X']]) == 10000
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: Player has no consecutive pieces, all opponents
        assert func5('X', 1, 1, [['O', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']]) == -1
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Player has 3 consecutive pieces diagonally, with a gap
        assert func5('X', 0, 0, [['X', 'O', ' '], [' ', 'X', ' '], ['X', ' ', 'O']]) == 4
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

failed_ratio = bullet_flat_test_cases()/10 # pragma: no cover

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