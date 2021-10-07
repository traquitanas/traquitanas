import random
import requests
from pycep_correios import get_address_from_cep, WebService



def ceps_bairros(estado='sp', municipio='piracicaba', loops=20):
    """
    Função que auxilia na definição de endereços aleatórios em uma cidade.

    :param estado: sigla da unidade da federação (default: "sp")
    :param municipio: nome do município (default: "piracicaba")
    :param loop: quanto maior o número de loops, maior a lista  (default: 20)
    :return: Output consiste em duas listas (list_ceps, list_bairros)
    """
    termos = [
        'rua', 'avenida', 'praça', 'bosque',  # Padrão
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro',
        'dezembro',  # Meses
        'marechal', 'sargento', 'duque', 'soldado', 'capitão', 'major',  # Patentes
        'dom', 'senhor', 'senhora',  # Pronomes de Tratamento
        'almeida', 'caetano', 'pedro', 'barbosa', 'rui', 'pinto', 'joão', 'são',  # Nomes
    ]
    i = 1
    list_ceps = []
    list_bairros = []
    while i <= loops:
        url = 'https://viacep.com.br/ws/{}/{}/{}/json/'.format(estado, municipio, random.choice(termos))
        resp = requests.get(url)
        json = resp.json()
        for data in json:
            list_ceps.append(data['cep'])
            list_bairros.append(data['bairro'])
        i += 1

    # CEPs
    list_ceps = list(set(list_ceps))
    list_ceps.sort()

    # Bairros
    list_bairros = list(set(list_bairros))
    list_bairros.sort()

    print(
        'Município: {}-{}\nCEPs distintos: {}\nBairros distintos: {}'.format(
            municipio.title(), estado.upper(),
            len(list_ceps),
            len(list_bairros)
        )
    )
    return list_ceps, list_bairros



if __name__ == '__main__':
    print('Fim')
