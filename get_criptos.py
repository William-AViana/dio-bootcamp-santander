import requests
import locale
from datetime import datetime


URL = 'https://api.coinbase.com/v2/prices/BTC-BRL/spot'

response = requests.get(URL)

data = response.json()

#transform data on object and extract informations
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data_and_hour = datetime.now().strftime("%d-%M-%Y %H:%M")
base = data['data']['base']
result_price = float(data['data']['amount'])
price_format = locale.currency(result_price, grouping=True)
currency = data['data']['currency']

print(base, currency, price_format, data_and_hour)

#create file or send informationsfrom database