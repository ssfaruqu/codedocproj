import coverage # pragma: no cover

# Create a coverage object
cov = coverage.Coverage(data_suffix=True) # pragma: no cover

# Start measuring coverage
cov.start() # pragma: no cover

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

#BULLET STRUC TESTS
def bullet_struc_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Head in the middle, food in the top-right quadrant
        head_x, head_y = 5, 5
        food_x, food_y = 8, 2
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 0, 1, -1, 0, 0, 0, 0]

        count += 1 # Test 2: Head in the top-left corner, food in the bottom-right quadrant
        head_x, head_y = 0, 0
        food_x, food_y = 8, 8
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [1, 1, 1, 1, 0, 0, 0, 0]

        count += 1 # Test 3: Head in the middle, food directly below
        head_x, head_y = 5, 5
        food_x, food_y = 5, 8
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 1, 0, -1, 0, 0, 0, 0]

        count += 1 # Test 4: Head in the middle, food directly above
        head_x, head_y = 5, 5
        food_x, food_y = 5, 2
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 1, 0, 1, 0, 0, 0, 0]

        count += 1 # Test 5: Head in the middle, food directly to the left
        head_x, head_y = 5, 5
        food_x, food_y = 2, 5
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [1, 0, 1, 0, 0, 0, 0, 0]

        count += 1 # Test 6: Head in the middle, food directly to the right
        head_x, head_y = 5, 5
        food_x, food_y = 8, 5
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = []
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [1, 0, -1, 0, 0, 0, 0, 0]

        count += 1 # Test 7: Head surrounded by body segments
        head_x, head_y = 5, 5
        food_x, food_y = 8, 2
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = [(5, 4), (5, 6), (4, 5), (6, 5)]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 0, 1, -1, 0, 0, 0, 0]

        count += 1 # Test 8: Head in the middle, food directly below, surrounded by body segments
        head_x, head_y = 5, 5
        food_x, food_y = 5, 8
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = [(5, 4), (5, 6), (4, 5), (6, 5)]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 1, 0, -1, 1, 0, 1, 0]

        count += 1 # Test 9: Head in the middle, food directly above, surrounded by body segments
        head_x, head_y = 5, 5
        food_x, food_y = 5, 2
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = [(5, 4), (5, 6), (4, 5), (6, 5)]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [0, 1, 0, 1, 1, 0, 1, 0]

        count += 1 # Test 10: Head in the middle, food directly to the left, surrounded by body segments
        head_x, head_y = 5, 5
        food_x, food_y = 2, 5
        BOARD_LIMIT_MIN, BOARD_LIMIT_MAX = 0, 10
        GRID_SIZE = 1
        body = [(5, 4), (5, 6), (4, 5), (6, 5)]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == [1, 0, 1, 0, 0, 1, 0, 0]

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