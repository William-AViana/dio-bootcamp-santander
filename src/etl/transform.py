import os
import random
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from generate_clients import generate_clients_to_cvs
from get_criptos import get_bitcoin


def trasform_data():
    
    users = generate_clients_to_cvs()
    bitcoin_value = get_bitcoin()

    load_dotenv()
    client = genai.Client(api_key=os.getenv("API_KEY"))
    
    for user in users:

        response = client.models.generate_content(
           model="gemini-2.5-flash-lite", 
           contents=f"Crie uma mensagem para {user['name']} sobre a importância \
               dos investimentos em criptomoedas, baseado no valor atualdo bitcoin \
               {bitcoin_value}.(máximo de 100 caracteres)",
           config=types.GenerateContentConfig(
               system_instruction=
               "Você é um especialista em marketing com experiência em conquistar \
                   novos investidores para o setor bancário, focado em criptomoedas",
               thinking_config=types.ThinkingConfig(thinking_budget=0)
           ),
       )
        
        user["news"].append({
            "id": f"{random.randint(1, 10000)}",
            "description": f"{response.text}"
            })
        time.sleep(60)
        
    return users