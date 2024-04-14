import coverage

# ACCESS TO TEST CASE FAIL RATIOS
import sys

sys.path.insert(0, '../../testing')

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func5_logic_equiv as func5_le
import logic_equiv.func6_logic_equiv as func6_le
import logic_equiv.func9_logic_equiv as func9_le
import logic_equiv.func10_logic_equiv as func10_le
import logic_equiv.func11_logic_equiv as func11_le

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
cov_5.report(show_missing=True)

# PASS_ARR MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)
# INPUT TOKEN COUNTS
func5_pf_count, func6_pf_count, func9_pf_count, func10_pf_count, func11_pf_count = (1366, 423, 1060, 1212, 811)