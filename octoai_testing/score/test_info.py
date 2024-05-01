import coverage
import math
import sys

sys.path.insert(0, '../../octoai_testing')

# ACCESS TO TOKEN COUNTS
import info.orig_info as oi
import info.gen_info as gi

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
cov_5.load()
cov_6 = coverage.Coverage(data_file="../code_tests/func6/.coverage")
cov_6.load()
cov_9 = coverage.Coverage(data_file="../code_tests/func9/.coverage")
cov_9.load()
cov_10 = coverage.Coverage(data_file="../code_tests/func10/.coverage")
cov_10.load()
cov_11 = coverage.Coverage(data_file="../code_tests/func11/.coverage")
cov_11.load()

# ARRAY INDEX MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)

# COVERAGE TEST FAIL RATIOS
func5_fail_ratios = [func5_pf.getFailRatio(), func5_pst.getFailRatio(), func5_bf.getFailRatio(), func5_bst.getFailRatio(), func5_psu.getFailRatio()]
func6_fail_ratios = [func6_pf.getFailRatio(), func6_pst.getFailRatio(), func6_bf.getFailRatio(), func6_bst.getFailRatio(), func6_psu.getFailRatio()]
func9_fail_ratios = [func9_pf.getFailRatio(), func9_pst.getFailRatio(), func9_bf.getFailRatio(), func9_bst.getFailRatio(), func9_psu.getFailRatio()]
func10_fail_ratios = [func10_pf.getFailRatio(), func10_pst.getFailRatio(), func10_bf.getFailRatio(), func10_bst.getFailRatio(), func10_psu.getFailRatio()]
func11_fail_ratios = [func11_pf.getFailRatio(), func11_pst.getFailRatio(), func11_bf.getFailRatio(), func11_bst.getFailRatio(), func11_psu.getFailRatio()]

# Performs equation
def score_eq(name, leq, cover, fail, prompt_style):
    a, b, c = 3, 1, 2
    #score = token*(1/(1 + a*leq) +  1/(1 + math.pow(1 - fail, b) + math.pow(cover, c)))
    gen_tok = gi.getFuncSummLen()[name][prompt_style]
    orig_tok = oi.getFuncLen()[name]
    score = (a*leq + math.pow(fail, b) + math.pow(cover, c))/ (gen_tok / orig_tok)
    return score

# Calls and prints equation plus input info
def print_score(token, leq, cover, fail, prompt_style):
    print(f"token= {token}, leq= {leq}, cover= {cover}, fail= {fail}, style= {prompt_style}")
    score = score_eq(token, leq, cover, fail, prompt_style)
    print(score)
    return score