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

#PARA FLAT TESTS
def para_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Empty board, no alignment
        assert func5(1, [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]], 1, 1) == 0
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Horizontal alignment of four pieces owned by player 1
        assert func5(1, [[0, 0, 0],
                        [1, 1, 1],
                        [0, 0, 0]], 1, 1) > 0
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Vertical alignment of four pieces owned by player 2
        assert func5(2, [[0, 2, 0],
                        [0, 2, 0],
                        [0, 2, 0]], 1, 1) < 0
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Diagonal alignment of four pieces owned by player 1
        assert func5(1, [[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]], 1, 1) > 0
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Horizontal and vertical alignments owned by player 2
        assert func5(2, [[2, 0, 0],
                        [2, 0, 0],
                        [2, 0, 0]], 1, 1) < 0
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Diagonal alignment of four pieces owned by player 2
        assert func5(2, [[0, 0, 2],
                        [0, 2, 0],
                        [2, 0, 0]], 1, 1) < 0
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Mixed alignments owned by player 1
        assert func5(1, [[1, 0, 0],
                        [1, 1, 0],
                        [1, 0, 1]], 1, 1) > 0
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Mixed alignments owned by player 2
        assert func5(2, [[2, 0, 0],
                        [2, 2, 0],
                        [2, 0, 2]], 1, 1) < 0
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: Four-piece horizontal alignment owned by player 1
        assert func5(1, [[1, 1, 1],
                        [0, 0, 0],
                        [0, 0, 0]], 0, 0) > 1000
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Four-piece diagonal alignment owned by player 2
        assert func5(2, [[0, 0, 2],
                        [0, 2, 0],
                        [2, 0, 0]], 0, 0) < -1000
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

failed_ratio = para_flat_test_cases()/10 # pragma: no cover

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