def func5(player_number, row, col, board):
    score = 1 
    uv_score, lh_score, rh_score = 1, 1, 1
        
    our_piece = board[row][col]
    if int(our_piece) != player_number: 
        sign = -1
    else: sign = 1

    max_col = len(board[0])
    max_row = len(board)
        
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
# test function 2
def func6(n):
    if len(n) == 0:
        return []
    elif len(n) == 1:
        return [n[0]*2]
    
    new_n = []
    i = math.floor(len(n)/2)

    new_n = new_n + func6(n[0:i])
    new_n = new_n + func6(n[i:])

    return new_n
# test function 3
def func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body):
        head_pos = [head_x, head_y]

        if head_pos[0] == BOARD_LIMIT_MIN: 
            ADJ_WALL_X_STATE = 0
        elif head_pos[0] == BOARD_LIMIT_MAX: 
            ADJ_WALL_X_STATE = 1
        else:                                      
            ADJ_WALL_X_STATE = 2

        if head_pos[1] == BOARD_LIMIT_MIN:  
            ADJ_WALL_Y_STATE = 0
        elif head_pos[1] == BOARD_LIMIT_MAX: 
            ADJ_WALL_Y_STATE = 1
        else:                                      
            ADJ_WALL_Y_STATE = 2
                
        if head_pos[0] > food_x:  
            FOOD_DIR_X = 0
        elif head_pos[0] < food_x: 
            FOOD_DIR_X = 1
        else:                      
            FOOD_DIR_X = 2

        if head_pos[1] > food_y:  
            FOOD_DIR_Y = 0
        elif head_pos[1] < food_y: 
            FOOD_DIR_Y = 1
        else:                      
            FOOD_DIR_Y = 2

        ADJ_BODY_TOP_STATE = 0 
        ADJ_BODY_BOTTOM_STATE = 0
        ADJ_BODY_LEFT_STATE = 0
        ADJ_BODY_RIGHT_STATE = 0
        for x in body:
            if x == [head_pos[0], head_pos[1] + GRID_SIZE]:
                ADJ_BODY_TOP_STATE = 1
            elif x == [head_pos[0], head_pos[1] - GRID_SIZE]:
                ADJ_BODY_BOTTOM_STATE = 1
            elif x == [head_pos[0] + GRID_SIZE, head_pos[1]]:
                ADJ_BODY_RIGHT_STATE = 1
            elif x == [head_pos[0] - GRID_SIZE, head_pos[1]]:
                ADJ_BODY_LEFT_STATE = 1
                
        return [ADJ_WALL_X_STATE, 
            ADJ_WALL_Y_STATE,
            FOOD_DIR_X,
            FOOD_DIR_Y,
            ADJ_BODY_TOP_STATE,
            ADJ_BODY_BOTTOM_STATE,
            ADJ_BODY_LEFT_STATE,
            ADJ_BODY_RIGHT_STATE]
# test function 4
def func10(a, b, c):
    char_vals = [ord(c) for c in a]

    match c:
        case 0:
            char_vals = [val << 1 for val in char_vals]
            b = b + 'a'
        case 1:
            char_vals = [val >> 1 for val in char_vals]
            b = 'b' + b
        case 2:
            char_vals = [val + 5 for val in char_vals]
            b = b + 'c'
        case _:
            char_vals = [val + 1 for val in char_vals]
            b = 'd' + b

    if len(a) > len(b):
        length = len(b)
    else:
        length = len(a)

    for i in range(length):
        b_val = ord(b[i])
                    
        if char_vals[i] > b_val:
            char_vals[i] -= b_val
        else:
            char_vals[i] += b_val

    ret = ""
    for x in char_vals:
        ret = ret + chr(x)

    if c > 0:
        repeat = int(abs(len(b)*len(b) - c*c)/(len(a)+1))
        ret = ret * repeat
    
    return ret
# test function 5
def func11(reverse, grid):
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