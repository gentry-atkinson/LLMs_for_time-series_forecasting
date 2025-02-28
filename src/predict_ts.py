import numpy as np
from transformers import pipeline
import torch

MODEL_LIST = [
    "NovaSky-AI/Sky-T1-32B-Flash",
    "meta-llama/Llama-3.3-70B-Instruct"
]

def stringify_series(series: np.ndarray, precision=2, masked_pos=None) -> str:
    formatted_elements = [0] * len(series)
    for i, num in enumerate(series):
        truncated_num = int(num * 10**precision) / float(10**precision)
        str_num = str(truncated_num).replace('.', '')
        formatted_elements[i] = (str_num)

    if masked_pos:
        formatted_elements[masked_pos] = '_'
    return ", ".join(formatted_elements)


def predict_pos_n(model_name: str, X: np.ndarray, pos: int, precision=2) -> np.ndarray:
    assert model_name in MODEL_LIST, "Not a supported model"
    pipe = pipeline(
        task="text-generation", 
        model="NovaSky-AI/Sky-T1-32B-Flash",
        tokenizer="NovaSky-AI/Sky-T1-32B-Flash",
        torch_dtype=torch.bfloat16,
        device_map='auto' 
    )

    for sample in X:
        masked_sample = stringify_series(sample, precision, -1)
        pred = pipe(f"Print only the missing number in this series, indicated with _: {masked_sample}")
        print(pred)


if __name__ == '__main__':
    from load_random_walks import load_random_walks
    from load_monash import load_monash_weather, load_monash_tourism_monthly

    X = load_monash_tourism_monthly()
    pred_values = predict_pos_n("NovaSky-AI/Sky-T1-32B-Flash", X, -1, 2)