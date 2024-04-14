import coverage # pragma: no cover

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

#PSUEDO TESTS
def psuedo_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test 1: Head at the minimum board limit, food below head, no body
        head_x = 0
        head_y = 0
        food_x = 0
        food_y = 1
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = []
        expected_output = [0, 1, 2, 1, 0, 0, 0, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test 2: Head at the maximum board limit, food to the left of head, no body
        head_x = 10
        head_y = 10
        food_x = 9
        food_y = 10
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = []
        expected_output = [1, 2, 0, 1, 0, 0, 0, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test 3: Head in the middle, food to the right and above head, body surrounding head
        head_x = 5
        head_y = 5
        food_x = 6
        food_y = 4
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(4, 5), (5, 6), (6, 5), (5, 4)]
        expected_output = [2, 2, 1, 0, 1, 1, 1, 1]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test 4: Head and food at the same position, no body
        head_x = 3
        head_y = 3
        food_x = 3
        food_y = 3
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = []
        expected_output = [2, 2, 2, 2, 0, 0, 0, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test 5: Head and food at the same position, with body covering all adjacent positions
        head_x = 5
        head_y = 5
        food_x = 5
        food_y = 5
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(4, 5), (5, 6), (6, 5), (5, 4), (4, 4), (4, 6), (6, 6), (6, 4)]
        expected_output = [2, 2, 2, 2, 1, 1, 1, 1]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test 6: Head and food at the same position, with body covering only top adjacent position
        head_x = 5
        head_y = 5
        food_x = 5
        food_y = 5
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(4, 5)]
        expected_output = [2, 2, 2, 2, 1, 0, 0, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test 7: Head at the minimum board limit, food to the left of head, body covering all adjacent positions
        head_x = 0
        head_y = 0
        food_x = 0
        food_y = 1
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(0, 1), (1, 0), (1, 1)]
        expected_output = [0, 1, 2, 1, 1, 1, 1, 1]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test 8: Head at the maximum board limit, food to the left of head, body covering only top adjacent position
        head_x = 10
        head_y = 10
        food_x = 10
        food_y = 9
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(10, 9)]
        expected_output = [1, 2, 0, 1, 1, 0, 0, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test 9: Head and food at the same position, with body covering only left adjacent position
        head_x = 5
        head_y = 5
        food_x = 5
        food_y = 5
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(5, 4)]
        expected_output = [2, 2, 2, 2, 0, 0, 1, 0]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test 10: Head and food at the same position, with body covering only right adjacent position
        head_x = 5
        head_y = 5
        food_x = 5
        food_y = 5
        BOARD_LIMIT_MIN = 0
        BOARD_LIMIT_MAX = 10
        GRID_SIZE = 10
        body = [(5, 6)]
        expected_output = [2, 2, 2, 2, 0, 0, 0, 1]
        assert func9(head_x, head_y, food_x, food_y, BOARD_LIMIT_MIN, BOARD_LIMIT_MAX, GRID_SIZE, body) == expected_output
    except Exception as e:
        print(f"{repr(e)} on test case 10")
        count += 1

    print(f"Total failed test cases: {count}")
    return count

def getFailRatio(): # pragma: no cover
    return failed_ratio

cov = coverage.Coverage() # pragma: no cover
# start coverage
cov.start() # pragma: no cover

failed_ratio = psuedo_test_cases() / 10 # pragma: no cover

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
