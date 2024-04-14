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

#PARA FLAT TESTS
def para_flat_test_cases(): # pragma: no cover
    count = 0

    try:
        # Test case 1: Head at top-left corner, no food, no body
        assert func9((0, 0), None, (10, 10), [])
    except Exception as e:
        print(f"{repr(e)} on test case 1")
        count += 1

    try:
        # Test case 2: Head at bottom-right corner, food at top-left corner, no body
        assert func9((9, 9), (0, 0), (10, 10), [])
    except Exception as e:
        print(f"{repr(e)} on test case 2")
        count += 1

    try:
        # Test case 3: Head at center, food at bottom-right corner, body surrounding
        assert func9((5, 5), (9, 9), (10, 10), [(4, 5), (6, 5), (5, 4), (5, 6)])
    except Exception as e:
        print(f"{repr(e)} on test case 3")
        count += 1

    try:
        # Test case 4: Head at top-right corner, food at bottom-left corner, no body
        assert func9((0, 9), (9, 0), (10, 10), [])
    except Exception as e:
        print(f"{repr(e)} on test case 4")
        count += 1

    try:
        # Test case 5: Head at bottom-left corner, food at top-right corner, body at top-left corner
        assert func9((9, 0), (0, 9), (10, 10), [(0, 0), (0, 1), (1, 0)])
    except Exception as e:
        print(f"{repr(e)} on test case 5")
        count += 1

    try:
        # Test case 6: Head at top-left corner, food at top-right corner, body at bottom-left corner
        assert func9((0, 0), (0, 9), (10, 10), [(9, 0), (9, 1), (8, 0)])
    except Exception as e:
        print(f"{repr(e)} on test case 6")
        count += 1

    try:
        # Test case 7: Head at top-left corner, food at bottom-right corner, body forming a ring around food
        assert func9((0, 0), (9, 9), (10, 10), [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 0)])
    except Exception as e:
        print(f"{repr(e)} on test case 7")
        count += 1

    try:
        # Test case 8: Head at bottom-left corner, food at top-left corner, body forming a straight line along the right side
        assert func9((9, 0), (0, 0), (10, 10), [(8, 9), (7, 9), (6, 9), (5, 9), (4, 9)])
    except Exception as e:
        print(f"{repr(e)} on test case 8")
        count += 1

    try:
        # Test case 9: Head at bottom-right corner, food at top-right corner, body forming a straight line along the left side
        assert func9((9, 9), (0, 9), (10, 10), [(8, 0), (7, 0), (6, 0), (5, 0), (4, 0)])
    except Exception as e:
        print(f"{repr(e)} on test case 9")
        count += 1

    try:
        # Test case 10: Head in the middle, food at top-right corner, body forming a circle around the head
        assert func9((5, 5), (0, 9), (10, 10), [(4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (5, 4), (4, 4)])
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

failed_ratio = para_flat_test_cases() / 10 # pragma: no cover

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
