from dotenv import load_dotenv
import os

load_dotenv()

def minha_chave() -> str:
    chave = os.getenv("CHAVE_API")
    if not chave:
        raise ValueError("API_KEY não encontrada no arquivo .env.")
    return chave