tests = [
    '''import hypothesis
from hypothesis import given, strategies as st

@given(st.text())
def test_para_flat_func1(string):
    orig =  orig_func1(string)
    flat = para_flat_func1(string)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(st.text())
def test_para_struc_func1(string):
    orig =  orig_func1(string)
    struc =  para_struc_func1(string)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(st.text())
def test_bullet_flat_func1(string):
    orig =  orig_func1(string)
    flat = bullet_flat_func1(string)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(st.text())
def test_bullet_struc_func1(string):
    orig =  orig_func1(string)
    struc =  bullet_struc_func1(string)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(st.text())
def test_psuedo_func1(string):
    orig =  orig_func1(string)
    psuedo = psuedo_func1(string)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
from hypothesis import given, strategies as st

@given(arr= st.lists(elements=st.integers(0, 15), min_size=0), target= st.integers())
def test_para_flat_func2(arr, target):
    orig =  orig_func2(arr, target)
    flat = para_flat_func2(arr, target)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(arr= st.lists(elements=st.integers(0, 15), min_size=0), target= st.integers())
def test_para_struc_func2(arr, target):
    orig =  orig_func2(arr, target)
    struc =  para_struc_func2(arr, target)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(arr= st.lists(elements=st.integers(0, 15), min_size=0), target= st.integers())
def test_bullet_flat_func2(arr, target):
    orig =  orig_func2(arr, target)
    flat = bullet_flat_func2(arr, target)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(arr= st.lists(elements=st.integers(0, 15), min_size=0), target= st.integers())
def test_bullet_struc_func2(arr, target):
    orig =  orig_func2(arr, target)
    struc =  bullet_struc_func2(arr, target)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(arr= st.lists(elements=st.integers(0, 15), min_size=0), target= st.integers())
def test_psuedo_func2(arr, target):
    orig =  orig_func2(arr, target)
    psuedo = psuedo_func2(arr, target)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
from hypothesis import given, strategies as st

@given(entity_type= st.integers(min_value=0, max_value=2), attack_type= st.lists(st.integers(min_value=0, max_value= 5), min_size= 2), 
curr_health= st.integers(min_value=0, max_value=100), tot_health= st.integers(min_value=0, max_value=100), attack_mag= st.integers(min_value=0, max_value=20))
def test_para_flat_func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    orig =  orig_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    flat = para_flat_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(entity_type= st.integers(min_value=0, max_value=2), attack_type= st.lists(st.integers(min_value=0, max_value= 5), min_size= 2), 
curr_health= st.integers(min_value=0, max_value=100), tot_health= st.integers(min_value=0, max_value=100), attack_mag= st.integers(min_value=0, max_value=20))
def test_para_struc_func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    orig =  orig_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    struc =  para_struc_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(entity_type= st.integers(min_value=0, max_value=2), attack_type= st.lists(st.integers(min_value=0, max_value= 5), min_size= 2), 
curr_health= st.integers(min_value=0, max_value=100), tot_health= st.integers(min_value=0, max_value=100), attack_mag= st.integers(min_value=0, max_value=20))
def test_bullet_flat_func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    orig =  orig_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    flat = bullet_flat_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(entity_type= st.integers(min_value=0, max_value=2), attack_type= st.lists(st.integers(min_value=0, max_value= 5), min_size= 2), 
curr_health= st.integers(min_value=0, max_value=100), tot_health= st.integers(min_value=0, max_value=100), attack_mag= st.integers(min_value=0, max_value=20))
def test_bullet_struc_func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    orig =  orig_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    struc =  bullet_struc_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(entity_type= st.integers(min_value=0, max_value=2), attack_type= st.lists(st.integers(min_value=0, max_value= 5), min_size= 2), 
curr_health= st.integers(min_value=0, max_value=100), tot_health= st.integers(min_value=0, max_value=100), attack_mag= st.integers(min_value=0, max_value=20))
def test_psuedo_func3(entity_type, attack_type, curr_health, tot_health, attack_mag):
    orig =  orig_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    psuedo = psuedo_func3(entity_type, attack_type, curr_health, tot_health, attack_mag)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import math
import hypothesis
from hypothesis import given, strategies as st

@given(pt1= st.tuples(st.integers(), st.integers()), pt2= st.tuples(st.integers(), st.integers()), pt3= st.tuples(st.integers(), st.integers()))
def test_para_flat_func4(pt1, pt2, pt3):
    orig =  orig_func4(pt1, pt2, pt3)
    flat = para_flat_func4(pt1, pt2, pt3)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(pt1= st.tuples(st.integers(), st.integers()), pt2= st.tuples(st.integers(), st.integers()), pt3= st.tuples(st.integers(), st.integers()))
def test_para_struc_func4(pt1, pt2, pt3):
    orig =  orig_func4(pt1, pt2, pt3)
    struc =  para_struc_func4(pt1, pt2, pt3)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(pt1= st.tuples(st.integers(), st.integers()), pt2= st.tuples(st.integers(), st.integers()), pt3= st.tuples(st.integers(), st.integers()))
def test_bullet_flat_func4(pt1, pt2, pt3):
    orig =  orig_func4(pt1, pt2, pt3)
    flat = bullet_flat_func4(pt1, pt2, pt3)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(pt1= st.tuples(st.integers(), st.integers()), pt2= st.tuples(st.integers(), st.integers()), pt3= st.tuples(st.integers(), st.integers()))
def test_bullet_struc_func4(pt1, pt2, pt3):
    orig =  orig_func4(pt1, pt2, pt3)
    struc =  bullet_struc_func4(pt1, pt2, pt3)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(pt1= st.tuples(st.integers(), st.integers()), pt2= st.tuples(st.integers(), st.integers()), pt3= st.tuples(st.integers(), st.integers()))
def test_psuedo_func4(pt1, pt2, pt3):
    orig =  orig_func4(pt1, pt2, pt3)
    psuedo = psuedo_func4(pt1, pt2, pt3)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
import numpy as np
from hypothesis import given, settings, strategies as st

rand_board = np.random.choice([1, 2], size=[7, 7], replace=True)
print(rand_board)

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

@given(n= st.lists(elements=st.integers(0, 15), min_size=0))
def test_para_flat_func6(n):
    orig = orig_func6(n)
    flat = para_flat_func6(n)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

@given(n= st.lists(elements=st.integers(0, 15), min_size=0))
def test_para_struc_func6(n):
    orig = orig_func6(n)
    struc = para_struc_func6(n)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

@given(n= st.lists(elements=st.integers(0, 15), min_size=0))
def test_bullet_flat_func6(n):
    orig = orig_func6(n)
    flat = bullet_struc_func6(n)
    #print(f"orig= {orig}, flat= {flat}")
    assert orig == flat

@given(n= st.lists(elements=st.integers(0, 15), min_size=0))
def test_bullet_struc_func6(n):
    orig = orig_func6(n)
    struc = bullet_struc_func6(n)
    #print(f"orig= {orig}, struc= {struc}")
    assert orig == struc

@given(n= st.lists(elements=st.integers(0, 15), min_size=0))
def test_psuedo_func6(n):
    orig = orig_func6(n)
    psuedo = psuedo_func6(n)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert orig == psuedo
    ''',

    '''import math
import hypothesis
from hypothesis import given, strategies as st

@given(num= st.integers())
def test_para_flat_func7(num):
    orig =  orig_func7(num)
    flat = para_flat_func7(num)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(num= st.integers())
def test_para_struc_func7(num):
    orig =  orig_func7(num)
    struc =  para_struc_func7(num)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(num= st.integers())
def test_bullet_flat_func7(num):
    orig =  orig_func7(num)
    flat = bullet_flat_func7(num)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(num= st.integers())
def test_bullet_struc_func7(num):
    orig =  orig_func7(num)
    struc =  bullet_struc_func7(num)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(num= st.integers())
def test_psuedo_func7(num):
    orig =  orig_func7(num)
    psuedo = psuedo_func7(num)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
from hypothesis import given, strategies as st

@given(num= st.floats(min_value= 0, allow_nan= False, allow_infinity= False, width= 16))
def test_para_flat_func8(num):
    orig =  orig_func8(num)
    flat = para_flat_func8(num)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(num= st.floats(min_value= 0, allow_nan= False, allow_infinity= False, width= 16))
def test_para_struc_func8(num):
    orig =  orig_func8(num)
    struc =  para_struc_func8(num)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(num= st.floats(min_value= 0, allow_nan= False, allow_infinity= False, width= 16))
def test_bullet_flat_func8(num):
    orig =  orig_func8(num)
    flat = bullet_flat_func8(num)
    #print(f"orig= {orig}, flat= {flat}")
    assert  orig == flat

@given(num= st.floats(min_value= 0, allow_nan= False, allow_infinity= False, width= 16))
def test_bullet_struc_func8(num):
    orig =  orig_func8(num)
    struc =  bullet_struc_func8(num)
    #print(f"orig= {orig}, struc= {struc}")
    assert  orig == struc

@given(num= st.floats(min_value= 0, allow_nan= False, allow_infinity= False, width= 16))
def test_psuedo_func8(num):
    orig =  orig_func8(num)
    psuedo = psuedo_func8(num)
    #print(f"orig= {orig}, psuedo= {psuedo}")
    assert  orig == psuedo
    ''',

    '''import hypothesis
import math
import numpy as np
from hypothesis import given, strategies as st

choices = [40, 80, 120, 160, 200, 240]
body_len = np.random.randint(1, 10)
rand_body = np.random.choice([40, 80, 120, 160, 200, 240], size=[body_len, 2])
rand_body.tolist()
rand_body = [list(b) for b in rand_body]

def test_para_flat_func9():
    for head_x, head_y, food_x, food_y in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
        orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        flat = para_flat_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        #print(f"orig= {orig}, flat= {flat}")
        assert  orig == flat

def test_para_struc_func9():
    for head_x, head_y, food_x, food_y in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
        orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        struc =  para_struc_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        #print(f"orig= {orig}, struc= {struc}")
        assert  orig == struc

def test_bullet_flat_func9():
    for head_x, head_y, food_x, food_y in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
        orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        flat = bullet_flat_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        #print(f"orig= {orig}, flat= {flat}")
        assert  orig == flat

def test_bullet_struc_func9():
    for head_x, head_y, food_x, food_y in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
        orig =  orig_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        struc =  bullet_struc_func9(head_x, head_y, food_x, food_y, 40, 240, 40, rand_body)
        #print(f"orig= {orig}, struc= {struc}")
        assert  orig == struc

def test_psuedo_func9():
    for head_x, head_y, food_x, food_y in ((a,b,c,d) for a in choices for b in choices for c in choices for d in choices):
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
    ''',
    '''import re
import hypothesis
from hypothesis import given, strategies as st

test_results = [
                [{"nothing": "null"},
                {"_hypothesis_stats": "53 passing, 41 failing on first pass. 1 passed, 93 failing sceond pass"},
                {"outcome": "failed"}
                ],
                [{"_hypothesis_stats": "53 passing, 41 failing on first pass. 1 passed, 93 failing sceond pass"},
                 {"_hypothesis_stats": "23 passing, 1 failing, 46 redone on first pass. 1 passed, 56 failing on second pass. "},
                 {"_hypothesis_stats": "23 passing, 1 failing on first pass. 1 passed, 56 failing,  46 redone on second pass. "}
                ],
                [{"outcome": "success"},
                 {"outcome": "success"},
                ],
                [{"outcome": "success"},
                 {"outcome": "success"},
                 {"outcome": "success"},
                 {"outcome": "failed"}
                ],
                [{"random": "junk"},
                 {"do not": "use"},
                 {"outcome": "success"}
                ],
                [{"_hypothesis_stats": "- passing, 41 failing on first pass. 1 passed, 93 failing sceond pass"},
                 {"_hypothesis_stats": "23 passing, 1 failing, - redone on first pass. 1 passed, - failing on second pass. "},
                 {"_hypothesis_stats": "45 passing, 2 failing on first pass. 56 passed, 2 failing,  - redone on second pass. "}
                ],
                [{"_hypothesis_stats": "- passing, 41 failing on first pass. 1 passed, 93 failing sceond pass"},
                 {"_hypothesis_stats": "23 passing, 1 failing, - redone on first pass. 1 passed, - failing on second pass. "},
                 {"_hypothesis_stats": "- passing, 2 failing on first pass. - passed, - failing,  3 redone on second pass. "}
                ],
                [{"_hypothesis_stat": "- passing, 41 failing on first pass. 1 passed, 93 failing sceond pass"},
                 {"hypothesis_stats": "23 passing, 1 failing, - redone on first pass. 1 passed, - failing on second pass. "},
                 {"_hypothess_stats": "- passing, 2 failing on first pass. - passed, 3 failing,  - redone on second pass. "},
                 {"outcome": "success"}
                ]
                ]

def test_para_flat_func12(results= test_results):
    for res in results:
        orig =  orig_func12(res)
        flat = para_flat_func12(res)
        #print(f"orig= {orig}, flat= {flat}")
        assert  orig == flat

def test_para_struc_func12(results= test_results):
    for res in results:
        orig =  orig_func12(res)
        struc =  para_struc_func12(res)
        #print(f"orig= {orig}, struc= {struc}")
        assert  orig == struc

def test_bullet_flat_func12(results= test_results):
    for res in results:
        orig =  orig_func12(res)
        flat = bullet_flat_func12(res)
        #print(f"orig= {orig}, flat= {flat}")
        assert  orig == flat

def test_bullet_struc_func12(results= test_results):
    for res in results:
        orig =  orig_func12(res)
        struc =  bullet_struc_func12(res)
        #print(f"orig= {orig}, struc= {struc}")
        assert  orig == struc

def test_psuedo_func12(results= test_results):
    for res in results:
        orig =  orig_func12(res)
        psuedo = psuedo_func12(res)
        #print(f"orig= {orig}, psuedo= {psuedo}")
        assert  orig == psuedo
    '''
]