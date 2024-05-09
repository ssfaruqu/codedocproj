import openai
from openai import OpenAI
import re
import sys

sys.path.insert(0, "..\..\octoai_testing")

import info.orig_info as oi 
import info.gen_info as gi

names = oi.getFuncName()
input = gi.getTestCaseNames()

def generate_code_tests(input, llm):
    for name in names:
        # get summary
        r = open(name+"/"+name+"_"+input+".txt", 'r')
        summary = r.read()
        r.close()

        f = open(name+"/"+name+"_"+input+"_tests.py", "w")

        client = OpenAI()
        completion = client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": '''
Write python code for just 10 small tests, without creating new functions, for a program with the following description, without any other text or use of ```. 
Wrap each individual test case in the following try-catch structure, without any other text or use of the ` character. No test should be longer than 5 lines:
```
<four whitespaces>try:
    <test code>
<four whitespaces>except Exception as e:
    print(f"{repr(e)} on test case <test number>")
    count += 1
```

TESTS:\n''' + summary
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
    llm = sys.argv[1]
    for x in input:
        generate_code_tests(x, llm)