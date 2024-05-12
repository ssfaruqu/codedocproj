import coverage
import math
import argparse
import sys

sys.path.insert(0, '../../openai_testing')

# ACCESS TO TOKEN COUNTS
import info.orig_info as oi
import info.gen_info as gi

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func1_logic_equiv as func1_le
import logic_equiv.func2_logic_equiv as func2_le
import logic_equiv.func3_logic_equiv as func3_le
import logic_equiv.func4_logic_equiv as func4_le
import logic_equiv.func5_logic_equiv as func5_le
import logic_equiv.func6_logic_equiv as func6_le
import logic_equiv.func7_logic_equiv as func7_le
import logic_equiv.func8_logic_equiv as func8_le
import logic_equiv.func9_logic_equiv as func9_le
import logic_equiv.func10_logic_equiv as func10_le
import logic_equiv.func11_logic_equiv as func11_le
import logic_equiv.func12_logic_equiv as func12_le

# ACCESS TO FAIL RATIOS
import code_tests.func1.func1_para_flat_tests as func1_pf
import code_tests.func1.func1_para_struc_tests as func1_pst
import code_tests.func1.func1_bullet_flat_tests as func1_bf
import code_tests.func1.func1_bullet_struc_tests as func1_bst
import code_tests.func1.func1_psuedo_tests as func1_psu
import code_tests.func2.func2_para_flat_tests as func2_pf
import code_tests.func2.func2_para_struc_tests as func2_pst
import code_tests.func2.func2_bullet_flat_tests as func2_bf
import code_tests.func2.func2_bullet_struc_tests as func2_bst
import code_tests.func2.func2_psuedo_tests as func2_psu
import code_tests.func3.func3_para_flat_tests as func3_pf
import code_tests.func3.func3_para_struc_tests as func3_pst
import code_tests.func3.func3_bullet_flat_tests as func3_bf
import code_tests.func3.func3_bullet_struc_tests as func3_bst
import code_tests.func3.func3_psuedo_tests as func3_psu
import code_tests.func4.func4_para_flat_tests as func4_pf
import code_tests.func4.func4_para_struc_tests as func4_pst
import code_tests.func4.func4_bullet_flat_tests as func4_bf
import code_tests.func4.func4_bullet_struc_tests as func4_bst
import code_tests.func4.func4_psuedo_tests as func4_psu
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
import code_tests.func7.func7_para_flat_tests as func7_pf
import code_tests.func7.func7_para_struc_tests as func7_pst
import code_tests.func7.func7_bullet_flat_tests as func7_bf
import code_tests.func7.func7_bullet_struc_tests as func7_bst
import code_tests.func7.func7_psuedo_tests as func7_psu
import code_tests.func8.func8_para_flat_tests as func8_pf
import code_tests.func8.func8_para_struc_tests as func8_pst
import code_tests.func8.func8_bullet_flat_tests as func8_bf
import code_tests.func8.func8_bullet_struc_tests as func8_bst
import code_tests.func8.func8_psuedo_tests as func8_psu
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
import code_tests.func12.func12_para_flat_tests as func12_pf
import code_tests.func12.func12_para_struc_tests as func12_pst
import code_tests.func12.func12_bullet_flat_tests as func12_bf
import code_tests.func12.func12_bullet_struc_tests as func12_bst
import code_tests.func12.func12_psuedo_tests as func12_psu

# ACCESS TO TEST COVERAGE RATIOS
cov_dict = {}
for i in range(1, oi.getNumOfFuncs()+1):
    func_name = "func"+str(i)
    cov_dict[func_name] = coverage.Coverage(data_file="../code_tests/"+func_name+"/.coverage")
    cov_dict[func_name].load()

# ARRAY INDEX MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)

# COVERAGE TEST FAIL RATIOS
func1_fail_ratios = [func1_pf.getFailRatio(), func1_pst.getFailRatio(), func1_bf.getFailRatio(), func1_bst.getFailRatio(), func1_psu.getFailRatio()]
func2_fail_ratios = [func2_pf.getFailRatio(), func2_pst.getFailRatio(), func2_bf.getFailRatio(), func2_bst.getFailRatio(), func2_psu.getFailRatio()]
func3_fail_ratios = [func3_pf.getFailRatio(), func3_pst.getFailRatio(), func3_bf.getFailRatio(), func3_bst.getFailRatio(), func3_psu.getFailRatio()]
func4_fail_ratios = [func4_pf.getFailRatio(), func4_pst.getFailRatio(), func4_bf.getFailRatio(), func4_bst.getFailRatio(), func4_psu.getFailRatio()]
func5_fail_ratios = [func5_pf.getFailRatio(), func5_pst.getFailRatio(), func5_bf.getFailRatio(), func5_bst.getFailRatio(), func5_psu.getFailRatio()]
func6_fail_ratios = [func6_pf.getFailRatio(), func6_pst.getFailRatio(), func6_bf.getFailRatio(), func6_bst.getFailRatio(), func6_psu.getFailRatio()]
func7_fail_ratios = [func7_pf.getFailRatio(), func7_pst.getFailRatio(), func7_bf.getFailRatio(), func7_bst.getFailRatio(), func7_psu.getFailRatio()]
func8_fail_ratios = [func8_pf.getFailRatio(), func8_pst.getFailRatio(), func8_bf.getFailRatio(), func8_bst.getFailRatio(), func8_psu.getFailRatio()]
func9_fail_ratios = [func9_pf.getFailRatio(), func9_pst.getFailRatio(), func9_bf.getFailRatio(), func9_bst.getFailRatio(), func9_psu.getFailRatio()]
func10_fail_ratios = [func10_pf.getFailRatio(), func10_pst.getFailRatio(), func10_bf.getFailRatio(), func10_bst.getFailRatio(), func10_psu.getFailRatio()]
func11_fail_ratios = [func11_pf.getFailRatio(), func11_pst.getFailRatio(), func11_bf.getFailRatio(), func11_bst.getFailRatio(), func11_psu.getFailRatio()]
func12_fail_ratios = [func12_pf.getFailRatio(), func12_pst.getFailRatio(), func12_bf.getFailRatio(), func12_bst.getFailRatio(), func12_psu.getFailRatio()]