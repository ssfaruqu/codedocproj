import hypothesis
import numpy as np
from hypothesis import given, strategies as st

#-------------------- BOARD SCORING TEST ---------------------------------------------------------------->
rand_board = np.random.choice([1, 2], size=[7, 7], replace=True)
print(rand_board)

#FAIL
@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_para_flat_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col)
    flat = para_flat_func5(player_number, row, col)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_para_struc_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col)
    struc =  para_struc_func5(player_number, row, col)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_bullet_flat_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col)
    flat = bullet_flat_func5(player_number, row, col)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_bullet_struc_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col)
    struc =  bullet_struc_func5(player_number, row, col)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_psuedo_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col)
    psuedo = psuedo_func5(player_number, row, col)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo

def orig_func5(player_number, row, col, board= rand_board):
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

def para_flat_func5(player_number, row, col, board= rand_board):
    """
    Calculates a score based on the position of a player's piece on a game board.

    Args:
    - player_number (int): The identification number of the player.
    - board (list of lists): The game board configuration.
    - row (int): The row index of the player's piece.
    - col (int): The column index of the player's piece.

    Returns:
    - int: The calculated score based on the player's piece position.
    """
    score = 0

    # Function to calculate score in a specific direction
    def calculate_score_in_direction(dx, dy):
        nonlocal score
        x, y = row, col
        consecutive_count = 0
        distance = 0

        # Check in the specified direction until reaching board limits or an opponent's piece
        while 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == player_number:
            consecutive_count += 1
            distance += 1
            x += dx
            y += dy

        # Reverse direction and check again for opponent's pieces
        x, y = row - dx, col - dy
        while 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == player_number:
            consecutive_count += 1
            distance += 1
            x -= dx
            y -= dy

        # Adjust score based on the number of consecutive pieces and their alignment
        if consecutive_count >= 4:
            score += 1000  # A high score for a win condition
        elif consecutive_count == 3 and distance == 3:
            score += 100  # High score for three consecutive pieces with no gaps
        elif consecutive_count == 2 and distance == 2:
            score += 10  # Moderate score for two consecutive pieces with no gaps
        elif consecutive_count == 1 and distance == 1:
            score += 1  # Low score for a single piece

    # Calculate scores in three directions: vertically, horizontally to the left, and horizontally to the right
    calculate_score_in_direction(0, 1)  # Vertical (upward)
    calculate_score_in_direction(-1, -1)  # Horizontal (to the left)
    calculate_score_in_direction(-1, 1)  # Horizontal (to the right)

    return score * player_number  # Adjust score based on player's identity

    
def para_struc_func5(player_number, row, col, board= rand_board):
    def check_direction(dx, dy):
        count = 0
        # Check for consecutive pieces in the specified direction
        for i in range(1, 5):
            new_row = row + i * dx
            new_col = col + i * dy
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == player_number:
                count += 1
            else:
                break
        # Check for consecutive pieces in the opposite direction
        for i in range(1, 5):
            new_row = row - i * dx
            new_col = col - i * dy
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == player_number:
                count += 1
            else:
                break
        return count

    # Calculate scores for vertical, horizontal, and diagonal alignments
    uv_score = check_direction(-1, 0)
    lh_score = check_direction(0, -1) + check_direction(0, 1)
    rh_score = check_direction(-1, -1) + check_direction(1, 1) + check_direction(-1, 1) + check_direction(1, -1)

    # Calculate the overall alignment score
    overall_score = uv_score + lh_score + rh_score

    return overall_score

def postpre_func5(player_number, row, col, board= rand_board):
    def calculate_score(direction):
        count = 0
        opponent_count = 0
        consecutive_player = 0
        consecutive_opponent = 0

        for i in range(-3, 4):
            r = row + i * direction[0]
            c = col + i * direction[1]

            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == player_number:
                    consecutive_player += 1
                    consecutive_opponent = 0
                elif board[r][c] != 0:
                    consecutive_opponent += 1
                    consecutive_player = 0
                else:
                    consecutive_opponent = 0
                    consecutive_player = 0

                if consecutive_player == 4:
                    return 1000
                elif consecutive_opponent == 4:
                    return -1000

                if consecutive_player > 0:
                    count += consecutive_player
                if consecutive_opponent > 0:
                    opponent_count += consecutive_opponent

        if count >= 4:
            return count * 10
        elif opponent_count >= 4:
            return -opponent_count * 10
        return 0

    uv_score = calculate_score((-1, 0)) + calculate_score((1, 0))
    lh_score = calculate_score((0, -1)) + calculate_score((0, 1))
    rh_score = calculate_score((-1, -1)) + calculate_score((1, 1))
    lh_score = max(lh_score, rh_score)
    score = max(uv_score, lh_score)

    return score

def bullet_flat_func5(player_number, row, col, board= rand_board):
    # Initialize scores
    score = uv_score = lh_score = rh_score = 1
    
    # Retrieve our_piece
    our_piece = board[row][col]
    
    # Determine sign
    sign = 1 if our_piece == player_number else -1
    
    # Calculate max_col and max_row
    max_col = len(board[0]) - 1
    max_row = len(board) - 1
    
    # Iterate over directions
    for direction in range(1, 4):
        # Initialize variables for the current direction
        consecutive_count = 1
        i = row
        j = col
        
        # Vertical direction
        if direction == 1:
            i -= 1
        # Left horizontal direction
        elif direction == 2:
            j -= 1
        # Right horizontal direction
        elif direction == 3:
            j += 1
        
        # Continue searching until consecutive pieces are found or maximum limit reached
        while 0 <= i <= max_row and 0 <= j <= max_col:
            if board[i][j] == our_piece:
                consecutive_count += 1
                if consecutive_count >= 3:
                    score *= 10000 * sign
                    return score
            elif board[i][j] != our_piece:
                score *= consecutive_count
                break
            else:
                consecutive_count = 1
            
            # Update coordinates based on direction
            if direction == 1:
                i -= 1
            elif direction == 2:
                j -= 1
            elif direction == 3:
                j += 1
        
    # Return final score
    return score * sign

def bullet_struc_func5(player_number, row, col, board= rand_board):
    score = uv_score = lh_score = rh_score = 1

    our_piece = board[row][col]
    sign = 1 if our_piece == player_number else -1

    max_col = len(board[0]) - 1
    max_row = len(board) - 1

    for direction in range(1, 4):
        # Vertical direction
        if direction == 1:
            for i in range(1, 4):
                if row + i > max_row:
                    break
                if board[row + i][col] == our_piece:
                    uv_score *= 2
                    if i == 3:
                        return 10000 * sign
                elif board[row + i][col] == 0:
                    break
                else:
                    uv_score = 0
                    break
        # Left horizontal direction
        elif direction == 2:
            for i in range(1, 4):
                if col - i < 0:
                    break
                if board[row][col - i] == our_piece:
                    lh_score *= 2
                    if i == 3:
                        return 10000 * sign
                elif board[row][col - i] == 0:
                    break
                else:
                    lh_score = 0
                    break
        # Right horizontal direction
        else:
            for i in range(1, 4):
                if col + i > max_col:
                    break
                if board[row][col + i] == our_piece:
                    rh_score *= 2
                    if i == 3:
                        return 10000 * sign
                elif board[row][col + i] == 0:
                    break
                else:
                    rh_score = 0
                    break

    total_score = uv_score + lh_score + rh_score
    return total_score * sign


def psuedo_func5(player_number, row, col, board= rand_board):
    score = 1
    uv_score = 1
    lh_score = 1
    rh_score = 1
    
    our_piece = board[row][col]
    
    sign = 1 if our_piece == player_number else -1
    
    max_col = len(board[0]) - 1
    max_row = len(board) - 1
    
    for i in range(1, 4):
        if row + i > max_row:
            break
        
        if board[row+i][col] == our_piece:
            if i == 3:
                return sign * 10000
            else:
                uv_score *= 2
        elif board[row+i][col] == 0:
            break
        else:
            uv_score = 0
            break
    
    for i in range(1, 4):
        if col - i < 0:
            break
        
        if board[row][col-i] == our_piece:
            if i == 3:
                return sign * 10000
            else:
                lh_score *= 2
        elif board[row][col-i] == 0:
            break
        else:
            lh_score = 0
            break
    
    for i in range(1, 4):
        if col + i > max_col:
            break
        
        if board[row][col+i] == our_piece:
            if i == 3:
                return sign * 10000
            else:
                rh_score *= 2
        elif board[row][col+i] == 0:
            break
        else:
            rh_score = 0
            break
    
    score = uv_score + lh_score + rh_score
    
    return sign * score

# EXECUTE TEST
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

print("----- func5 LOGIC EQUIV TESTING -------")
pass_arr = [0,0,0,0,0]
pass_arr[0] = try_test(test_para_flat_func5, "PARA FLAT FAIL", "PARA FLAT PASS")
pass_arr[1] = try_test(test_para_struc_func5, "PARA STRUC FAIL", "PARA STRUC PASS")
pass_arr[2] = try_test(test_bullet_flat_func5, "BULLET FLAT FAIL", "BULLET FLAT PASS")
pass_arr[3] = try_test(test_bullet_struc_func5, "BULLET STRUC FAIL", "BULLET STRUC PASS")
pass_arr[4] = try_test(test_psuedo_func5, "PSUEDO FAIL", "PSUEDO PASS")