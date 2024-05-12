import sys
sys.path.insert(0, '../../openai_testing')

import info.orig_info as ofi

class GenInfo:
    def __init__(self, llm):
        # INFO ABOUT GENERATED CONTENT
        self.llm = llm
        self.test_case_names = ["para_flat", "para_struc", "bullet_flat", "bullet_struc", "psuedo"]
        self.func_summ_len = dict()

        # get for each func, get a list of its generated summary lengths and add it to dict
        for name in ofi.getFuncName():
            sl = []
            for case in self.test_case_names:
                f = open("../generate/"+llm+"/"+name+"/"+name+"_"+case+".txt")
                txt = f.read()
                f.close()
                sl.append(len(txt))
            self.func_summ_len[name] = sl

    # return dict containing lists of generated function summary lengths (number of chars) for each function
    def getFuncSummLen(self):
        return self.func_summ_len

    # return list of the names of the prompt styles being tested
    def getTestCaseNames(self):
        return self.test_case_names
