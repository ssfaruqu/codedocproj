from openai import OpenAI
import re
import os
import argparse
import sys

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 

# list of (prompt, query style) pairs
input = [
("Give only a concise, unstructured one paragraph summary of the following code, which incorporates the function's name and inputs", "para_flat"),
("Give only a concise, structured one paragraph summary of the following code, including a concise section for the function name and summary, input, and return values", "para_struc"),
("Give only a concise, unstructured bullet point summary of the following code, including a point about the function's name and inputs", "bullet_flat"),
("Give only a concise, structured bullet point summary of the following code, including bullet points for the function name and summary, input, and return values", "bullet_struc"),
("Write concise, high-level psuedocode in written English for the following code, which incorporates the function's name and inputs", "psuedo")
]

# constraints for the model so that it produces python code as needed for testing
summ_constraints = ", without any introduction or use of ```:\n"
code_constraints = " Use inputs/outputs with the exact same name and order as in the following summary. Also, do not include any written language or use of ```:\n"

# list of (name, code, length) tuples for each orignal func
functions = []
for i in range(0, oi.getNumOfFuncs()):
    functions.append((oi.getFuncName()[i], oi.getFuncs()[i], oi.getFuncLen()[oi.getFuncName()[i]]))

# send functions to model to generate summaries and functions based off those summaries
def generate_code(input, llm):
    for name, code, len in functions:
        f = open(name+"/"+name+"_"+input[1]+".py", "w")
        t = open(name+"/"+name+"_"+input[1]+".txt", "w")

        client = OpenAI()
        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": input[0]+ summ_constraints + code
                }
            ],
            model=llm,
            max_tokens= len,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )

        summary = completion.choices[0].message.content
        t.write(summary)
        t.close()

        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "user",
                    "content": "Generate only a python function based on the following description." + code_constraints + summary
                }
            ],
            model=llm,
            max_tokens= len,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )

        gen_func = completion.choices[0].message.content
        gen_name = re.findall("def .*\(", gen_func)
        if not gen_name:
            gen_name = re.findall(".* = lambda", gen_func)[0][0:-8]
        else:
            gen_name = gen_name[0][4:-1]
        gen_func = gen_func.replace(gen_name, input[1]+"_"+name)
        print(gen_name,  input[1]+"_"+name)
        f.write(gen_func)
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("llm", help="The LLM model to be used: gpt-3.5-turbo, gpt-4.5-turbo")
    args = parser.parse_args()

    # make function folders if they dont exist
    for i in range(1, oi.getNumOfFuncs()+1):
        fldr = "func"+str(i)
        if not os.path.exists(fldr):
            os.makedirs(fldr)

    # generate code and txt using llm
    llm = args.llm
    for x in input:
        generate_code(x, llm)