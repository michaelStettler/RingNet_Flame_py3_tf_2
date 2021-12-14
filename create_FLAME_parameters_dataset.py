import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from config_AffectNet import get_config


def read_FLAME_parameters(path):
    params = np.load(path, allow_pickle=True)
    return params


if __name__ == '__main__':
    """
    run: python -m read_FLAME_parameters
    """
    config = get_config()

    df = pd.read_csv(os.path.join(config.AffectNet_path, config.csv_file))


    new_df = pd.DataFrame(columns=('subDirectory_filePath', 'expression', 'params'))
    for i in tqdm(range(len(df))):
    # for i in tqdm(range(5)):
        param_path = os.path.join(config.out_folder, 'params', df.at[i, 'subDirectory_filePath'] + '.npy')
        params = read_FLAME_parameters(param_path)
        entry_dict = {}
        entry_dict['subDirectory_filePath'] = df.at[i, 'subDirectory_filePath']
        entry_dict['expression'] = df.at[i, 'expression']
        entry_dict['params'] = params
        new_df = new_df.append(entry_dict, ignore_index=True)

    print("")
    print(new_df.head())

    new_df.to_csv(os.path.join(config.AffectNet_path, 'flame_params.csv'))