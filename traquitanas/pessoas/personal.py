"""
Módulo com questões relacionadas ao nome das pessoas.


"""


import random
from unicodedata import normalize

import requests


def classify_name(name):
    """
    Retorna o gênero provável de um nome em "Masculino" "Feminino"
    Ideal para personalizar mensagens, mencionando um "Prezado" ou "Prezada", a depender do gênero.
    https://blog.brasil.io/2019/05/31/classificando-nomes-por-genero-usando-dados-publicos/index.html
    :param name: Nome que se deseja saber o gênero (ex: "Michel")
    :return: String "Masculino" "Feminino"
    """
    # Ajusta Nome
    first_name = name.split(' ')[0]
    ascii_name = (
        normalize('NFKD', first_name)
        .encode('ascii', errors='ignore')
        .decode('ascii')
    )
    ascii_name = ascii_name.lower()

    #
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{ascii_name}?sexo=F'
    resp = requests.get(url)
    if resp.status_code == 200:
        json = resp.json()
        if len(json) > 0:
            n_feminino_ultimoperiodo = json[0]['res'][-1]['frequencia']
        else:
            n_feminino_ultimoperiodo = 0

    #
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{ascii_name}?sexo=M'
    resp = requests.get(url, timeout=60)
    if resp.status_code == 200:
        json = resp.json()
        if len(json) > 0:
            n_masculino_ultimoperiodo = json[0]['res'][-1]['frequencia']
            
        else:
            n_masculino_ultimoperiodo = 0

    try:
        aa = n_feminino_ultimoperiodo + n_masculino_ultimoperiodo
        calc = n_feminino_ultimoperiodo / aa

    except Exception as e:
        print(e)
        calc = random.random()

    prob_limiar = 95 / 100
    if calc > prob_limiar:
        sexo = 'Feminino'
        prob = calc
    else:
        sexo = 'Masculino'
        prob = 1 - calc

    a = round(prob, 4) * 100
    print(f'"{first_name.title()}" é um nome "{sexo}" com {a} % de certeza')
    return sexo


if __name__ == '__main__':
    classify_name('Samile')
