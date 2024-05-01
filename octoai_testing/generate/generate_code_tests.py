from octoai.client import Client
import json
import re
import sys

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 

names  = oi.getFuncName()
input = [
    "para_flat",
    "para_struc",
    "bullet_flat",
    "bullet_struc",
    "psuedo"
]

def generate_code_tests(input):
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
                    "content": '''
Write python code for just 10 tests, without creating new functions, for a program with the following description, without any other text or use of ```. 
Wrap these test cases in the following try-catch structure, without any other text or use of ```::
```
try:
            <test code>
except Exception as e:
            print(f"{repr(e)} on test case <test number>")
            count += 1
```

TESTS:\n''' + summary
                }
            ],
            model="meta-llama-3-70b-instruct",
            max_tokens= 2048,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )

        x = json.dumps(completion.model_dump())
        load_x = json.loads(x)

        tests = load_x['choices'][0]['message']['content']
        #print(tests)

        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": '''
Wrap these test cases in the following try-catch structure, without any other text or use of ```, and add an extra indent each line:
```
try:
            <test code>
except Exception as e:
            print(f"case <test number> FAIL: {repr(e)}")
            count += 1
```

TESTS:''' + tests
                }
            ],
            model="meta-llama-3-70b-instruct",
            max_tokens= 2048,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )
        x = json.dumps(completion.model_dump())
        load_x = json.loads(x)

        gen_func = load_x['choices'][0]['message']['content']
        #print(gen_func)
        print(name, input)
        f.write(gen_func)
        f.close()

for x in input:
    generate_code_tests(x)