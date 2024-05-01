tests = [
    '''import hypothesis
import numpy as np
from hypothesis import given, settings, strategies as st
from hypothesis._settings import Phase

rand_board = np.random.choice([1, 2], size=[7, 7], replace=True)
print(rand_board)

#FAIL
#@settings(phases=[Phase.explicit])
@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_para_flat_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col, rand_board)
    flat = para_flat_func5(player_number, row, col, rand_board)
    assert  orig == flat

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_para_struc_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col, rand_board)
    struc =  para_struc_func5(player_number, row, col, rand_board)
    assert  orig == struc

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_bullet_flat_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col, rand_board)
    flat = bullet_flat_func5(player_number, row, col, rand_board)
    assert  orig == flat

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_bullet_struc_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col, rand_board)
    struc =  bullet_struc_func5(player_number, row, col, rand_board)
    assert  orig == struc

@given(player_number= st.integers(min_value=1, max_value=2), row= st.integers(min_value=0, max_value=6), col= st.integers(min_value=0, max_value=6))
def test_psuedo_func5(player_number, row, col):
    orig =  orig_func5(player_number, row, col, rand_board)
    psuedo = psuedo_func5(player_number, row, col, rand_board)
    assert  orig == psuedo
    ''',

    '''import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

rand_arr = [np.random.randint(10) for i in range(0,7)]

def test_para_flat_func6():
    orig = orig_func6(rand_arr)
    flat = para_flat_func6(rand_arr)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

def test_para_struc_func6():
    orig = orig_func6(rand_arr)
    struc = para_struc_func6(rand_arr)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

def test_bullet_flat_func6():
    orig = orig_func6(rand_arr)
    flat = bullet_struc_func6(rand_arr)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

def test_bullet_struc_func6():
    orig = orig_func6(rand_arr)
    struc = bullet_struc_func6(rand_arr)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

def test_psuedo_func6():
    orig = orig_func6(rand_arr)
    psuedo = psuedo_func6(rand_arr)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert orig == psuedo
    ''',

    '''import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

body_len = np.random.randint(1, 10)
rand_body = np.random.choice([40, 80, 120, 160, 200, 240], size=[body_len, 2])
rand_body.tolist()
rand_body = [list(b) for b in rand_body]
print(rand_body)

def test_para_flat_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    flat = para_flat_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

def test_para_struc_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    struc =  para_struc_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

def test_bullet_flat_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    flat = bullet_flat_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

def test_bullet_struc_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    struc =  bullet_struc_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

def test_psuedo_func9(head_x, head_y, food_x, food_y):
    orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    psuedo = psuedo_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
from hypothesis import given, strategies as st

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_para_flat_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    flat = para_flat_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == flat

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_para_struc_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    struc =  para_struc_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == struc

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_bullet_flat_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    flat = bullet_flat_func10(a,b,c)
    #print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    assert  orig == flat

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_bullet_struc_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    struc =  bullet_struc_func10(a,b,c)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(a= st.characters(min_codepoint=0, max_codepoint=10000), b= st.characters(min_codepoint=0, max_codepoint=10000), c= st.integers(min_value=0, max_value=3))
def test_psuedo_func10(a,b,c):
    orig =  orig_func10(a,b,c)
    psuedo = psuedo_func10(a,b,c)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

x = np.random.randint(1, 7)
y = np.random.randint(1, 7)
rand_grid = list(np.random.randint(-10, 10, size=[x, y]))
print(rand_grid)

@given(reverse= st.integers(min_value=0, max_value=1))
def test_para_flat_func11(reverse):
    orig =  orig_func11(reverse, rand_grid)
    flat = para_flat_func11(reverse, rand_grid)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(reverse= st.integers(min_value=0, max_value=1))
def test_para_struc_func11(reverse):
    orig =  orig_func11(reverse, rand_grid)
    struc =  para_struc_func11(reverse, rand_grid)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(reverse= st.integers(min_value=0, max_value=1))
def test_bullet_flat_func11(reverse):
    orig =  orig_func11(reverse, rand_grid)
    flat = bullet_flat_func11(reverse, rand_grid)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(reverse= st.integers(min_value=0, max_value=1))
def test_bullet_struc_func11(reverse):
    orig =  orig_func11(reverse, rand_grid)
    struc =  bullet_struc_func11(reverse, rand_grid)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(reverse= st.integers(min_value=0, max_value=1))
def test_psuedo_func11(reverse):
    orig =  orig_func11(reverse, rand_grid)
    psuedo = psuedo_func11(reverse, rand_grid)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    '''
]