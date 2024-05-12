import os
import argparse
import sys
sys.path.insert(0, '..\..\openai_testing')

import info.orig_info as oi 
import info.gen_info as gi

test_case_names = ["para_flat", "para_struc", "bullet_flat", "bullet_struc", "psuedo"]
functions = []
for i in range(0, oi.getNumOfFuncs()):
    functions.append((oi.getFuncName()[i], oi.getFuncs()[i]))

def make_code_tests(llm):
    for name, code in functions:
        for case in test_case_names:
            # write new file for code tests
            f = open(name+"/"+name+"_"+case+"_tests.py", "w")

            #get generated tests
            t = open("../generate/"+llm+"/"+name+"/"+name+"_"+case+"_tests.py", "r")
            tests = t.read()
            print(tests)
            t.close()

            if case == "psuedo":
                cover = "coverage.Coverage()"
            else:
                cover = "coverage.Coverage(data_suffix=True)"

            f.write('''import coverage # pragma: no cover
import numpy as np # pragma: no cover
import math # pragma: no cover
rand_grid = [] # pragma: no cover
rand_body = [] # pragma: no cover
rand_board = [] # pragma: no cover
    ''')

            f.write("\n\n"+code)

            f.write("\ndef "+case+"_test_cases(): # pragma: no cover\n    count = 0\n"+tests+'''\n    print(f"Total failed test cases: {count}")\n    return count\n''')

            f.write('''
def getFailRatio(): # pragma: no cover
    return failed_ratio

cov = '''+cover+''' # pragma: no cover
# start coverage
cov.start() # pragma: no cover

x = '''+ case + '''_test_cases() # pragma: no cover
if type(x) != int: # pragma: no cover
    failed_ratio = 1.0 # pragma: no cover
else: # pragma: no cover
    failed_ratio = x/10 # pragma: no cover

# stop coverage
cov.stop() # pragma: no cover
# make report
cov.save() # pragma: no cover
cov.combine() # pragma: no cover
cov.save() # pragma: no cover
# load report
cov.load() # pragma: no cover

# print report
coverage_percentage = cov.report() * 0.01 # pragma: no cover
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
    
     # make function folders if they dont exist
    for i in range(1, oi.getNumOfFuncs()+1):
        fldr = "func"+str(i)
        if not os.path.exists(fldr):
            os.makedirs(fldr)
            f = open(fldr+"/"+fldr+"_tests.bat", "w")
            p = open(fldr+"/"+fldr+"_tests.sh", "w")

            f.write("python ./"+fldr+"_para_flat_tests.py\n")
            f.write("python ./"+fldr+"_para_struc_tests.py\n")
            f.write("python ./"+fldr+"_bullet_flat_tests.py\n")
            f.write("python ./"+fldr+"_bullet_struc_tests.py\n")
            f.write("python ./"+fldr+"_psuedo_tests.py\n")
            f.close()

            p.write("python ./"+fldr+"_para_flat_tests.py\n")
            p.write("python ./"+fldr+"_para_struc_tests.py\n")
            p.write("python ./"+fldr+"_bullet_flat_tests.py\n")
            p.write("python ./"+fldr+"_bullet_struc_tests.py\n")
            p.write("python ./"+fldr+"_psuedo_tests.py\n")
            p.close()


    make_code_tests(llm)