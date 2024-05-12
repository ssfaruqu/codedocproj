import openai
from openai import OpenAI
import argparse
import re
import sys

sys.path.insert(0, "..\..\openai_testing")

import info.orig_info as oi 
import info.gen_info as gi

prompts = ['''
Write python code for just 10 small tests, without creating new functions, for a program with the following description, without any other text or use of ```. 
Wrap each individual test case in the following try-catch structure, without any other text or use of the ` character. No test should be longer than 5 lines,
and no string solution should be longer than 50 characters and no integer solution should be longer than 20 digits. Furthermore, do not include return statements.
Test code must include an assert statement, and must use only valid syntax:
```
<four whitespaces>try:
    <test code>
<four whitespaces>except Exception as e:
    print(f"{repr(e)} on test case <test number>")
    count += 1
```

''',
'''
Write python code for just 10 small tests, without creating new functions, for a program with the following description, without any other text or use of ```. 
Wrap each individual test case in the following try-catch structure, without any other text or use of the ` character. No test should be longer than 5 lines,
and no string solution should be longer than 50 characters and no integer solution should be longer than 20 digits. Furthermore, no test should return a value or None.
You must add an extra indent to each line, and do not include '```python ```', and test code must have an assert statement and must use only valid syntax:

<indent>try:
    <test code>
<indent>except Exception as e:
    print(f"{repr(e)} on test case <test number>")
    count += 1
    
'''
]

def generate_code_tests(input, llm, prompt, i):
    names = [oi.getFuncName()[i]]

    for name in names:
        # get summary
        r = open(llm+"/"+name+"/"+name+"_"+input+".txt", 'r')
        summary = r.read()
        r.close()

        f = open(llm+"/"+name+"/"+name+"_"+input+"_tests.py", "w")

        client = OpenAI()
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
            model=llm,
            max_tokens= 4096,
            presence_penalty=0,
            temperature=0.1,
            top_p=0.9,
        )
        tests = completion.choices[0].message.content
        print(name, input)
        f.write(tests)
        f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("llm", help="The LLM model to be used: gpt-3.5-turbo, gpt-4-turbo")
    parser.add_argument("func", help="Select function: 1-12")
    parser.add_argument("style", help="Select prompt style: 0= para_flat, 1= para_struc, 2= bullet_flat, 3= bullet_struc, 4= psuedo")
    args = parser.parse_args()
    llm = args.llm
    func = int(args.func) - 1
    style = int(args.style)

    if llm != "gpt-3.5-turbo" and llm != "gpt-4-turbo":
        print("Selected model not available: Use gpt-3.5-turbo or gpt-4-turbo")
        exit(0)
    if func not in range(0, 13):
        print("Selected invalid func")
        exit(0)
    if style not in range(0, 5):
        print("Selected invalid style")
        exit(0)

    gen_info = gi.GenInfo(llm)
    input = gen_info.getTestCaseNames()[style]

    if llm == "gpt-3.5-turbo":
        i = 0
    else:
        i = 1

    generate_code_tests(input, llm, prompts[i], func)