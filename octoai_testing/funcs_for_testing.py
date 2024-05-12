def func1(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
# test function 2
def func2(arr, target):
    if len(arr) == 0:
        return None
    
    m = (len(arr)-1)//2
    val = arr[m]

    if type(target) == int and val == target:
        return target
    
    if type(target) == int and target%2 == 0:
        if val > target:
            return func2(arr[m+1:], target)
        else:
            return func2(arr[0:m], target)
    elif type(target) == int and target%2 == 1:
        if val < target:
            return func2(arr[m+1:], target)
        else:
            return func2(arr[0:m], target)
    elif type(target) == str:
        return "No strings allowed"
    
    return -1
# test function 3
def func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    def incrHealth(health, magnitude):
        return health + magnitude
    def scale_attack(multiplier, magnitude):
        return multiplier * len(attack_type) * magnitude
    
    if curr_health <= 0 or len(attack_type) == 0:
        return -1
    
    scaled_attack_mag = 0
    match entity_type:
        case 0:
            for type in attack_type:
                if type == 0:
                    scaled_attack_mag += scale_attack(2, attack_mag)
                elif type == 1:
                    scaled_attack_mag += scale_attack(0.25, attack_mag)
                elif type == 2:
                    scaled_attack_mag += scale_attack(1, -1*attack_mag)
                else:
                    scaled_attack_mag += scale_attack(1, attack_mag)
        case 1:
             for type in attack_type:
                if type == 3:
                    scaled_attack_mag += scale_attack(2, attack_mag)
                elif type == 4:
                    scaled_attack_mag += 0
                elif type == 5:
                    scaled_attack_mag += scale_attack(1, attack_mag)
                else:
                    scaled_attack_mag += scale_attack(0.1, attack_mag)
        case 2:
             for type in attack_type:
                if type == 1:
                    scaled_attack_mag += scale_attack(2, attack_mag)
                elif type == 0 or type == 5:
                    scaled_attack_mag += 0
                elif type == 4:
                    scaled_attack_mag += scale_attack(1, attack_mag)
                else:
                    scaled_attack_mag += scale_attack(0.1, attack_mag)
    
    new_health = incrHealth(curr_health, scaled_attack_mag)

    if new_health <= 0:
        return -1
    elif new_health > tot_health:
        return tot_health
    else:
        return new_health
# test function 4
def func4(pt1, pt2, pt3):
    euc_dist = math.sqrt(math.pow(pt1[0] - pt2[0], 2) + math.pow(pt1[1] - pt2[0], 2))
    man_dist = abs(pt2[0] - pt3[0]) + abs(pt2[1] - pt3[1])

    if euc_dist > 0.75*man_dist:
        return math.sqrt(math.pow(pt2[0] - pt3[0], 2) + math.pow(pt2[1] - pt3[0], 2))
    elif 0.75*man_dist < euc_dist:
        man_dist = abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])
    else:
        return euc_dist + man_dist
# test function 5
def func5(player_number, row, col, board):
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
# test function 6
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
# test function 7
def func7(num):
    digits = []
    temp = num

    while temp > 0:
        digits.append(temp % 10)
        temp = temp // 10

    digits.reverse()
    rev_num = 0
    for i in range(0, len(digits)):
        rev_num += math.pow(10, i)*digits[i]
    rev_bigger = rev_num > num
    
    if len(digits) > 1:
        digits.reverse()
        mid = (len(digits)-1)//2
        digits = digits[mid:] + digits[0:mid]
        
        switch_num = 0
        for i in range(0, len(digits)):
            switch_num += math.pow(10, i)*digits[i]
        switch_bigger = switch_num > num

        return (int(rev_num), rev_bigger, int(switch_num), switch_bigger)
    
    return (int(rev_num), rev_bigger)
# test function 8
def func8(num):
    if type(num) == int or num < 0:
        return None

    upper = int(num)
    upper_digs = 0
    while upper % 10 > 0:
        upper_digs += 1
        upper = upper // 10

    lower = num - upper
    lower = round(lower, 5)
    lower_digs = 0
    while lower % 1 > 0:
        lower_digs += 1
        lower *= 10
        lower = round(lower, 5)
    lower = int(lower)
   
    if upper_digs > lower_digs:
        return True
    elif upper_digs > lower_digs:
        return False
    else:
        return upper > lower
# test function 9
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
# test function 10
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
# test function 11
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
# test function 12
def func12(results):
    fail_ratios = []

    stats = [x for x in results if '_hypothesis_stats' in x]

    for s in stats:
        passing = re.findall('[0-9]*[0-9]*[0-9] passing', s['_hypothesis_stats'])
        passing = [re.findall('[0-9]*[0-9]*[0-9]', x)[0] for x in passing]
        passing = [int(x) for x in passing]
        passing = sum(passing)

        failing = re.findall('[0-9]*[0-9]*[0-9] failing', s['_hypothesis_stats'])
        failing = [re.findall('[0-9]*[0-9]*[0-9]', x)[0] for x in failing]
        failing = [int(x) for x in failing]
        failing = sum(failing)

        fail_ratios.append(failing/(passing+failing))

    if fail_ratios == []:
        stats = [x for x in results if 'outcome' in x]
        for s in stats:
            if s['outcome'] == 'failed':
                return [1.0]*5
            else:
                fail_ratios = [0.0]*5
    
    return fail_ratios