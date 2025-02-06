import numpy as np
from datasets import load_dataset

def load_monash_weather(logger=None, series_length=200, step=100):
    ds = load_dataset('Monash-University/monash_tsf', 'weather')

    converted_array = None
    for series in ds['train']['target']:
        set_array = np.zeros(((len(series)-series_length)//step, series_length))

if __name__ == "__main__":
    load_monash_weather()