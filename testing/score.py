import coverage

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func9_logic_equiv as func9_le

# ACCESS TO TEST CASE FAIL RATIOS
import sys

sys.path.insert(1, '/code_tests/func9')

import code_tests.func9.func9_bullet_flat_tests as func9_bf
import code_tests.func9.func9_bullet_struc_tests as func9_bs
import code_tests.func9.func9_para_flat_tests as func9_pf
import code_tests.func9.func9_para_struc_tests as func9_ps
import code_tests.func9.func9_bullet_flat_tests as func9_bf

# PASS_ARR MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)
# ACCESS TO TEST COVERAGE RATIOS
cov_11 = coverage.Coverage(data_file="code_tests/func9/.coverage")
cov_11.load()
cov_11.report(show_missing=True)
print(len(cov_11.analysis2(morf="code_tests/func9/func9_para_flat_tests.py")[-2]))
print(func9_le.getPassArr())

print(func9_bf.getFailRatio())