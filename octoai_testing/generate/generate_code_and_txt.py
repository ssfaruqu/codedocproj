from octoai.client import Client
import json
import re
import sys

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 

# list of (prompt, query style) pairs
input = [
("Give only a concise, unstructured one paragraph summary of the following code, which incorporates the function's name and inputs", "para_flat"),
("Give only a concise, structured one paragraph summary of the following code, including a concise section for the function name and summary, input, and return values", "para_struc"),
("Give only a concise, unstructured bullet point summary of the following code, including a point about the function's name and inputs", "bullet_flat"),
("Give only a concise, structured bullet point summary of the following code, including bullet points for the function name and summary, input, and return values", "bullet_struc"),
("Write high-level psuedocode for the following code, which incorporates the function's name and inputs", "psuedo")
]

# constraints for the model so that it produces python code as needed for testing
summ_constraints = ", without any introduction or use of ```:\n"
code_constraints = " Use inputs/outputs with the exact same name and order as in the following summary. Also, do not include any written language or use of ```:\n"

# list of (name, code, length) tuples for each orignal func
functions = []
for i in range(0, oi.getNumOfFuncs()):
    functions.append((oi.getFuncName()[i], oi.getFuncs()[i], oi.getFuncLen()[oi.getFuncName()[i]]))

# send functions to model to generate summaries and functions based off those summaries
def generate_code(input):
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
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
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

for x in input:
    generate_code(x)