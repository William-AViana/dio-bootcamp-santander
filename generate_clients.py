import pandas as pd
import random
import os
from extract_clients import read_and_return_users

def generate_clients_to_cvs():
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

    df.to_csv('clients.csv', index=False, encoding='utf-8')
    
    return read_and_return_users()
