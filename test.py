import torch
from transformers.pipelines import pipeline

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
    {"role": "user", "content": "Do you have mayonnaise recipes?"}
]

chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3", torch_dtype=torch.bfloat16, device=0)
chatbot(messages)