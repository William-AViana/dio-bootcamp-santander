from pathlib import Path


def create_dir_whith_file_csv():
    source_data = Path("raw_data")
    source_data.mkdir(parents=True, exist_ok=True)

    
    folder_path = source_data / 'clients.csv'
    return folder_path

def processed_data():
    source_load = Path("processed_data")
    source_load.mkdir(parents=True, exist_ok=True)
    
    folder = source_load / 'data_clients.json'
    
    return folder