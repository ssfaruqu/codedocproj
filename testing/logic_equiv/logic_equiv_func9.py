import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

body_len = np.random.randint(1, 10)
rand_body = np.random.choice([40, 80, 120, 160, 200, 240], size=[body_len, 2])
rand_body.tolist()
rand_body = [list(b) for b in rand_body]
print(rand_body)

def test_para_flat_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y)
    flat = para_flat_func9(head_x, head_y, food_x, food_y)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

def test_para_struc_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y)
    struc =  para_struc_func9(head_x, head_y, food_x, food_y)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

def test_bullet_flat_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y)
    flat = bullet_flat_func9(head_x, head_y, food_x, food_y)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

def test_bullet_struc_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y)
    struc =  bullet_struc_func9(head_x, head_y, food_x, food_y)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

def test_psuedo_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y)
    psuedo = psuedo_func9(head_x, head_y, food_x, food_y)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo

def orig_func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN=40, BOARD_LIMIT_MAX=240, GRID_SIZE=40, body=rand_body):
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

# THE FUNCTION PARAMETERS FOR para_flat ARE COMPLETELY DIFFERENT AND DONT INCLUDE BOARD LIMITS
# ALSO, RETURN VALUE IS WRONG
def para_flat_func9(snake_head, food, body=rand_body, grid_size=40):
    """
    Computes various states based on the positions of the snake's head, food, board limits,
    grid size, and snake's body.

    Args:
    - snake_head (tuple): The position of the snake's head (x, y).
    - food (tuple): The position of the food (x, y).
    - body (list of tuples): The positions of the snake's body segments [(x1, y1), (x2, y2), ...].
    - grid_size (tuple): The size of the game grid (width, height).

    Returns:
    - list of ints: A list representing different aspects of the game environment.
    """
    # Extract positions of head, food, and body
    head_x, head_y = snake_head
    food_x, food_y = food

    # Determine relative positions of head to board limits and food in terms of X and Y directions
    rel_pos_x = 1 if head_x < food_x else (-1 if head_x > food_x else 0)
    rel_pos_y = 1 if head_y < food_y else (-1 if head_y > food_y else 0)

    # Check adjacency of head to the snake's body in top, bottom, left, and right directions
    adjacent_top = (head_x, head_y - 1) in body
    adjacent_bottom = (head_x, head_y + 1) in body
    adjacent_left = (head_x - 1, head_y) in body
    adjacent_right = (head_x + 1, head_y) in body

    # Create a list of integers representing different aspects of the game environment
    states = [rel_pos_x, rel_pos_y, int(adjacent_top), int(adjacent_bottom), int(adjacent_left), int(adjacent_right)]

    return states

def para_struc_func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN=40, BOARD_LIMIT_MAX=240, GRID_SIZE=40, body=rand_body):
    # Calculate adjacency to board limits
    ADJ_WALL_X_STATE = 0 if head_x == BOARD_LIMIT_MIN else (1 if head_x == BOARD_LIMIT_MAX else 2)
    ADJ_WALL_Y_STATE = 0 if head_y == BOARD_LIMIT_MIN else (1 if head_y == BOARD_LIMIT_MAX else 2)

    # Calculate direction of food relative to the head
    FOOD_DIR_X = 0 if food_x < head_x else (1 if food_x > head_x else 2)
    FOOD_DIR_Y = 0 if food_y < head_y else (1 if food_y > head_y else 2)

    # Calculate adjacency to snake's body
    ADJ_BODY_TOP_STATE = (head_x, head_y - GRID_SIZE) in body
    ADJ_BODY_BOTTOM_STATE = (head_x, head_y + GRID_SIZE) in body
    ADJ_BODY_LEFT_STATE = (head_x - GRID_SIZE, head_y) in body
    ADJ_BODY_RIGHT_STATE = (head_x + GRID_SIZE, head_y) in body

    # Return the list containing the calculated states
    return [ADJ_WALL_X_STATE, ADJ_WALL_Y_STATE, FOOD_DIR_X, FOOD_DIR_Y,
            ADJ_BODY_TOP_STATE, ADJ_BODY_BOTTOM_STATE, ADJ_BODY_LEFT_STATE, ADJ_BODY_RIGHT_STATE]


def bullet_flat_func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN=40, BOARD_LIMIT_MAX=240, GRID_SIZE=40, body=rand_body):
    """
    Determine the state of adjacent walls, food direction, and adjacency of body segments.

    Args:
    - head_x: X-coordinate of the head.
    - head_y: Y-coordinate of the head.
    - food_x: X-coordinate of the food.
    - food_y: Y-coordinate of the food.
    - BOARD_LIMIT_MIN: Minimum board limit.
    - BOARD_LIMIT_MAX: Maximum board limit.
    - GRID_SIZE: Size of the grid.
    - body: List representing the body segments.

    Returns:
    - List containing the states of adjacent walls, food direction, and adjacency of body segments in all directions.
    """
    # Initialize a list to store the current position of the head
    head_pos = [head_x, head_y]

    # Determine the state of adjacent walls along the x-axis
    ADJ_WALL_X_STATE = [head_x == BOARD_LIMIT_MIN, head_x == BOARD_LIMIT_MAX]

    # Determine the state of adjacent walls along the y-axis
    ADJ_WALL_Y_STATE = [head_y == BOARD_LIMIT_MIN, head_y == BOARD_LIMIT_MAX]

    # Determine the direction of the food along the x-axis
    FOOD_DIR_X = food_x - head_x

    # Determine the direction of the food along the y-axis
    FOOD_DIR_Y = food_y - head_y

    # Initialize variables to represent the adjacency of the body segments in each direction
    LEFT_ADJ, RIGHT_ADJ, UP_ADJ, DOWN_ADJ = False, False, False, False

    # Iterate over each body segment to determine adjacency to the head in each direction
    for segment in body:
        if segment[0] == head_x - 1 and segment[1] == head_y:
            LEFT_ADJ = True
        elif segment[0] == head_x + 1 and segment[1] == head_y:
            RIGHT_ADJ = True
        elif segment[0] == head_x and segment[1] == head_y - 1:
            UP_ADJ = True
        elif segment[0] == head_x and segment[1] == head_y + 1:
            DOWN_ADJ = True

    # Return a list containing the states of adjacent walls, food direction, and adjacency of body segments in all directions
    return [ADJ_WALL_X_STATE, ADJ_WALL_Y_STATE, FOOD_DIR_X, FOOD_DIR_Y, LEFT_ADJ, RIGHT_ADJ, UP_ADJ, DOWN_ADJ]

def bullet_struc_func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN=40, BOARD_LIMIT_MAX=240, GRID_SIZE=40, body=rand_body):
    # 1. Calculate the current position of the head (head_pos).
    head_pos = (head_x, head_y)

    # 2. Determine the state of adjacent walls along the x-axis (ADJ_WALL_X_STATE) based on the head position relative to the board limits.
    ADJ_WALL_X_STATE = "Left" if head_x == BOARD_LIMIT_MIN else "Right" if head_x == BOARD_LIMIT_MAX else "Neither"

    # 3. Determine the state of adjacent walls along the y-axis (ADJ_WALL_Y_STATE) based on the head position relative to the board limits.
    ADJ_WALL_Y_STATE = "Top" if head_y == BOARD_LIMIT_MIN else "Bottom" if head_y == BOARD_LIMIT_MAX else "Neither"

    # 4. Determine the direction of the food along the x-axis (FOOD_DIR_X) based on the head position relative to the food position.
    FOOD_DIR_X = "Left" if food_x < head_x else "Right" if food_x > head_x else "Same"

    # 5. Determine the direction of the food along the y-axis (FOOD_DIR_Y) based on the head position relative to the food position.
    FOOD_DIR_Y = "Up" if food_y < head_y else "Down" if food_y > head_y else "Same"

    # 6. Initialize variables to represent the adjacency of the body segments in each direction.
    ADJ_BODY_TOP_STATE = False
    ADJ_BODY_BOTTOM_STATE = False
    ADJ_BODY_LEFT_STATE = False
    ADJ_BODY_RIGHT_STATE = False

    # 7. Iterate over each body segment to determine adjacency to the head in each direction.
    for segment in body:
        seg_x, seg_y = segment
        if seg_x == head_x:
            if seg_y == head_y + GRID_SIZE:
                ADJ_BODY_BOTTOM_STATE = True
            elif seg_y == head_y - GRID_SIZE:
                ADJ_BODY_TOP_STATE = True
        elif seg_y == head_y:
            if seg_x == head_x + GRID_SIZE:
                ADJ_BODY_RIGHT_STATE = True
            elif seg_x == head_x - GRID_SIZE:
                ADJ_BODY_LEFT_STATE = True

    # 8. Return a list containing the states of adjacent walls, food direction, and adjacency of body segments in all directions.
    return [ADJ_WALL_X_STATE, ADJ_WALL_Y_STATE, FOOD_DIR_X, FOOD_DIR_Y, ADJ_BODY_TOP_STATE, ADJ_BODY_BOTTOM_STATE, ADJ_BODY_LEFT_STATE, ADJ_BODY_RIGHT_STATE]

def psuedo_func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN=40, BOARD_LIMIT_MAX=240, GRID_SIZE=40, body=rand_body):
    # Initialize head_pos as list containing head_x and head_y
    head_pos = [head_x, head_y]

    # Determine ADJ_WALL_X_STATE based on head_x position
    if head_x == BOARD_LIMIT_MIN:
        ADJ_WALL_X_STATE = 0
    elif head_x == BOARD_LIMIT_MAX:
        ADJ_WALL_X_STATE = 1
    else:
        ADJ_WALL_X_STATE = 2

    # Determine ADJ_WALL_Y_STATE based on head_y position
    if head_y == BOARD_LIMIT_MIN:
        ADJ_WALL_Y_STATE = 0
    elif head_y == BOARD_LIMIT_MAX:
        ADJ_WALL_Y_STATE = 1
    else:
        ADJ_WALL_Y_STATE = 2

    # Determine FOOD_DIR_X based on relative position of head_x and food_x
    if head_x > food_x:
        FOOD_DIR_X = 0
    elif head_x < food_x:
        FOOD_DIR_X = 1
    else:
        FOOD_DIR_X = 2

    # Determine FOOD_DIR_Y based on relative position of head_y and food_y
    if head_y > food_y:
        FOOD_DIR_Y = 0
    elif head_y < food_y:
        FOOD_DIR_Y = 1
    else:
        FOOD_DIR_Y = 2

    # Initialize ADJ_BODY_TOP_STATE, ADJ_BODY_BOTTOM_STATE, ADJ_BODY_LEFT_STATE, and ADJ_BODY_RIGHT_STATE to 0
    ADJ_BODY_TOP_STATE = 0
    ADJ_BODY_BOTTOM_STATE = 0
    ADJ_BODY_LEFT_STATE = 0
    ADJ_BODY_RIGHT_STATE = 0

    # Iterate over each position in body
    for pos in body:
        # Check if each position is adjacent to head_pos in each direction
        if pos[0] == head_pos[0] and pos[1] == head_pos[1] + 1:
            ADJ_BODY_TOP_STATE = 1
        elif pos[0] == head_pos[0] and pos[1] == head_pos[1] - 1:
            ADJ_BODY_BOTTOM_STATE = 1
        elif pos[0] == head_pos[0] + 1 and pos[1] == head_pos[1]:
            ADJ_BODY_LEFT_STATE = 1
        elif pos[0] == head_pos[0] - 1 and pos[1] == head_pos[1]:
            ADJ_BODY_RIGHT_STATE = 1

    # Return list containing the computed states
    return [
        ADJ_WALL_X_STATE,
        ADJ_WALL_Y_STATE,
        FOOD_DIR_X,
        FOOD_DIR_Y,
        ADJ_BODY_TOP_STATE,
        ADJ_BODY_BOTTOM_STATE,
        ADJ_BODY_LEFT_STATE,
        ADJ_BODY_RIGHT_STATE
    ]

def try_test(test, test_fail_string, test_pass_string):
    try:
        choices = [40, 80, 120, 160, 200, 240]
        for hx, hy, fx, fy in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
            test(hx, hy, fx, fy)
        print(test_pass_string)
        print("")
    except Exception as e:
        print(test_fail_string)
        print(repr(e))
        print("")

print("----- func9 LOGIC EQUIV TESTING -------")
try_test(test_para_flat_func9, "PARA FLAT FAIL", "PARA FLAT PASS")
try_test(test_para_struc_func9, "PARA STRUC FAIL", "PARA STRUC PASS")
try_test(test_bullet_flat_func9, "BULLET FLAT FAIL", "BULLET FLAT PASS")
try_test(test_bullet_struc_func9, "BULLET STRUC FAIL", "BULLET STRUC PASS")
try_test(test_psuedo_func9, "PSUEDO FAIL", "PSUEDO PASS")
