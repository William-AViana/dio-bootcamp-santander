import pandas as pd

def read_and_return_users():
    users = pd.read_csv('clients.csv').to_dict(orient='records')

    for user in users:
        user['news'] = []
    return users