from octoai.client import Client
import argparse
import re
import sys
import json

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 
import info.gen_info as gi

prompts = '''
Write python code for just 10 small tests, without creating new functions, for a program with the following description, without any other text or use of ```. 
Wrap each individual test case in the following try-catch structure, without any other text or use of the ` character, and add an extra indent to each line.
No test should be longer than 5 lines, and no string solution should be longer than 50 characters and no integer solution should be longer than 20 digits. 
Furthermore, no test should return a value. You must add an extra indent to each line as though the code was inside a function body,
and test code must have an assert statement and must use only valid syntax:

```
try:
    <test code>
except Exception as e:
    print(f"{repr(e)} on test case <test number>")
    count += 1
```

'''

def generate_code_tests(input, prompt, i):
    names = [oi.getFuncName()[i]]

    for name in names:
        # get summary
        r = open(name+"/"+name+"_"+input+".txt", 'r')
        summary = r.read()
        r.close()

        f = open(name+"/"+name+"_"+input+"_tests.py", "w")

        client = Client()
        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt + '''TESTS:\n''' + summary
                }
            ],
            model="meta-llama-3-70b-instruct",
            max_tokens= 4096,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )
        x = json.dumps(completion.model_dump())
        load_x = json.loads(x)

        tests = load_x['choices'][0]['message']['content']
        #print(tests)
        print(name, input)
        f.write(tests)
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("func", help="Select function: 1-12")
    parser.add_argument("style", help="Select prompt style: 0= para_flat, 1= para_struc, 2= bullet_flat, 3= bullet_struc, 4= psuedo")
    args = parser.parse_args()
    func = int(args.func) - 1
    style = int(args.style)

    if func not in range(0, 13):
        print("Selected invalid func")
        exit(0)
    if style not in range(0, 5):
        print("Selected invalid style")
        exit(0)

    input = gi.getTestCaseNames()[style]

    generate_code_tests(input, prompts, func)