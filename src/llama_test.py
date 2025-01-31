from transformers import  pipeline
import torch
import os

# Use, consistent with MIT work

with open(os.path.join('src', 'token.txt')) as f:
    token = f.read().strip()

pipe = pipeline(
    task="text-generation", 
    model="meta-llama/Llama-3.3-70B-Instruct",
    tokenizer="meta-llama/Llama-3.3-70B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map='auto',
    token=token
)

print(pipe("Who are you?")[0])