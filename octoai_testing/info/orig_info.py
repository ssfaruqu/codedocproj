import re

# INFORMATION ABOUT TESTING FUNCTIONS
num_of_funcs = 5
funcs = []
func_len = dict()
func_name = []

# READ FUNCTIONS FROM FILE
f = open("../funcs_for_testing.py", "r")
post = f.read()
f.close()

# EXTRACT INFORMATION FROM FUNCTIONS
for i in range(2, num_of_funcs+1):
    # seperate functions
    divider = "# test function " + str(i)
    pre, post = post.split(divider)

    # extract info
    funcs.append(pre)
    name = re.findall("def [a-zA-Z0-9]*", pre)[0][4:]
    func_name.append(name)
    func_len[name] = len(pre)
    
    if i == num_of_funcs:
        funcs.append(post)
        name = re.findall("def [a-zA-Z0-9]*", post)[0][4:]
        func_name.append(re.findall("def [a-zA-Z0-9]*", post)[0][4:])
        func_len[name] = len(post)

# returns list of code of all functions
def getFuncs():
    return funcs

# returns dict of lengths(# of chars) of each function
def getFuncLen():
    return func_len

# return total number of functions
def getNumOfFuncs():
    return num_of_funcs

# return list of name of each functions
def getFuncName():
    return func_name