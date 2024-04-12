import hypothesis
import argparse
from hypothesis import given, strategies as st

# Takes text to be optimized, and returns same-order list of the operation statements
def get_expression_list(s):
    filtered_str = s.replace(" ", "").replace("\n", "")
    expression_list = filtered_str.split(";")
    expression_list = [expr for expr in expression_list if expr]
    return expression_list

def orig_func7(f):
    f = open(f)
    s = f.read()
    f.close()

    pre = s.split("// Start optimization range")[0]
    post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    global_counter = 0
    H = {}
    var_number = {}
    to_initialize = []
    replaced = 0
    expression_list = get_expression_list(to_optimize)
    lvn_expression_list = []

    for expr in expression_list:
        lhs = expr[0]
        left_val = expr[2]
        op = expr[3]
        right_val = expr[4]

        lvn_left_val = ""
        lvn_right_val = ""
        lvn_rhs = ""

        if left_val not in var_number:
            lvn_left_val = left_val + str(global_counter)
            var_number[left_val] = str(global_counter)
            to_initialize.append(lvn_left_val) 
            global_counter += 1
        else:
            lvn_left_val = left_val + var_number[left_val]

        if right_val not in var_number:
            lvn_right_val = right_val + str(global_counter)
            var_number[right_val] = str(global_counter)
            to_initialize.append(lvn_right_val)  
            global_counter += 1
        else:
            lvn_right_val = right_val + var_number[right_val]

        if op == "+" and (lvn_right_val < lvn_left_val):
            lvn_rhs = lvn_right_val + " " + op + " " + lvn_left_val
        else:
            lvn_rhs = lvn_left_val + " " + op + " " + lvn_right_val

        lvn_lhs = lhs + str(global_counter)
        var_number[lhs] = str(global_counter)
        global_counter += 1

        if lvn_rhs in H:
            opt_var = H[lvn_rhs]
            replaced += 1
            lvn_rhs = opt_var

        else:
            H[lvn_rhs] = lvn_lhs

        lvn_expr = lvn_lhs + " = " + lvn_rhs
        lvn_expression_list.append(lvn_expr)

    print(pre)

    for var in to_initialize:
        print("    double " + var + " = " + var[0] + ";")

    for expr in lvn_expression_list:
        print("    double " + expr + ";")

    for key, val in var_number.items():
        print("    " + key + " = " + key + val + ";")

    print(post)

    print("// replaced: " + str(replaced))
    return replaced

def para_flat_func7(source_file):
    """
    Performs basic optimizations on a given source file containing C-like code.

    Args:
    - source_file (str): The path to the source file.

    Returns:
    - str: The optimized code.
    - int: The number of replacements made.
    """

    def apply_optimization(section):
        """
        Applies optimization to a given section of code.

        Args:
        - section (str): The code section to be optimized.

        Returns:
        - str: The optimized code section.
        - int: The number of replacements made.
        """
        replacements = 0
        # Implement basic optimization logic here (e.g., common subexpression elimination)
        # For demonstration purposes, let's assume replacing repetitive expressions with temporary variables
        optimized_section = section  # Placeholder for optimized section
        
        # Example of optimization (replace repetitive expressions with temporary variables)
        expressions = {}  # Dictionary to store expressions and their corresponding temporary variables
        
        # Split the section into lines and process each line
        lines = optimized_section.split('\n')
        for i, line in enumerate(lines):
            # Assuming expressions are assigned to variables in the format: variable = expression;
            parts = line.split('=')
            if len(parts) == 2:
                variable = parts[0].strip()
                expression = parts[1].strip().rstrip(';')
                if expression in expressions:
                    # Replace repetitive expression with temporary variable
                    temp_variable = expressions[expression]
                    lines[i] = f"{variable} = {temp_variable};"
                    replacements += 1
                else:
                    # Add new expression to the dictionary
                    expressions[expression] = variable
        
        # Rejoin the lines to form the optimized section
        optimized_section = '\n'.join(lines)
        
        return optimized_section, replacements

    # Read the source file
    with open(source_file, 'r') as file:
        source_code = file.read()

    # Split the code into sections based on optimization ranges (if applicable)
    # For demonstration purposes, let's assume the entire code is one section
    optimization_ranges = [(0, len(source_code))]  # Single section covering the entire code

    # Apply optimization to each section
    total_replacements = 0
    optimized_code = ""
    for start, end in optimization_ranges:
        section = source_code[start:end]
        optimized_section, replacements = apply_optimization(section)
        optimized_code += optimized_section
        total_replacements += replacements

    return optimized_code, total_replacements

def para_struc_func7(f):
    """
    Performs basic optimizations on a given source file containing C-like code.

    Args:
    - f (str): The file path to the source file.

    Prints:
    - The optimized version of the input code.
    - The number of expressions replaced during optimization.
    """

    def apply_optimization(section):
        """
        Applies optimization to a given section of code.

        Args:
        - section (str): The code section to be optimized.

        Returns:
        - str: The optimized code section.
        - int: The number of replacements made.
        """
        replacements = 0
        # Implement basic optimization logic here (e.g., common subexpression elimination)
        # For demonstration purposes, let's assume replacing repetitive expressions with temporary variables
        optimized_section = section  # Placeholder for optimized section
        
        # Example of optimization (replace repetitive expressions with temporary variables)
        expressions = {}  # Dictionary to store expressions and their corresponding temporary variables
        
        # Split the section into lines and process each line
        lines = optimized_section.split('\n')
        for i, line in enumerate(lines):
            # Assuming expressions are assigned to variables in the format: variable = expression;
            parts = line.split('=')
            if len(parts) == 2:
                variable = parts[0].strip()
                expression = parts[1].strip().rstrip(';')
                if expression in expressions:
                    # Replace repetitive expression with temporary variable
                    temp_variable = expressions[expression]
                    lines[i] = f"{variable} = {temp_variable};"
                    replacements += 1
                else:
                    # Add new expression to the dictionary
                    expressions[expression] = variable
        
        # Rejoin the lines to form the optimized section
        optimized_section = '\n'.join(lines)
        
        return optimized_section, replacements

    # Read the source file
    with open(f, 'r') as file:
        source_code = file.read()

    # Split the code into sections based on optimization ranges (if applicable)
    # For demonstration purposes, let's assume the entire code is one section
    optimization_ranges = [(0, len(source_code))]  # Single section covering the entire code

    # Apply optimization to each section
    total_replacements = 0
    optimized_code = ""
    for start, end in optimization_ranges:
        section = source_code[start:end]
        optimized_section, replacements = apply_optimization(section)
        optimized_code += optimized_section
        total_replacements += replacements

    # Print the optimized code
    print("Optimized Code:")
    print(optimized_code)
    print("Number of Replacements Made:", total_replacements)
    return total_replacements

def bullet_flat_func7(f):
    # Open the file and read its contents
    with open(f, 'r') as file:
        s = file.read()

    # Close the file
    file.close()

    # Split the string into parts based on optimization comments
    pre, to_optimize, post = s.split("# OPTIMIZE HERE") #ORIGINALLY GENERATED

    #FROM orig_func7
    # pre = s.split("// Start optimization range")[0]
    # post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    # to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # Initialize variables
    global_counter = 0 #UNUSED VARIABLES
    H = ""
    var_number = 0     #UNUSED VARIABLES
    to_initialize = []
    replaced = {}

    # Retrieve expressions to optimize
    expression_list = to_optimize.strip().split('\n')

    # List to store expressions after applying optimization
    lvn_expression_list = []

    # Iterate over each expression in the list of expressions to optimize
    for expression in expression_list:
        # Process each expression to apply optimization
        # Update the expression using the optimization technique
        # Keep track of replaced expressions and their occurrences
        optimized_expression = expression  # Placeholder for optimization process
        replaced[expression] = replaced.get(expression, 0) + 1

        # Append the optimized expression to the list
        lvn_expression_list.append(optimized_expression)

    # Print part of the code before the optimization range
    print(pre)

    # Print declarations to initialize variables needed for optimization
    print(H)
    for var in to_initialize:
        print(var)

    # Print optimized expressions
    for expression in lvn_expression_list:
        print(expression)

    # Print assignments to update variables with optimized expressions
    for var in to_initialize:
        print(var)

    # Print part of the code after the optimization range
    print(post)

    # Print the number of expressions replaced during optimization
    print("Number of expressions replaced:", len(replaced))
    return replaced

def bullet_struc_func7(f):
    # Open the file and read its contents
    with open(f, 'r') as file:
        s = file.read()

    # Close the file
    file.close()

    # Split the string into parts based on optimization comments
    pre, to_optimize, post = s.split("# OPTIMIZE HERE") #ORIGINALLY GENERATED
    
    #FROM orig_func7
    # pre = s.split("// Start optimization range")[0]
    # post = s.split("// Start optimization range")[1].split("// End optimization range")[1]
    # to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # Initialize variables
    global_counter = 0    #UNUSED VARIABLES
    H = ""
    var_number = 0        #UNUSED VARIABLES
    to_initialize = []
    replaced = {}

    # Retrieve expressions to optimize
    expression_list = to_optimize.strip().split('\n')

    # List to store expressions after applying optimization
    lvn_expression_list = []

    # Iterate over each expression in the list of expressions to optimize
    for expression in expression_list:
        # Process each expression to apply optimization
        # Update the expression using the optimization technique
        # Keep track of replaced expressions and their occurrences
        optimized_expression = expression  # Placeholder for optimization process
        replaced[expression] = replaced.get(expression, 0) + 1

        # Append the optimized expression to the list
        lvn_expression_list.append(optimized_expression)

    # Print part of the code before the optimization range
    print(pre)

    # Print declarations to initialize variables needed for optimization
    print(H)
    for var in to_initialize:
        print(var)

    # Print optimized expressions
    for expression in lvn_expression_list:
        print(expression)

    # Print assignments to update variables with optimized expressions
    for var in to_initialize:
        print(var)

    # Print part of the code after the optimization range
    print(post)

    # Print the number of expressions replaced during optimization
    print("Number of expressions replaced:", len(replaced))
    return replaced

def psuedo_func7(f):
    # Open file f
    with open(f, 'r') as file:
        # Read contents of f into s
        s = file.read()

    # Split s before "// Start optimization range" to get pre
    pre = s.split("// Start optimization range")[0]

    # Split s after "// Start optimization range" and before "// End optimization range" to get to_optimize
    to_optimize = s.split("// Start optimization range")[1].split("// End optimization range")[0]

    # Split s after "// End optimization range" to get post
    post = s.split("// End optimization range")[1]

    # Initialize global_counter to 0
    global_counter = 0

    # Initialize H as an empty dictionary
    H = {}

    # Initialize var_number as an empty dictionary
    var_number = {}

    # Initialize to_initialize as an empty list
    to_initialize = []

    # Initialize replaced to 0
    replaced = 0

    # Initialize expression_list by calling get_expression_list(to_optimize)
    expression_list = get_expression_list(to_optimize)

    # Initialize lvn_expression_list as an empty list
    lvn_expression_list = []

    # Iterate over each expression in expression_list
    for expression in expression_list:
        # Extract lhs, left_val, op, right_val from expression
        lhs, left_val, op, right_val = expression # PSEUDO WAS VAGUE IN HOW TO EXTRACT FROM expression

        #FROM orig_func7
        # lhs = expression[0]
        # left_val = expression[2]
        # op = expression[3]
        # right_val = expression[4]

        # Initialize lvn_left_val, lvn_right_val, lvn_rhs as empty strings
        lvn_left_val, lvn_right_val, lvn_rhs = "", "", ""

        # If left_val is not in var_number
        if left_val not in var_number:
            lvn_left_val = left_val + str(global_counter)
            var_number[left_val] = str(global_counter)
            to_initialize.append(lvn_left_val)
            global_counter += 1
        else:
            lvn_left_val = left_val + var_number[left_val]

        # If right_val is not in var_number
        if right_val not in var_number:
            lvn_right_val = right_val + str(global_counter)
            var_number[right_val] = str(global_counter)
            to_initialize.append(lvn_right_val)
            global_counter += 1
        else:
            lvn_right_val = right_val + var_number[right_val]

        # Construct lvn_rhs based on operator precedence
        if op == "+" and lvn_right_val < lvn_left_val:
            lvn_rhs = lvn_right_val + op + lvn_left_val
        else:
            lvn_rhs = lvn_left_val + op + lvn_right_val

        # Concatenate lhs with str(global_counter) to get lvn_lhs
        lvn_lhs = lhs + str(global_counter)
        var_number[lhs] = str(global_counter)
        global_counter += 1

        # If lvn_rhs is in H
        if lvn_rhs in H:
            opt_var = H[lvn_rhs]
            replaced += 1
            lvn_rhs = opt_var
        else:
            H[lvn_rhs] = lvn_lhs

        # Construct lvn_expr and append to lvn_expression_list
        lvn_expr = lvn_lhs + " = " + lvn_rhs
        lvn_expression_list.append(lvn_expr)

    # Print pre
    print(pre)

    # Iterate over each variable in to_initialize
    for var in to_initialize:
        print("    double " + var + " = " + var[0] + ";")

    # Iterate over each expression in lvn_expression_list
    for expr in lvn_expression_list:
        print("    double " + expr + ";")

    # Iterate over key, val pairs in var_number
    for key, val in var_number.items():
        print("    " + key + " = " + key + val + ";")

    # Print post
    print(post)

    # Print "// replaced: " + str(replaced)
    print("// replaced: " + str(replaced))
    return replaced


# if you run this file, you can give it one of the python test cases
# in the test_cases/ directory.
# see solutions.py for what to expect for each test case.

#FAIL
def test_para_func7():
    parser = argparse.ArgumentParser()
    parser.add_argument("cppfile", help="The cpp file to be analyzed")
    args = parser.parse_args()

    orig = orig_func7(args.cppfile)
    code, flat = para_flat_func7(args.cppfile)
    struc = para_struc_func7(args.cppfile)
    
    try:
        assert orig == flat == struc
    except:
        print(f"orig= {orig}, flat= {flat}, struc= {struc}")
    
#FUNCTION DOESN"T WORK; WHEN INCORRECT PART REPLACED, FAILED
def test_bullet_func7():
    parser = argparse.ArgumentParser()
    parser.add_argument("cppfile", help="The cpp file to be analyzed")
    args = parser.parse_args()

    orig = orig_func7(args.cppfile)
    flat = bullet_flat_func7(args.cppfile)
    struc = bullet_struc_func7(args.cppfile)
    
    try:
        assert orig == flat == struc
    except:
        print("NOT MATCHING")
        print(f"orig= {orig}, flat= {flat}, struc= {struc}")

#FUNCTION DOESN"T WORK; WHEN INCORRECT PART REPLACED, FAILED
def test_psuedo_func7():
    parser = argparse.ArgumentParser()
    parser.add_argument("cppfile", help="The cpp file to be analyzed")
    args = parser.parse_args()

    orig = orig_func7(args.cppfile)
    psuedo = psuedo_func7(args.cppfile)
    
    try:
        assert orig == psuedo
    except:
        print("NOT MATCHING")
        print(f"orig= {orig}, psuedo= {psuedo}")

test_psuedo_func7()