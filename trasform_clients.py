import os
from dotenv import load_dotenv
from google import genai

load_dotenv() # Carrega as variáveis do arquivo .env

# Agora o SDK ou seu código pode acessar a variável
#api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)