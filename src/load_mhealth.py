import os

import numpy as np
import pandas as pd

data_dir = 'data'
dataset_dir = 'MHEALTHDATASET'
files = [
    'mHealth_subject1.log', 'mHealth_subject2.log', 'mHealth_subject3.log',
    'mHealth_subject4.log', 'mHealth_subject5.log', 'mHealth_subject6.log',
    'mHealth_subject7.log', 'mHealth_subject8.log', 'mHealth_subject9.log',
    'mHealth_subject10.log',
]

columns = [
    'acc_chest_x', 'acc_chest_y', 'acc_chest_z',
    'ecg_1', 'ecg_2',
    'acc_lankle_x', 'acc_lankle_y', 'acc_lankle_z',
    'gyro_lankle_x', 'gyro_lankle_y', 'gyro_lankle_z',
    'mag_lankle_x', 'mag_lankle_y', 'mag_lankle_z',
    'acc_rarm_x', 'acc_rarm_y', 'acc_rarm_z',
    'gyro_rarm_x', 'gyro_rarm_y', 'gyro_rarm_z',
    'mag_rarm_x', 'mag_rarm_y', 'mag_rarm_z',
    'label'
]

def load_mhealth_samples(logger=None, series_length=500, step=250):
    converted_array = None

    # For all subjects
    for set_num in range(1, 11):
        df = pd.read_csv(
            #f"data/MHEALTHDATASET/mHealth_subject{set_num}.log",
            os.path.join('data', 'MHEALTHDATASET', f"mHealth_subject{set_num}.log"),
            sep='\t',
            header=None,
            names=columns
        )
        if logger:
            logger.info(f"MHealth DataFrame {set_num} shape: {df.shape}")
        else:
            print(f"MHealth DataFrame {set_num} shape: {df.shape}")
        
        # Number channels * samples per original signal, series_length
        set_array = np.zeros(
            (df.shape[1] * ((df.shape[0]-series_length)//step), series_length),
            dtype=np.float16
        )
        # For every slice
        for idx, start in enumerate(range(0, df.shape[0]-series_length, step)):
            set_array[idx, :] = df[columns[idx%24]][start:start+series_length]
        # end for every slice
        if converted_array is None:
            converted_array = set_array
        else:
            converted_array = np.concat([converted_array, set_array])
    # end For all subjects

    np.random.shuffle(converted_array)

    if logger:
            logger.info(f"Final shape of converted MHealth array: {converted_array.shape}")
    else:
        print(f"Final shape of converted MHealth array: {converted_array.shape}")
        print(f"Max of converted arrar: {np.max(converted_array)}")
        print(f"Min of converted arrar: {np.min(converted_array)}")

    return converted_array
        

if __name__ == '__main__':
    load_mhealth_samples()