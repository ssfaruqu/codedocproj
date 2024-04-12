import math as math

#determines if string is a palindrome
'''
func1 initializes two index variables, left and right, to increment along string from the start and
decrement along string from the end. These increments and decrements are iterated simultaneously, using the 
left and right variables to check the characters at those indices for each iteration. If during any iteration
the characters don't match, string isn't a palindrome. If the iterations reach the point where right is 
less than left, string is a palindrome.

- keep track of increment and decrement using left and right
- if at any iteration string[left] != string string[right], string not palindrome
- if right < left, string is palindrome

Psuedocode:
left = start of string
right = end of string

while right >= left:
    if string[right] != string[left]: return False
    left++
    right--

return True

Input Parameters:
string -> a string to be checked for being a palindrome
Return Values:
Boolean True or False

Function Usage Example:
func1("racecar") -> True
func1("apple") -> False
'''
def func1(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# BFS search, returns list of nodes visited in order if goal found, else None
'''
func2 intializes the fringe list with just the start node, and the visited list as empty.
While the fringe isn't empty, the front node of the fringe will be popped of the fringe list
and appended to the visited list. A goal check is performed on the popped node; if it fails, 
its successors will be added to the back of the fringe if they aren't already on the fringe or in the 
visited list. If a goal is found, then return the visited list, else return None.

- fringe starts as [start] and visited is empty
- until the fringe is empty, we pop off front of fringe to check its succ
- if popped node is goal, we return visited, else we attempt to add succs to fringe
- return None if goal not found

Psuedocode:
fringe = [start]
visited = []

while fringe isn't empty:
    curr_node = fringe.pop()
    add curr_node to visited
    if goal check passes:
        return visited

    for each succ of curr_node:
        if succ not in visited or fringe:
            add succ to fringe

return None

Input Parameters:
start -> the inital Node object to start the BFS algorithm
goal -> the goal Node object to find
Return Values:
visted -> the list of nodes visited during BFS, in the order they are first discovered
None

Function Usage Example:
func2(A, Z) -> [A, B, F, Z]
func2(A, T) -> None
'''
def func2(start, goal):
    fringe = [start]
    visited = []

    while fringe:
        curr_node = fringe.pop(0)
        visited.append(curr_node)
        if curr_node == goal:
            return visited
        
        for child in curr_node.succesor:
            if child not in fringe and child not in visited:
                fringe.append(child)

    return None

# get Euclidean dist between 2 points
'''
func3 calculates the Euclidian distance between two points on a 2D plane. It performs this calculation
using the helper function euc_dist

- pass pos1 and pos2 to euc_dist and returns result

Psuedocode:
return euc_dist(pos1, pos2)

Input Parameters:
pos1 -> a list containing the x and y values of the first point
pos1 -> a list containing the x and y values of the second point
Return Values:
dist -> the Euclidian distance bewteen pos1 and pos2

Function Usage Example:
func3([0,0], [4,4]) -> 4
'''
def func3(pos1, pos2):
    dist = euc_dist(pos1, pos2)
    return dist

# sets the Map class' class variables based on the layout file
'''
func4 first uses layout_file to open the corresponding file and set the layout of the Map object. It reads in 
the first three lines to set the Map objects length, width, and enemy_types. It then enumerates through the 
rest of the lines to transfer the layout file to map_grid and original_layout. In each row, there is a check to 
see if there is a spawn point whose position needs to be noted. Once the enumeration is done, the file is closed.

- join abs_map_layouts_path and layout_file to get file path
- open layout file to set length, width, enemy_types, map_grid, and original_layout
- find spawn points while going through file
- close file when done

Psuedocode:
set layout
file path = abs_map_layouts_path + layout_file
open file
set length, width, and enemy types

iterate through rest of file to set map_grid and original_layout:
    if spawn point found:
        add position to spawn_points

close file

Input Parameters:
layout_file-> a string containing the name of the layout file being used to set the Map object
Return Values:
None

Function Usage Example:
Map_obj.func4("swamp")
'''
def func4(self, layout_file):
    self.setLayout(layout_file)
    path = os.path.join(abs_map_layouts_path, layout_file)
    f = open(path, "r")
    self.setLength(int(f.readline()))
    self.setWidth(int(f.readline()))
    self.enemy_types = f.readline().strip('\n').split(',')

    for i, line in enumerate(f):
        row = []
        for j, x in enumerate(line):
            if x != '\n':
                row.append(x)
                if x == '#':
                    self.spawn_points.append((i,j))
        self.map_grid.append(row)
        self.original_layout.append(row[:])
        
    f.close()

# get a heuristic score of a specific piece (given by row and col) on a given board state
'''
Given the board and a position on it, check what connections there are from that position.
A score is returned based on the number of consecutive pieces, as well as if that connection 
is cut off by an opponent's piece, or has a free spot. If a connect-4 is found, we return a max
score. Otherwise, the final score is the sum of all scores of chains found. If it's an opponent's 
connection, return negative value, else a positive one.

- set all scores to 1 first to represent the score a a one piece chain
- set the sign based on the player_number
- calculate the proper score for each chain
- if a connect-4 is found, immediately return sign*10000
- set score to sum of chain scores and return sign*score

Psuedocode:
score, uv_score, lh_score, rh_score = 1
set sign based on player_number

calculate uv_score:
    if connect-4 found: return sign*10000
calculate lh_score:
    if connect-4 found: return sign*10000
calculate rh_score:
    if connect-4 found, return sign*10000

score = uv_score + lh_score + rh_score
return sign*score

Input Parameters:
player_number -> an int used to identify which piece on the board is the player's
board -> a 2D array representing the game's board state
row -> the row number of the piece being checked
col -> the column number of the piece being checked
Return Values:
sign*score -> an int value representing the heuristic value of a given piece in a board state; 
              positive if the piece is the player's, negative if it's the opponent's

Function Usage Example:
func5(1, board, 3, 5) -> 12
func5(2, board, 4, 6) -> -10000
'''
def func5(player_number, board, row, col):
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

# Recursive function to double elements of an array
'''
func6 takes an array of ints and recurs along each half of it to create a new array whose elements are
the doubled values of the elements of the initial array.

- base case if len(n) == 1, returns singleton list of [n[0]*2]
- get middle index and use it to recur on first half of list
- then use middle index to recur upper half
- return new_n after recursion done

Psuedocode:
if len(n) == 1:
    return [n[0]*2]

new_n = []

new_n = new_n + func6(lower half of n)
new_n = new_n + func6(upper half of n)

return new_n

Input Parameters:
n -> an array of ints
Return Values:
new_n -> a new version of n where all elements are ints

Function Usage Example:
func6([8, 7, 0, 4]) -> [16, 14, 0, 8]
'''
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

# takes in a C++ test file, performs local value numbering, and prints out the resulting file
def func7(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    global_counter = 0
    H = {}
    var_number = {}
    to_initialize = []
    replaced = 0
    expression_list = get_expression_list(to_optimize)
    lvn_expression_list = []

    for expr in expression_list:
        lhs = expr[0]
        left_val = expr[2]
        op = expr[3]
        right_val = expr[4]

        lvn_left_val = ""
        lvn_right_val = ""
        lvn_rhs = ""

        if left_val not in var_number:
            lvn_left_val = left_val + str(global_counter)
            var_number[left_val] = str(global_counter)
            to_initialize.append(lvn_left_val) 
            global_counter += 1
        else:
            lvn_left_val = left_val + var_number[left_val]

        if right_val not in var_number:
            lvn_right_val = right_val + str(global_counter)
            var_number[right_val] = str(global_counter)
            to_initialize.append(lvn_right_val)  
            global_counter += 1
        else:
            lvn_right_val = right_val + var_number[right_val]

        if op == "+" and (lvn_right_val < lvn_left_val):
            lvn_rhs = lvn_right_val + " " + op + " " + lvn_left_val
        else:
            lvn_rhs = lvn_left_val + " " + op + " " + lvn_right_val

        lvn_lhs = lhs + str(global_counter)
        var_number[lhs] = str(global_counter)
        global_counter += 1

        if lvn_rhs in H:
            opt_var = H[lvn_rhs]
            replaced += 1
            lvn_rhs = opt_var

        else:
            H[lvn_rhs] = lvn_lhs

        lvn_expr = lvn_lhs + " = " + lvn_rhs
        lvn_expression_list.append(lvn_expr)

    print(pre)

    for var in to_initialize:
        print("    double " + var + " = " + var[0] + ";")

    for expr in lvn_expression_list:
        print("    double " + expr + ";")

    for key, val in var_number.items():
        print("    " + key + " = " + key + val + ";")

    print(post)

    print("// replaced: " + str(replaced))

# returns the set of live variables in each node of a given CFG ()
"""
Computes the LiveOut set using the default PyCFG traversal on a non-reversed CFG
"""
def func8(CFG, UEVar, VarKill, VarDomain):
    LiveOut = {}
    num_loops = 0

    for i in range(len(CFG)):
        LiveOut[CFG.get_node(i)] = set({})

    changed = True
    while changed:
        num_loops += 1
        changed = False
        for i in CFG:
            LiveOut_curr = LiveOut[CFG.get_node(i)].copy()
            LiveOut_new = set({})
            succ = get_node_successors(CFG, CFG.get_node(i))

            for s in succ:
                UEVar_s = UEVar[s]
                LiveOut_s = LiveOut[s]
                VarKill_s = VarKill[s]

                VarKillCmpl_s = {var for var in VarDomain if var not in VarKill_s}
                y = LiveOut_s.intersection(VarKillCmpl_s)
                x = UEVar_s.union(y)
                LiveOut_new = LiveOut_new.union(x)

            if LiveOut_curr != LiveOut_new:
                LiveOut[CFG.get_node(i)] = LiveOut_new
                changed = True

    return LiveOut

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

# encodes string a using string b and operation selection c
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
        
if __name__ == "__main__":
    #print(func11([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False))
    print(func10("򈀱", "a", 0))