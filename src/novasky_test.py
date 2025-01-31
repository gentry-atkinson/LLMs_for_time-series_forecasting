from transformers import pipeline
import torch
import os

# Is this Qwen? It thinks it is. Yes, "trained from"
# Use, lightweght and open

pipe = pipeline(
    task="text-generation", 
    model="NovaSky-AI/Sky-T1-32B-Flash",
    tokenizer="NovaSky-AI/Sky-T1-32B-Flash",
    torch_dtype=torch.bfloat16,
    device_map='auto' 
)
print(pipe("Who are you?")[0])