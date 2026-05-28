"""""
#arquivo com as ferramentas de comunicaçao com apis
"""""

import requests

def buscar_cep(cep: str) -> dict:
    """""
    a funçao recebe o cep,consulta uma api e devolve informaçoes sobre o cep
    """""
    resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    return resposta.json()

print(buscar_cep("06501115"))