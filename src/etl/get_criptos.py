import requests
import locale
from datetime import datetime
import pandas as pd

URL = 'https://api.coinbase.com/v2/prices/BTC-BRL/spot'

response = requests.get(URL)

data = response.json()

#transform data on object and extract informations
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
result_price = float(data['data']['amount'])
df = pd.DataFrame([{
    'Ativo': data['data']['base'],
    'Moeda': data['data']['currency'],
    'Preço': locale.currency(result_price, grouping=True),
    'Data': datetime.now().strftime("%d-%M-%Y %H:%M")
    }])


print(df)

#create file or send informationsfrom database