import pandas as pd
from create_directory import create_dir_whith_file


def read_file_and_return_users():
    file_path = create_dir_whith_file()
    
    users = pd.read_csv(file_path).to_dict(orient='records')

    for user in users:
        user['news'] = []
        
    return users