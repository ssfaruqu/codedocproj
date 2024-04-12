import coverage

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func6_logic_equiv as func6_le

# ACCESS TO TEST CASE FAIL RATIOS
import sys

sys.path.insert(1, '/code_tests/func6')

import code_tests.func6.func6_bullet_flat_tests as func6_bf
import code_tests.func6.func6_bullet_struc_tests as func6_bs
import code_tests.func6.func6_para_flat_tests as func6_pf
import code_tests.func6.func6_para_struc_tests as func6_ps
import code_tests.func6.func6_bullet_flat_tests as func6_bf

# PASS_ARR MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)
# ACCESS TO TEST COVERAGE RATIOS
cov_11 = coverage.Coverage(data_file="code_tests/func6/.coverage")
cov_11.load()
cov_11.report(show_missing=True)
print(len(cov_11.analysis2(morf="code_tests/func6/func6_para_flat_tests.py")[-2]) / len(cov_11.analysis2(morf="code_tests/func6/func6_para_flat_tests.py")[1]))
print(func6_le.getPassArr())

print(func6_bf.getFailRatio())