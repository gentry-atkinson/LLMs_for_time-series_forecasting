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

def load_mhealth_samples():
    df = pd.read_csv(
        "data/MHEALTHDATASET/mHealth_subject1.log", 
        sep='\t',
        header=None,
        names=columns
    )
    print(df['acc_chest_y'].head())


if __name__ == '__main__':
    load_mhealth_samples()