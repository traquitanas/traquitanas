"""
Funções
"""

import hashlib
import os
import os.path
from pathlib import Path

import click
import requests
from tqdm import tqdm

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

URL_BASE = 'http://www.patentsview.org/data'
"""str: Base url for PatentsView. Just to reduce url length."""

URLS = [
    f'{URL_BASE}/20171226/botanic.tsv.zip',
    f'{URL_BASE}/20171226/cpc_subsection.tsv.zip',
]
"""List: Contains urls of files which need to be downloaded.
Make sure that you add a hash in the same position in ``HASHES`` so that the
integrity of the file can be verified. The hash has to be a lowercase sha265.
The has can be computed in Powershell with ``Get-FileHash <file>``. Notice
that Powershell returns uppercase letters and Python lowercase."""

HASHES = [
    '94c642405619b20ecaf657b30e84bab787320649e751ed6ac629c0be613ded44',
    '8437a94cf0c777486a10f77df89749a4278c6dbc69ff6bc62c2dd01b515a84f4',
]
"""List: Contains sha265 hashes calculated for the files in ``URLS``."""

DOWNLOAD_FOLDER = Path('.')
"""pathlib.Path: Points to the target directory of downloads."""


def downloader(position: int, resume_byte_pos: int = None):
    """Download url in ``URLS[position]`` to disk with possible resumption.
    Parameters
    ----------
    position: int
        Position of url.
    resume_byte_pos: int
        Position of byte from where to resume the download
    """
    # Get size of file
    url = URLS[position]
    r = requests.head(url)
    file_size = int(r.headers.get('content-length', 0))

    # Append information to resume download at specific byte position
    # to header
    resume_header = (
        {'Range': f'bytes={resume_byte_pos}-'} if resume_byte_pos else None
    )

    # Establish connection
    r = requests.get(url, stream=True, headers=resume_header)

    # Set configuration
    block_size = 1024
    initial_pos = resume_byte_pos if resume_byte_pos else 0
    mode = 'ab' if resume_byte_pos else 'wb'
    file = DOWNLOAD_FOLDER / url.split('/')[-1]

    with open(file, mode) as f:
        with tqdm(
            total=file_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            desc=file.name,
            initial=initial_pos,
            ascii=True,
            miniters=1,
        ) as pbar:
            for chunk in r.iter_content(32 * block_size):
                f.write(chunk)
                pbar.update(len(chunk))


def download_file(position: int) -> None:
    """Execute the correct download operation.
    Depending on the size of the file online and offline, resume the
    download if the file offline is smaller than online.
    Parameters
    ----------
    position: int
        Position of url.
    """
    # Establish connection to header of file
    url = URLS[position]
    r = requests.head(url)

    # Get filesize of online and offline file
    file_size_online = int(r.headers.get('content-length', 0))
    file = DOWNLOAD_FOLDER / url.split('/')[-1]

    if file.exists():
        file_size_offline = file.stat().st_size

        if file_size_online != file_size_offline:
            click.echo(f'File {file} is incomplete. Resume download.')
            downloader(position, file_size_offline)
        else:
            click.echo(f'File {file} is complete. Skip download.')
            pass
    else:
        click.echo(f'File {file} does not exist. Start download.')
        downloader(position)


def validate_file(position: int) -> None:
    """Validate a given file with its hash.
    The downloaded file is hashed and compared to a pre-registered
    has value to validate the download procedure.
    Parameters
    ----------
    position: int
        Position of url and hash.
    """
    file = DOWNLOAD_FOLDER / URLS[position].split('/')[-1]
    try:
        hash = HASHES[position]
    except IndexError:
        click.echo(f'File {file.name} has no hash.')
        return 0

    sha = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(1000 * 1000)  # 1MB so that memory is not exhausted
            if not chunk:
                break
            sha.update(chunk)
    try:
        assert sha.hexdigest() == hash
    except AssertionError:
        file = URLS[position].split("/")[-1]
        click.echo(
            f'File {file} is corrupt. '
            'Delete it manually and restart the program.'
        )
    else:
        click.echo(f'File {file} is validated.')


@click.group(context_settings=CONTEXT_SETTINGS, chain=True)
def cli():
    """Program for downloading and validating files.

    It is possible to run both operations consecutively with

    .. code-block:: shell

        $ python python-downloader.py download validate
    To download a file, add the link to ``URLS`` and its hash to ``HASHES`` if
    you want to validate downloaded files.
    """
    pass


@cli.command()
def download():
    """Download files specified in ``URLS``."""
    click.echo('\n### Start downloading required files.\n')
    for position in range(len(URLS)):
        download_file(position)
    click.echo('\n### End\n')


@cli.command()
def validate():
    """Validate downloads with hashes in ``HASHES``."""
    click.echo('### Start validating required files.\n')
    for position in range(len(URLS)):
        validate_file(position)
    click.echo('\n### End\n')


if __name__ == '__main__':
    # cli()
    URLS = [
        'https://sage.saude.gov.br/dados/sisagua/cadastro_pontos_captacao.zip'
    ]
    # position = 0
    # downloader(position, resume_byte_pos=200000)

    url = URLS[0]
    download_path = os.path.join('.')

    def downloader2(url, resume_byte_pos: int = None):
        """

        :rtype: object
        """
        r = requests.head(url)
        file_size = int(r.headers.get('content-length', 0))

        # Append information to resume download at specific byte position
        # to header
        resume_header = (
            {'Range': f'bytes={resume_byte_pos}-'} if resume_byte_pos else None
        )

        # Establish connection
        r = requests.get(url, stream=True, headers=resume_header)

        # Set configuration
        block_size = 1024
        initial_pos = resume_byte_pos if resume_byte_pos else 0
        mode = 'ab' if resume_byte_pos else 'wb'
        file = DOWNLOAD_FOLDER / url.split('/')[-1]

        with open(file, mode) as f:
            with tqdm(
                total=file_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc=file.name,
                initial=initial_pos,
                ascii=True,
                miniters=1,
            ) as pbar:
                for chunk in r.iter_content(32 * block_size):
                    f.write(chunk)
                    pbar.update(len(chunk))

    # ---------------------------------------------------------------

    r = requests.head(url)

    # Get filesize of online and offline file
    file_size_online = int(r.headers.get('content-length', 0))
    print(file_size_online)

    filename = os.path.basename(url)
    filepath = os.path.join(download_path, filename)

    if os.path.isfile(filepath):
        file_size_offline = os.stat(filepath).st_size

        # Se o tamanho for diferente
        if file_size_online != file_size_offline:
            print(f'File {filename} is incomplete. Resume download.')
            downloader2(url, file_size_offline)
        else:
            print(f'File {filename} is complete. Skip download.')
            pass
    else:
        # Download
        downloader2(url)
        pass
