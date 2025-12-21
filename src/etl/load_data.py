import pandas as pd
from pathlib import Path
from etl.transform import trasform_data
from create_directory import processed_data

def load_data():
    datas = trasform_data()
    df = pd.DataFrame(datas)
    
    directory = processed_data()
    
    df.to_json(directory, orient='records', date_format='iso', indent=4)
    