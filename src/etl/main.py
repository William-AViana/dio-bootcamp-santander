#importar os resultados de cada API
from generate_clients import generate_clients_to_cvs
import create_directory as cd

# all in function

users = generate_clients_to_cvs()



print(users)
# Criar um único data frame e enviar