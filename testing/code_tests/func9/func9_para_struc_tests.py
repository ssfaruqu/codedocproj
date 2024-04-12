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

#PARA STRUC TESTS
def para_struc_test_cases(): # pragma: no cover
    try:
        count = 1 # Test 1: Basic test case with head adjacent to the minimum X limit and food to the right
        head_x1, head_y1 = 0, 5
        food_x1, food_y1 = 2, 5
        BOARD_LIMIT_MIN1, BOARD_LIMIT_MAX1 = 0, 10
        GRID_SIZE1 = 1
        body1 = [(1, 5), (2, 5), (3, 5)]
        expected_output1 = [1, 2, 1, 2, 0, 0, 0, 1]
        output1 = func9(head_x1, head_y1, food_x1, food_y1, BOARD_LIMIT_MIN1, BOARD_LIMIT_MAX1, GRID_SIZE1, body1)
        assert output1 == expected_output1

        count += 1 # Test 2: Test case with head adjacent to the maximum Y limit and food below
        head_x2, head_y2 = 8, 9
        food_x2, food_y2 = 8, 7
        BOARD_LIMIT_MIN2, BOARD_LIMIT_MAX2 = 0, 10
        GRID_SIZE2 = 1
        body2 = [(8, 8), (8, 7), (7, 7)]
        expected_output2 = [0, 1, 2, 0, 0, 0, 1, 0]
        output2 = func9(head_x2, head_y2, food_x2, food_y2, BOARD_LIMIT_MIN2, BOARD_LIMIT_MAX2, GRID_SIZE2, body2)
        assert output2 == expected_output2

        count += 1 # Test 3: Test case with head adjacent to neither X nor Y limit and food to the left
        head_x3, head_y3 = 5, 5
        food_x3, food_y3 = 3, 5
        BOARD_LIMIT_MIN3, BOARD_LIMIT_MAX3 = 0, 10
        GRID_SIZE3 = 1
        body3 = [(4, 5), (3, 5), (3, 6)]
        expected_output3 = [2, 2, 0, 0, 0, 0, 1, 0]
        output3 = func9(head_x3, head_y3, food_x3, food_y3, BOARD_LIMIT_MIN3, BOARD_LIMIT_MAX3, GRID_SIZE3, body3)
        assert output3 == expected_output3

        count += 1 # Test 4: Test case with food in the same row as the head but to the left
        head_x4, head_y4 = 3, 2
        food_x4, food_y4 = 2, 2
        BOARD_LIMIT_MIN4, BOARD_LIMIT_MAX4 = 0, 10
        GRID_SIZE4 = 1
        body4 = [(3, 3), (2, 3), (2, 2)]
        expected_output4 = [2, 0, 0, 0, 0, 0, 0, 1]
        output4 = func9(head_x4, head_y4, food_x4, food_y4, BOARD_LIMIT_MIN4, BOARD_LIMIT_MAX4, GRID_SIZE4, body4)
        assert output4 == expected_output4

        count += 1 # Test 5: Test case with food in the same column as the head but below
        head_x5, head_y5 = 7, 8
        food_x5, food_y5 = 7, 9
        BOARD_LIMIT_MIN5, BOARD_LIMIT_MAX5 = 0, 10
        GRID_SIZE5 = 1
        body5 = [(7, 7), (7, 6), (6, 6)]
        expected_output5 = [0, 2, 0, 0, 0, 1, 0, 0]
        output5 = func9(head_x5, head_y5, food_x5, food_y5, BOARD_LIMIT_MIN5, BOARD_LIMIT_MAX5, GRID_SIZE5, body5)
        assert output5 == expected_output5

        count += 1 # Test 6: Test case with head adjacent to the minimum Y limit and food above
        head_x6, head_y6 = 3, 0
        food_x6, food_y6 = 3, 2
        BOARD_LIMIT_MIN6, BOARD_LIMIT_MAX6 = 0, 10
        GRID_SIZE6 = 1
        body6 = [(3, 1), (3, 2), (4, 2)]
        expected_output6 = [0, 0, 0, 1, 0, 0, 0, 0]
        output6 = func9(head_x6, head_y6, food_x6, food_y6, BOARD_LIMIT_MIN6, BOARD_LIMIT_MAX6, GRID_SIZE6, body6)
        assert output6 == expected_output6

        count += 1 # Test 7: Test case with head adjacent to the maximum X limit and food to the left
        head_x7, head_y7 = 9, 5
        food_x7, food_y7 = 7, 5
        BOARD_LIMIT_MIN7, BOARD_LIMIT_MAX7 = 0, 10
        GRID_SIZE7 = 1
        body7 = [(8, 5), (7, 5), (7, 4)]
        expected_output7 = [1, 0, 2, 0, 0, 0, 1, 0]
        output7 = func9(head_x7, head_y7, food_x7, food_y7, BOARD_LIMIT_MIN7, BOARD_LIMIT_MAX7, GRID_SIZE7, body7)
        assert output7 == expected_output7

        count += 1 # Test 8: Test case with head adjacent to the minimum X limit and food to the right
        head_x8, head_y8 = 0, 5
        food_x8, food_y8 = 2, 5
        BOARD_LIMIT_MIN8, BOARD_LIMIT_MAX8 = 0, 10
        GRID_SIZE8 = 1
        body8 = [(1, 5), (2, 5), (3, 5)]
        expected_output8 = [1, 2, 1, 2, 0, 0, 0, 1]
        output8 = func9(head_x8, head_y8, food_x8, food_y8, BOARD_LIMIT_MIN8, BOARD_LIMIT_MAX8, GRID_SIZE8, body8)
        assert output8 == expected_output8

        count += 1 # Test 9: Test case with head adjacent to the maximum Y limit and food below
        head_x9, head_y9 = 8, 9
        food_x9, food_y9 = 8, 7
        BOARD_LIMIT_MIN9, BOARD_LIMIT_MAX9 = 0, 10
        GRID_SIZE9 = 1
        body9 = [(8, 8), (8, 7), (7, 7)]
        expected_output9 = [0, 1, 2, 0, 0, 0, 1, 0]
        output9 = func9(head_x9, head_y9, food_x9, food_y9, BOARD_LIMIT_MIN9, BOARD_LIMIT_MAX9, GRID_SIZE9, body9)
        assert output9 == expected_output9

        count += 1 # Test 10: Test case with head adjacent to neither X nor Y limit and food to the left
        head_x10, head_y10 = 5, 5
        food_x10, food_y10 = 3, 5
        BOARD_LIMIT_MIN10, BOARD_LIMIT_MAX10 = 0, 10
        GRID_SIZE10 = 1
        body10 = [(4, 5), (3, 5), (3, 6)]
        expected_output10 = [2, 2, 0, 0, 0, 0, 1, 0]
        output10 = func9(head_x10, head_y10, food_x10, food_y10, BOARD_LIMIT_MIN10, BOARD_LIMIT_MAX10, GRID_SIZE10, body10)
        assert output10 == expected_output10

        print("All tests passed!")
    except Exception as e:
        print(f"{repr(e)} on test case {count}")
        print("PARA STRUC TEST CASE FAILED\n")

para_struc_test_cases() # pragma: no cover

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

print("Para Struc Coverage Percentage:", coverage_percentage) # pragma: no cover