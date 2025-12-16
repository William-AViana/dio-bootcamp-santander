import requests

# BTC ETH SOL
URL = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# For para cada cripto
response = requests.get(URL)
print(response.json())

#Extrair os dados de interesse

#criar um arquivo ou enviar para o banco de dados