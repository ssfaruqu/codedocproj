import test_info as t

# REMEMBER TO MAKE SURE EACH COVERAGE FILE EXISTS FOR EACH OF THE FUNCTIONS IN code_tests
# YOU CAN RUN run_code_tests.sh TO DO SO, OR RUN THE *.bat FILE IN EACH DIR INDIVIDUALLY

def summary_scores(func_name, log_eq, cov, fail):
    para_flat = "../code_tests/" +func_name+"/"+func_name+"_para_flat_tests.py"
    para_struc = "../code_tests/" +func_name+"/"+func_name+"_para_struc_tests.py"
    bullet_flat = "../code_tests/" +func_name+"/"+func_name+"_bullet_flat_tests.py"
    bullet_struc = "../code_tests/" +func_name+"/"+func_name+"_bullet_struc_tests.py"
    psuedo = "../code_tests/" +func_name+"/"+func_name+"_psuedo_tests.py"

    cover = 1 - (len(cov.analysis2(morf=para_flat)[-2]) / len(cov.analysis2(morf=para_flat)[1]))
    print("PARA FLAT")
    t.print_score(func_name, log_eq[t.PF_IDX], cover, fail[t.PF_IDX], t.PF_IDX)

    cover = 1 - (len(cov.analysis2(morf=para_struc)[-2]) / len(cov.analysis2(morf=para_struc)[1]))
    print("PARA STRUC")
    t.print_score(func_name, log_eq[t.PST_IDX], cover, fail[t.PST_IDX], t.PST_IDX)

    cover = 1 - (len(cov.analysis2(morf=bullet_flat)[-2]) / len(cov.analysis2(morf=bullet_flat)[1]))
    print("BULLET FLAT")
    t.print_score(func_name, log_eq[t.BF_IDX], cover, fail[t.BF_IDX], t.BF_IDX)

    cover = 1 - (len(cov.analysis2(morf=bullet_struc)[-2]) / len(cov.analysis2(morf=bullet_struc)[1]))
    print("BULLET STRUC")
    t.print_score(func_name, log_eq[t.BST_IDX], cover, fail[t.BST_IDX], t.BST_IDX)

    cover = 1 - (len(cov.analysis2(morf=psuedo)[-2]) / len(cov.analysis2(morf=psuedo)[1]))
    print("PSUEDO")
    t.print_score(func_name, log_eq[t.PSU_IDX], cover, fail[t.PSU_IDX], t.PSU_IDX)

print("------------------------------------------ FUNC 5 ------------------------------------------------>")
summary_scores("func5", t.func5_le.getPassArr(), t.cov_5, t.func5_fail_ratios)

print("------------------------------------------ FUNC 6 ------------------------------------------------>")
summary_scores("func6", t.func6_le.getPassArr(), t.cov_6, t.func6_fail_ratios)

print("------------------------------------------ FUNC 9 ------------------------------------------------>")
summary_scores("func9", t.func9_le.getPassArr(), t.cov_9, t.func9_fail_ratios)

print("------------------------------------------ FUNC 10 ----------------------------------------------->")
summary_scores("func10", t.func10_le.getPassArr(), t.cov_10, t.func10_fail_ratios)

print("------------------------------------------ FUNC 11 ----------------------------------------------->")
summary_scores("func11", t.func11_le.getPassArr(), t.cov_11, t.func11_fail_ratios)