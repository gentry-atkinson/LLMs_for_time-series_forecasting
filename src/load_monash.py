import multiprocessing

import numpy as np
from datasets import load_dataset


def process_series(series, series_length, step):
    """Processes a single time series."""
    set_array = np.zeros((((len(series) - series_length) // step) + 1, series_length))
    for i, start in enumerate(range(0, len(series) - series_length, step)):
        set_array[i] = series[start:start + series_length]
    return set_array


def load_monash_weather(logger=None, series_length=200, step=100, num_processes=None):
    ds = load_dataset('Monash-University/monash_tsf', 'weather')
    series_list = ds['train']['target']  # Get the list of series

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()  # Use all available cores by default

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(process_series, [(series, series_length, step) for series in series_list])

    converted_array = np.concatenate(results) # Efficient concatenation

    if logger:
        logger.info(f"Final shape of converted Monash Weather array: {converted_array.shape}")
    else:
        print(f"Final shape of converted Monash Weather array: {converted_array.shape}")
        print(f"Max of converted array: {np.max(converted_array)}")
        print(f"Min of converted array: {np.min(converted_array)}")

    return converted_array # Return the array


def load_monash_tourism_monthly(logger=None, series_length=24, step=12, num_processes=None):
    ds = load_dataset('Monash-University/monash_tsf', 'tourism_monthly')
    series_list = ds['train']['target']  # Get the list of series

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()  # Use all available cores by default

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(process_series, [(series, series_length, step) for series in series_list])

    converted_array = np.concatenate(results) # Efficient concatenation

    if logger:
            logger.info(f"Final shape of converted Yearly Tourism array: {converted_array.shape}")
    else:
        print(f"Final shape of converted Yearly Tourism array: {converted_array.shape}")
        print(f"Max of converted arrar: {np.max(converted_array)}")
        print(f"Min of converted arrar: {np.min(converted_array)}")

if __name__ == "__main__":
    X = load_monash_tourism_monthly()