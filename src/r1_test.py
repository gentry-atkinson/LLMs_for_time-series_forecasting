from transformers import pipeline
import torch
import os

# Exclude, commonly experiences bugs

pipe = pipeline(
    task="text-generation", 
    model="deepseek-ai/DeepSeek-R1",
    tokenizer="deepseek-ai/DeepSeek-R1",
    torch_dtype=torch.bfloat16,
    device_map='auto'
)

print(pipe("Who are you?")[0]['generated_text'])