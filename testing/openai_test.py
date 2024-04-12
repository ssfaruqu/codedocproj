import openai
import argparse
import tree_sitter
import datasets
from datasets import load_dataset
from tree_sitter import Language, Parser

# Language.build_library('/tmp/sqlite.so', ['/tmp/tree-sitter-sqlite'])
# language = Language('/tmp/sqlite.so', 'sqlite')
# parser = Parser()
# parser.set_language(language)
# sql = b"""CREATE TABLE _datasette_auth_tokens (
#    id INTEGER PRIMARY KEY,
#    secret TEXT,
#    description TEXT,
#    permissions TEXT,
#    actor_id TEXT,
#    created_timestamp INTEGER,
#    last_used_timestamp INTEGER,
#    expires_after_seconds INTEGER
# );"""
# tree = parser.parse(sql)
# print(tree.root_node.sexp())

ds = load_dataset("shailja/Verilog_GitHub", streaming=True, split="train")
print(next(iter(ds))['text'])

f = open("OpenAI_API_key.txt", "r") 
openai.my_api_key = f.readline()
f.close()

messages = [ {"role": "system", 
              "content": "You provide code documentation to the code submitted."
              } ]

#while True: 
message = "User: " + next(iter(ds))['text'] #input("User : ") 
if message: 
	messages.append( 
		{"role": "user", "content": message}, 
	) 
	chat = openai.ChatCompletion.create( 
		model="gpt-3.5-turbo", messages=messages 
	) 
reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}") 
messages.append({"role": "assistant", "content": reply}) 
