# dio-bootcamp-santander
Bootcamp sobre ciência de dados com python

## Desafio: Criar um pipelinde de dados.
### Passos para criar uma pipeline simples.

* Criar uma conexão com uma API do mercado de criptomoedas.
* Extrair os dados de interesse (valor da criptomoeda).
* Criar uma lista de clientes.
* Transformar e enrriquecer os dados.
* Carregar os dados em formato JSON


## Descrição dos arquivos e suas funcinalidades:

- Para criar os diretórios "raw_data" e "processed_data", utilizamos a função ```create_dir_whith_file_csv()``` e ```processed_data()``` do arquivo ```create_directory.py```.

- Para gerar uma lista fictícia de clientes o arquivo ```generate_clients.py``` faz todo esse trabalho, chamando a função ```create_dir_whith_file_csv()``` para criar o diretório com o arquivo csv com os dados dos clientes.

- O arquivo ```extract.py``` faz a leitura do csv, extrai os dados e faz o tratamento do atributo "news" de cada usuário para transformar em uma lista.

- O arquivo ```get_criptos.py``` acessa uma API de valores de criptomoedas, neste caso estou consumindo e tratando os dados do valor do Bitcoin.

- O arquivo ```transform.py``` recebe os dados em csv dos clientes e o retorno da API de criptomoedas, para enrriquecer os dados dos clientes, utilizei a API do Gemini para enviar mensagens personalizadas sobre investimentos em Bitcoin e retornar os dados no formato JSON dentro da pasta ```processed_data```