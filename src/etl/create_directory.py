from pathlib import Path


def create_dir_whith_file():
    source = Path("raw_data")
    source.mkdir(parents=True, exist_ok=True)
    
    folder_path = source / 'clients.csv'
    return folder_path
