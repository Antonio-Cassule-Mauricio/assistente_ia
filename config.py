
import os
from dotenv import load_dotenv

load_dotenv()

QWEN_API_KEY = os.getenv("QWEN_API_KEY")

if not QWEN_API_KEY:
    raise ValueError("Chave Qwen API não encontrada!")

print("Configuração Qwen do NEXA carregada!")
