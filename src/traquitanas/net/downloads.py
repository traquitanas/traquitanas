import os
import time
import random
import requests
from tqdm.notebook import trange, tqdm


def download_urls(urls, path, get_filename_from_url=True):
    """
    Function to download list of files with a progress bar.

    #urls = ('http://sage.saude.gov.br/dados/sisagua/10Pontos_de_captacao_de_agua/10PontoCaptacao.zip',
    #        'http://sage.saude.gov.br/dados/sisagua/10Pontos_de_captacao_de_agua/10PontoCaptacao.zip')
    #path = os.path.join('home/michel/Geodata/Sourcecodes/case_sisgua', 'data', 'DadosOriginais')
    #download_urls(urls, path)

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
                desc=str(i + 1) + '/' + str(n_urls)
            ):
                f.write(data)

        # Interactions
        i = i + 1

        # Definir um intervalo de tempo
        time.sleep(random.randint(1, 3))
