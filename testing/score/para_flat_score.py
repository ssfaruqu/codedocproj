import test_info as t
import math

def score_eq(token, leq, cover, fail):
    a, b, c = 0.5, 0.5, 0.5
    score = token*(math.pow(leq, a) + math.pow(cover, b)) + fail
    return score

#logic equiv pass or fail
log_eq = t.func5_le.getPassArr()
#coverage ratio
cover = 1 - (len(t.cov_5.analysis2(morf="../code_tests/func5/func5_para_flat_tests.py")[-2]) / len(t.cov_5.analysis2(morf="../code_tests/func5/func5_para_flat_tests.py")[1]))
#test fail ratio
fail = t.func5_pf.getFailRatio()

print(f"le= {log_eq[t.PF_IDX]}, cover= {cover}, fail= {fail}")
score = score_eq(t.func5_pf_count, log_eq[t.PF_IDX], cover, fail)
print(score)
