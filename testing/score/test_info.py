import coverage
import math

# ACCESS TO TEST CASE FAIL RATIOS
import sys

sys.path.insert(0, '../../testing')

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func5_logic_equiv as func5_le
import logic_equiv.func6_logic_equiv as func6_le
import logic_equiv.func9_logic_equiv as func9_le
import logic_equiv.func10_logic_equiv as func10_le
import logic_equiv.func11_logic_equiv as func11_le

# ACCESS TO FAIL RATIOS
import code_tests.func5.func5_para_flat_tests as func5_pf
import code_tests.func5.func5_para_struc_tests as func5_pst
import code_tests.func5.func5_bullet_flat_tests as func5_bf
import code_tests.func5.func5_bullet_struc_tests as func5_bst
import code_tests.func5.func5_psuedo_tests as func5_psu
import code_tests.func6.func6_para_flat_tests as func6_pf
import code_tests.func6.func6_para_struc_tests as func6_pst
import code_tests.func6.func6_bullet_flat_tests as func6_bf
import code_tests.func6.func6_bullet_struc_tests as func6_bst
import code_tests.func6.func6_psuedo_tests as func6_psu
import code_tests.func9.func9_para_flat_tests as func9_pf
import code_tests.func9.func9_para_struc_tests as func9_pst
import code_tests.func9.func9_bullet_flat_tests as func9_bf
import code_tests.func9.func9_bullet_struc_tests as func9_bst
import code_tests.func9.func9_psuedo_tests as func9_psu
import code_tests.func10.func10_para_flat_tests as func10_pf
import code_tests.func10.func10_para_struc_tests as func10_pst
import code_tests.func10.func10_bullet_flat_tests as func10_bf
import code_tests.func10.func10_bullet_struc_tests as func10_bst
import code_tests.func10.func10_psuedo_tests as func10_psu
import code_tests.func11.func11_para_flat_tests as func11_pf
import code_tests.func11.func11_para_struc_tests as func11_pst
import code_tests.func11.func11_bullet_flat_tests as func11_bf
import code_tests.func11.func11_bullet_struc_tests as func11_bst
import code_tests.func11.func11_psuedo_tests as func11_psu

# ACCESS TO TEST COVERAGE RATIOS
cov_5 = coverage.Coverage(data_file="../code_tests/func5/.coverage")
cov_6 = coverage.Coverage(data_file="../code_tests/func6/.coverage")
cov_9 = coverage.Coverage(data_file="../code_tests/func9/.coverage")
cov_10 = coverage.Coverage(data_file="../code_tests/func10/.coverage")
cov_11 = coverage.Coverage(data_file="../code_tests/func11/.coverage")

# ARRAY INDEX MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)

# INPUT TOKEN COUNTS
# func5_pf_count, func6_pf_count, func9_pf_count, func10_pf_count, func11_pf_count =        (492, 613, 660, 890, 584)
# func5_pst_count, func6_pst_count, func9_pst_count, func10_pst_count, func11_pst_count = (1271, 995, 1606, 1307, 962)
# func5_bf_count, func6_bf_count, func9_bf_count, func10_bf_count, func11_bf_count =      (1366, 423, 1060, 1212, 811)
# func5_bst_count, func6_bst_count, func9_bst_count, func10_bst_count, func11_bst_count = (1536, 479, 2150, 1370, 894)
# func5_psu_count, func6_psu_count, func9_psu_count, func10_psu_count, func11_psu_count = (1483, 444, 1662, 1110, 926)
func5_count = [492, 1271, 1366, 1536, 1483]
func6_count = [613, 995, 423, 479, 444]
func9_count = [660, 1606, 1060, 2150, 1662]
func10_count = [890, 1307, 1212, 1370, 1110]
func11_count = [584, 962, 811, 894, 926]

# COVERAGE TEST FAIL RATIOS
func5_fail_ratios = [func5_pf.getFailRatio(), func5_pst.getFailRatio(), func5_bf.getFailRatio(), func5_bst.getFailRatio(), func5_psu.getFailRatio()]
func6_fail_ratios = [func6_pf.getFailRatio(), func6_pst.getFailRatio(), func6_bf.getFailRatio(), func6_bst.getFailRatio(), func6_psu.getFailRatio()]
func9_fail_ratios = [func9_pf.getFailRatio(), func9_pst.getFailRatio(), func9_bf.getFailRatio(), func9_bst.getFailRatio(), func9_psu.getFailRatio()]
func10_fail_ratios = [func10_pf.getFailRatio(), func10_pst.getFailRatio(), func10_bf.getFailRatio(), func10_bst.getFailRatio(), func10_psu.getFailRatio()]
func11_fail_ratios = [func11_pf.getFailRatio(), func11_pst.getFailRatio(), func11_bf.getFailRatio(), func11_bst.getFailRatio(), func11_psu.getFailRatio()]

# Performs equation
def score_eq(token, leq, cover, fail):
    a, b, c = 2, 2, 2
    score = token*(math.pow(leq, a) + math.pow(cover, b)*math.pow(fail, c))
    return score

# Calls and prints equation plus input info
def print_score(token, le, cover, fail):
    print(f"token= {token}, le= {le}, cover= {cover}, fail= {fail}")
    score = score_eq(token, le, cover, fail)
    print(score)