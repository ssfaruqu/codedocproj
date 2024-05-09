import sys
sys.path.insert(0, '../../octoai_testing')

import info.orig_info as ofi

# INFO ABOUT GENERATED CONTENT
test_case_names = ["para_flat", "para_struc", "bullet_flat", "bullet_struc", "psuedo"]
func_summ_len = dict()

# get for each func, get a list of its generated summary lengths and add it to dict
for name in ofi.getFuncName():
    sl = []
    for case in test_case_names:
        f = open("../generate/"+name+"/"+name+"_"+case+".txt")
        txt = f.read()
        f.close()
        sl.append(len(txt))
    func_summ_len[name] = sl

# return dict containing lists of generated function summary lengths (number of chars) for each function
def getFuncSummLen():
    return func_summ_len

# return list of the names of the prompt styles being tested
def getTestCaseNames():
    return test_case_names
