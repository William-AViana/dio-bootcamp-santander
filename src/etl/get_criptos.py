import requests
import locale
from datetime import datetime
import pandas as pd

def get_bitcoin():
    URL = 'https://api.coinbase.com/v2/prices/BTC-BRL/spot'

    response = requests.get(URL)

    data = response.json()

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    result_price = float(data['data']['amount'])
    df = pd.DataFrame([{
        'ativo': data['data']['base'],
        'moeda': data['data']['currency'],
        'preco': locale.currency(result_price, grouping=True),
        'data': datetime.now().strftime("%d-%M-%Y %H:%M")
        }])
    
    return df['preco'][0]
