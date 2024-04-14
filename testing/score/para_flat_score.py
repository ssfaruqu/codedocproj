import coverage

# ACCESS TO TEST CASE FAIL RATIOS
import sys

sys.path.insert(0, '../../testing')

# ACCESS TO LOGICAL EQUIVALENCE TESTS
import logic_equiv.func5_logic_equiv as func5_le

import code_tests.func5.func5_para_flat_tests as func5_pf
import code_tests.func5.func5_para_struc_tests as func5_ps
import code_tests.func5.func5_bullet_flat_tests as func5_bf
import code_tests.func5.func5_bullet_struc_tests as func5_bs
import code_tests.func5.func5_psuedo_tests as func5_bf

# ACCESS TO TEST COVERAGE RATIOS
cov_11 = coverage.Coverage(data_file="../code_tests/func5/.coverage")
cov_11.load()
cov_11.report(show_missing=True)

# PASS_ARR MACROS
PF_IDX, PST_IDX, BF_IDX, BST_IDX, PSU_IDX = (0,1,2,3,4)
# INPUT TOKEN COUNTS
f5_count, f6_count, f9_count, f10_count, f11_count = (1366, 423, 1060, 1212, 811)

#logic equiv pass or fail
log_eq = func5_le.getPassArr()
#coverage ratio
cover = 1 - (len(cov_11.analysis2(morf="../code_tests/func5/func5_para_flat_tests.py")[-2]) / len(cov_11.analysis2(morf="../code_tests/func5/func5_para_flat_tests.py")[1]))
#test fail ratio
fail = func5_pf.getFailRatio()

print(f"le= {log_eq[PF_IDX]}, cover= {cover}, fail= {fail}")
score = (f5_count)*(log_eq[PF_IDX] + cover*fail)
print(score)
