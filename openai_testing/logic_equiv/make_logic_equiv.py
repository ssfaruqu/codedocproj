import test_txt
import argparse
import sys
sys.path.insert(0, '..\..\openai_testing')

import info.orig_info as oi
import info.gen_info as gi

def make_logic_equiv_tests(llm):
    # get func and test case names
    func_names = oi.getFuncName()

    # create original funcs by replacing names in each func
    orig_funcs = oi.getFuncs()
    for i in range(0, oi.getNumOfFuncs()):
        orig_funcs[i] = orig_funcs[i].replace(func_names[i], " orig_"+func_names[i])

    # get test case names
    gen_info = gi.GenInfo(llm)
    test_case_names = gen_info.getTestCaseNames()

    # create a logic equiv test for each func
    for i in range(0, oi.getNumOfFuncs()):
        # create file and write the setup and testing code
        f = open(func_names[i]+"_logic_equiv.py", "w")
        f.write(test_txt.tests[i])

        # write original func
        f.write("\n"+orig_funcs[i])

        # write each of the generated funcs
        for case in test_case_names:
            t = open("../generate/"+llm+"/"+func_names[i]+"/"+func_names[i]+"_"+case+".py", "r")
            func = t.read()
            t.close()
            f.write("\n"+func)

        # write the calls to testing code
        f.write('''\n
# EXECUTE TEST
def try_test(test, test_fail_string, test_pass_string):
    try:
        test()
        print(test_pass_string)
        print("")
        return 1
    except Exception as e:
        print(test_fail_string)
        print(repr(e))
        print("")
        return 0

def getPassArr():
    return pass_arr

print("----- '''+func_names[i]+''' LOGIC EQUIV TESTING -------")
pass_arr = [0,0,0,0,0]
pass_arr[0] = try_test(test_para_flat_'''+func_names[i]+''', "PARA FLAT FAIL", "PARA FLAT PASS")
pass_arr[1] = try_test(test_para_struc_'''+func_names[i]+''', "PARA STRUC FAIL", "PARA STRUC PASS")
pass_arr[2] = try_test(test_bullet_flat_'''+func_names[i]+''', "BULLET FLAT FAIL", "BULLET FLAT PASS")
pass_arr[3] = try_test(test_bullet_struc_'''+func_names[i]+''', "BULLET STRUC FAIL", "BULLET STRUC PASS")
pass_arr[4] = try_test(test_psuedo_'''+func_names[i]+''', "PSUEDO FAIL", "PSUEDO PASS")
''')

    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("llm", help="The LLM model to be used: gpt-3.5-turbo, gpt-4-turbo")
    args = parser.parse_args()
    llm = args.llm
    if llm != "gpt-3.5-turbo" and llm != "gpt-4-turbo":
        print("Selected model not available: Use gpt-3.5-turbo or gpt-4-turbo")
        exit(0)
    
    make_logic_equiv_tests(llm)