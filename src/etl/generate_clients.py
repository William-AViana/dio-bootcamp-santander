import pandas as pd
import random
from extract import read_file_and_return_users
from create_directory import create_dir_whith_file_csv


def generate_clients_to_cvs():
    directory = create_dir_whith_file_csv()
    
    names = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", 
        "Igor", "Juliana"
    ]

    data_list = []

    for i in range(1, 11):
        nome = names[i-1]
        
        record = {
            "id": i,
            "name": nome,
            "account_id": 1000 + i,
            "account_number": f"{random.randint(10000, 99999)}-{random.randint(0, 9)}",
            "account_agency": "0001",
            "account_balance": round(random.uniform(0, 5000), 2),
            "account_limit": 500.0,
            "card_id": 2000 + i,
            "card_number": f"**** **** **** {random.randint(1000, 9999)}",
            "card_limit": 1000.0 + (i * 100),
            "features": "Pix;Investimentos" if i % 2 == 0 else "Seguros",
            "news":""
        }
        
        data_list.append(record)
        
    df = pd.DataFrame(data_list)
    
    
    df.to_csv(directory, index=False, encoding='utf-8')
    
    return read_file_and_return_users()
