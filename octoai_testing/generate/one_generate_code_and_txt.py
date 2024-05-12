from octoai.client import Client
import re
import os
import argparse
import sys
import json

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 

# list of (prompt, query style) pairs
input = [
[
("Give only a concise, unstructured one paragraph summary of the following code, which incorporates the function's name and input names", "para_flat"),
("Give only a concise, structured one paragraph summary of the following code, including a concise section for the function name and summary, input, and return values", "para_struc"),
("Give only a concise, unstructured bullet point summary of the following code, including a point about the function's name and input names", "bullet_flat"),
("Give only a concise, structured bullet point summary of the following code, including bullet points for the function name and summary, input, and return values", "bullet_struc"),
("Write concise, high-level psuedocode in written English for the following code, which incorporates the function's name and inputs", "psuedo")
],
[
("Give only an unstructured summary of the following code within 5-sentences, which incorporates the function's name and inputs", "para_flat"),
("Give only a structured summary of the following code within 5-sentences, including a concise section for the function name and summary, input, and return values", "para_struc"),
("Give only an unstructured bullet point summary of the following code within 10-bullets, including a point about the function's name and inputs", "bullet_flat"),
("Give only a structured bullet point summary of the following code within 10-bullets, including bullet points for the function name and summary, input, and return values", "bullet_struc"),
("Write concise, high-level psuedocode in written English for the following code within 20 lines, which incorporates the function's name and inputs", "psuedo")
],
[
("Give only a concise, unstructured one paragraph summary of the following code, including its preconditions and postconditions, which incorporates the function's name and input names", "para_flat"),
("Give only a concise, structured one paragraph summary of the following code, including concise sections for the function name and summary, preconditions, and postconditions. Do not use bullet points.", "para_struc"),
("Give only a concise, unstructured bullet point summary of the following code, including its preconditions and postconditions, which incorporates points about the function's name and input names", "bullet_flat"),
("Give only a concise, structured bullet point summary of the following code, including concise sections for the function name and summary, preconditions, and postconditions", "bullet_struc"),
("Write concise, high-level psuedocode in written English for the following code, which incorporates the function's name, preconditions, and postconditions", "psuedo")
]
]

# constraints for the model so that it produces python code as needed for testing
summ_constraints = ", without any introduction or use of ```:\n"
code_constraints = " Use inputs/outputs with the exact same name and order as in the following summary. Also, do not include any written language or use of ``` or any other non-python syntax:\n"

# send functions to model to generate summaries and functions based off those summaries
def generate_code(input, i):
    functions = []
    functions.append((oi.getFuncName()[i], oi.getFuncs()[i], oi.getFuncLen()[oi.getFuncName()[i]]))

    for name, code, len in functions:
        f = open(name+"/"+name+"_"+input[1]+".py", "w")
        t = open(name+"/"+name+"_"+input[1]+".txt", "w")

        client = Client()
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
            model="meta-llama-3-70b-instruct",
            max_tokens= len,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )

        x = json.dumps(completion.model_dump())
        load_x = json.loads(x)

        summary = load_x['choices'][0]['message']['content']
        t.write(summary)
        t.close()

        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "user",
                    "content": "Generate only a python function based on the following description." + code_constraints + summary
                }
            ],
            model="meta-llama-3-70b-instruct",
            max_tokens= len,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )

        x = json.dumps(completion.model_dump())
        load_x = json.loads(x)

        gen_func = load_x['choices'][0]['message']['content']
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
    parser.add_argument("input_type", help="Select input type: 0= normal, 1= structural size limit, 2= pre/postconditon")
    parser.add_argument("func", help="Select function: 1-12")
    parser.add_argument("style", help="Select prompt style: 0= para_flat, 1= para_struc, 2= bullet_flat, 3= bullet_struc, 4= psuedo")
    args = parser.parse_args()
    input_type = int(args.input_type)
    func = int(args.func) - 1
    style = int(args.style)

    if input_type not in range(0, 3):
        print("Selected invalid input type")
        exit(0)
    if func not in range(0, 13):
        print("Selected invalid func")
        exit(0)
    if style not in range(0, 5):
        print("Selected invalid style")
        exit(0)

    # make function folders if they dont exist
    for i in range(1, oi.getNumOfFuncs()+1):
        fldr = "/func"+str(i)
        if not os.path.exists(fldr):
            os.makedirs(fldr)
    
    # generate code and txt using llm
    prompts = input[input_type]
    generate_code(prompts[style], func)