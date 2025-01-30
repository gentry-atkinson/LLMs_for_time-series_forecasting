from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import os

with open(os.path.join('src', 'token.txt')) as f:
    token = f.read().strip()

print(token)

# tokenizer = AutoTokenizer.from_pretrained(
#     "databricks/dbrx-instruct", 
#     token=token
# )

# model = AutoModelForCausalLM.from_pretrained(
#     "databricks/dbrx-instruct", 
#     device_map="auto", 
#     torch_dtype=torch.bfloat16, 
#     token=token
# )

# input_text = "What does it take to build a great LLM?"
# messages = [{"role": "user", "content": input_text}]
# input_ids = tokenizer.apply_chat_template(messages, return_dict=True, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")

# outputs = model.generate(**input_ids, max_new_tokens=200)
# print(tokenizer.decode(outputs[0]))

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="meta-llama/Llama-3.3-70B-Instruct", torch_dtype=torch.bfloat16, token=token, device="cuda")
output = pipe(messages)
print(output)