import random
import requests
from unicodedata import normalize


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
    ascii_name = normalize('NFKD', first_name).encode('ascii', errors='ignore').decode('ascii')
    ascii_name = ascii_name.lower()

    #
    url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}?sexo=F'.format(ascii_name)
    resp = requests.get(url)
    if resp.status_code == 200:
        json = resp.json()
        if len(json) > 0:
            n_feminino_ultimoperiodo = json[0]['res'][-1]['frequencia']
        else:
            n_feminino_ultimoperiodo = 0

    #
    url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{}?sexo=M'.format(ascii_name)
    resp = requests.get(url)
    if resp.status_code == 200:
        json = resp.json()
        if len(json) > 0:
            n_masculino_ultimoperiodo = json[0]['res'][-1]['frequencia']
        else:
            n_masculino_ultimoperiodo = 0

    try:
        calc = n_feminino_ultimoperiodo / (n_feminino_ultimoperiodo + n_masculino_ultimoperiodo)
    except Exception as e:
        print(e)
        calc = random.random()

    prob_limiar = (95 / 100)
    if calc > prob_limiar:
        sexo = 'Feminino'
        prob = calc
    else:
        sexo = 'Masculino'
        prob = 1 - calc

    print('"{}" é um nome "{}" com {}% de certeza'.format(first_name.title(), sexo, round(prob, 4) * 100))
    return sexo


if __name__ == '__main__':
    classify_name('Michel')
