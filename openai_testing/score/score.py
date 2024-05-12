import test_info as t
from test_info import math as math
from test_info import gi as gi
from test_info import oi as oi

#------------------- CONNECTING TO GOOGLE SPREADSHEET TO COLLECT DATA ---------------------------
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credits.json",scope)
client = gspread.authorize(creds)

#-----------------------------------------------------------------------------------------------

# Performs equation
def score_eq(name, leq, cover, fail, prompt_style):
    a, b, c = 5, 1, 1
    gen_tok = gen_info.getFuncSummLen()[name][prompt_style]
    orig_tok = oi.getFuncLen()[name]
    score = (a*leq + 0.35*(1 - math.pow(fail, b)) + 0.65*math.pow(cover, c))/ (gen_tok / orig_tok)
    return score

# Calls and prints equation plus input info
def print_score(name, leq, cover, fail, prompt_style, gen_info):
    print(f"leq_bin= {leq}, cover_ratio= {cover}, fail_ratio= {fail}, gen_tok= {gen_info.getFuncSummLen()[name][prompt_style]},  orig_tok= {oi.getFuncLen()[name]}")
    score = score_eq(name, leq, cover, fail, prompt_style)
    print(score)

    # add data to spreadsheet
    row = [name, gen_info.getTestCaseNames()[prompt_style], score, oi.getFuncLen()[name], gen_info.getFuncSummLen()[name][prompt_style], (gen_info.getFuncSummLen()[name][prompt_style]/oi.getFuncLen()[name]), leq, cover, fail]
    sheet.append_row(row)

    return score

# REMEMBER TO MAKE SURE EACH COVERAGE FILE EXISTS FOR EACH OF THE FUNCTIONS IN code_tests
# YOU CAN RUN run_code_tests.sh TO DO SO, OR RUN THE *.bat FILE IN EACH DIR INDIVIDUALLY

def summary_scores(func_name, log_eq, cov, fail, gen_info):
    para_flat = "../code_tests/" +func_name+"/"+func_name+"_para_flat_tests.py"
    para_struc = "../code_tests/" +func_name+"/"+func_name+"_para_struc_tests.py"
    bullet_flat = "../code_tests/" +func_name+"/"+func_name+"_bullet_flat_tests.py"
    bullet_struc = "../code_tests/" +func_name+"/"+func_name+"_bullet_struc_tests.py"
    psuedo = "../code_tests/" +func_name+"/"+func_name+"_psuedo_tests.py"

    cover = 1 - (len(cov.analysis2(morf=para_flat)[-2]) / len(cov.analysis2(morf=para_flat)[1]))
    print("PARA FLAT")
    print_score(func_name, log_eq[t.PF_IDX], cover, fail[t.PF_IDX], t.PF_IDX, gen_info)

    cover = 1 - (len(cov.analysis2(morf=para_struc)[-2]) / len(cov.analysis2(morf=para_struc)[1]))
    print("PARA STRUC")
    print_score(func_name, log_eq[t.PST_IDX], cover, fail[t.PST_IDX], t.PST_IDX, gen_info)

    cover = 1 - (len(cov.analysis2(morf=bullet_flat)[-2]) / len(cov.analysis2(morf=bullet_flat)[1]))
    print("BULLET FLAT")
    print_score(func_name, log_eq[t.BF_IDX], cover, fail[t.BF_IDX], t.BF_IDX, gen_info)

    cover = 1 - (len(cov.analysis2(morf=bullet_struc)[-2]) / len(cov.analysis2(morf=bullet_struc)[1]))
    print("BULLET STRUC")
    print_score(func_name, log_eq[t.BST_IDX], cover, fail[t.BST_IDX], t.BST_IDX, gen_info)

    cover = 1 - (len(cov.analysis2(morf=psuedo)[-2]) / len(cov.analysis2(morf=psuedo)[1]))
    print("PSUEDO")
    print_score(func_name, log_eq[t.PSU_IDX], cover, fail[t.PSU_IDX], t.PSU_IDX, gen_info)

if __name__ == "__main__":
    parser = t.argparse.ArgumentParser()
    parser.add_argument("llm", help="The LLM model to be used: gpt-3.5-turbo, gpt-4-turbo")
    args = parser.parse_args()
    llm = args.llm
    if llm != "gpt-3.5-turbo" and llm != "gpt-4-turbo":
        print("Selected model not available: Use gpt-3.5-turbo or gpt-4-turbo")
        exit(0)
    
    if llm == "gpt-3.5-turbo":
        sheet_num = 0
    else:
        sheet_num = 2
    
    sheet = client.open("CodeDocProj").get_worksheet(sheet_num)
    categories = ["func name", "prompt style",  "score", "orig tok", "gen tok", "tok ratio", "leq_bin", "coverage ratio", "fail ratio"]
    sheet.append_row(categories)

    gen_info = gi.GenInfo(llm)

    print("------------------------------------------ FUNC 1 ------------------------------------------------>")
    summary_scores("func1", t.func1_le.getPassArr(), t.cov_dict["func1"], t.func1_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 2 ------------------------------------------------>")
    summary_scores("func2", t.func2_le.getPassArr(), t.cov_dict["func2"], t.func2_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 3 ------------------------------------------------>")
    summary_scores("func3", t.func3_le.getPassArr(), t.cov_dict["func3"], t.func3_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 4 ------------------------------------------------>")
    summary_scores("func4", t.func4_le.getPassArr(), t.cov_dict["func4"], t.func4_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 5 ------------------------------------------------>")
    summary_scores("func5", t.func5_le.getPassArr(), t.cov_dict["func5"], t.func5_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 6 ------------------------------------------------>")
    summary_scores("func6", t.func6_le.getPassArr(), t.cov_dict["func6"], t.func6_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 7 ------------------------------------------------>")
    summary_scores("func7", t.func7_le.getPassArr(), t.cov_dict["func7"], t.func7_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 8 ------------------------------------------------>")
    summary_scores("func8", t.func8_le.getPassArr(), t.cov_dict["func8"], t.func8_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 9 ------------------------------------------------>")
    summary_scores("func9", t.func9_le.getPassArr(), t.cov_dict["func9"], t.func9_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 10 ----------------------------------------------->")
    summary_scores("func10", t.func10_le.getPassArr(), t.cov_dict["func10"], t.func10_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 11 ----------------------------------------------->")
    summary_scores("func11", t.func11_le.getPassArr(), t.cov_dict["func11"], t.func11_fail_ratios, gen_info)

    print("------------------------------------------ FUNC 12 ------------------------------------------------>")
    summary_scores("func12", t.func12_le.getPassArr(), t.cov_dict["func12"], t.func12_fail_ratios, gen_info)