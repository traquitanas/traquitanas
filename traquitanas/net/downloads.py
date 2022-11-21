"""
_summary_

:return: _description_
:rtype: _type_
"""

import os
import random
import time

import requests
from tqdm.notebook import tqdm, trange


def download_urls(urls, path, get_filename_from_url=True):
    """
    Function to download list of files with a progress bar.


    :param urls: Lista ou tuple, a depender da função #
    :param path: Local onde os arquivos serão inseridos
    :param get_filename_from_url: Se VERDADEIRO, a função irá nomear o arquivo conforme o link das lista das URLs.
    Se FALSO, a função irá nomear o arquivo conforme string definida no tuple das URLs
    """

    # Reset Interactions
    i = 0
    n_urls = len(urls)

    for n_url in trange(n_urls, desc='Total'):
        # Download path and file name
        if get_filename_from_url:
            url = urls[i]
            filename = urls[i].rsplit('/', 1)[1]
        else:
            url = urls[i][0]
            filename = urls[i][1]

        # File size
        r = requests.get(url, stream=True)
        chunk_size = 1024 * 1024
        total_size = int(r.headers['content-length'])

        # Download the file from 'url' and save it locally under 'filename'
        with open(os.path.join(path, filename), 'wb') as f:
            for data in tqdm(
                iterable=r.iter_content(chunk_size=chunk_size),
                total=int(total_size / chunk_size),
                unit='MB',
                desc=f'{i + 1}/{n_urls}',
            ):

                f.write(data)
                time.sleep(0.1)

        # Interactions
        i += 1

        # Definir um intervalo de tempo
        time.sleep(random.randint(3, 8))


def download_file_upper(url):
    """
    _summary_

    :param url: _description_
    :type url: _type_
    """
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        time.sleep(0.03)

        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


def download_file(url):
    """
    _summary_

    :param url: _description_
    :type url: _type_
    :return: _description_
    :rtype: _type_
    NOTE the stream=True parameter below
    """
    local_filename = url.split('/')[-1]
    with requests.get(url, timeout=60, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


if __name__ == '__main__':
    urls = [
        'https://sage.saude.gov.br/dados/sisagua/cadastro_pontos_captacao.zip',
        'https://sage.saude.gov.br/dados/sisagua/cadastro_tratamento_de_agua.zip',
        'https://sage.saude.gov.br/dados/sisagua/cadastro_populacao_abastecida.zip',
    ]

    path = os.path.abspath(os.path.join(os.getcwd(), '..', '..', '..', 'data'))
    print(path)

    download_urls(urls, path)
    # DownloadFile(urls[1])
    # download_file(urls[1])
