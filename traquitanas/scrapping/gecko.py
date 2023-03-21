"""
Equivalente ao Webdriver Project
Evita a necessidade de instalar drivers

https://github.com/mozilla/geckodriver/releases
out/22

Usei em:
- br_arisp
"""

import platform
import tarfile
import time
from pathlib import Path
from zipfile import ZipFile

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from .adds import add_extension_xpath


class Driver(webdriver.Firefox):
    """
    Cria driver customizado do Selenium

    :param webdriver: _description_
    :type webdriver: _type_
    """

    def __init__(self, my_driver_path, my_logs_path, *args, **kwargs):
        """

        verify_ssl

        :param my_driver_path: _description_
        :type my_driver_path: pathlib
        :param my_logs_path: _description_
        :type my_logs_path: pathlib
        """
        # Services
        gecko_path = get_path_geckodriver(
            my_driver_path, verify_ssl=kwargs['verify_ssl']
        )

        # Logs
        logs_filepath = my_logs_path / 'geckodriver.log'

        # Services
        my_service = FirefoxService(
            executable_path=gecko_path, log_path=logs_filepath
        )

        # Options
        my_options = FirefoxOptions()
        my_options.headless = False
        my_options.set_preference('intl.accept_languages', 'pt-BR, pt')

        # Driver
        my_driver = super(Driver, self)
        my_driver.__init__(service=my_service, options=my_options)

    def add_extension_xpath(self, my_adds_path):
        """
        Adiciona Xpath extension

        :param my_adds_path: Pasta da Extensão
        :type my_adds_path: pathlib
        """
        add_extension_xpath(self, my_adds_path)


def _check_geckodriver_exists(path):
    """
    _summary_

    :param path: _description_
    :type path: _type_
    :return: _description_
    :rtype: _type_
    """

    # Paths
    path.mkdir(exist_ok=True)
    gecko_win_filepath = path / 'geckodriver.exe'
    gecko_linux_filepath = path / 'geckodriver'

    if platform.system() == 'Windows':
        if gecko_win_filepath.is_file():
            return True

        elif not gecko_win_filepath.is_file():
            return False

    elif platform.system() == 'Linux':
        if gecko_linux_filepath.is_file():
            return True

        elif not gecko_linux_filepath.is_file():
            return False

    else:
        return None


def _get_geckodriver(path, verify_ssl=False):
    """
    Faz o download do geckodriver!
    TODO: Testar no windows!

    :param path:
    :return:
    """
    # Test
    has_geckodriver = _check_geckodriver_exists(path)

    # print(gecko_zip_filepath)
    if not has_geckodriver:
        if platform.system() == 'Windows':
            # Download do geckodriver
            url = 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win64.zip'
            r = requests.get(url, timeout=60, verify=verify_ssl)

            # Save
            gecko_zip_filepath = path / Path(url).name
            with open(gecko_zip_filepath, 'wb') as f:
                f.write(r.content)

            # Extract
            with ZipFile(gecko_zip_filepath, 'r') as zip_ref:
                zip_ref.extractall(path)

        elif platform.system() == 'Linux':
            # Download do geckodriver
            url = 'https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz'
            r = requests.get(url, timeout=60, verify=verify_ssl)

            # Save
            gecko_zip_filepath = path / Path(url).name
            with open(gecko_zip_filepath, 'wb') as f:
                f.write(r.content)

            # Extract
            with tarfile.open(gecko_zip_filepath, 'r') as tar_ref:
                tar_ref.extractall(path)

    elif has_geckodriver:
        #print(f'Geckodriver already in {path}')
        pass


def get_path_geckodriver(path, verify_ssl=False):
    """
    _summary_

    :param path: _description_
    :type path: _type_
    :return: _description_
    :rtype: _type_
    """
    # Faz download se for necessário
    _get_geckodriver(path, verify_ssl=verify_ssl)

    # Path
    if platform.system() == 'Windows':
        _gecko_path = path / 'geckodriver.exe'
        _gecko_path = _gecko_path.resolve().as_posix().replace('/', '\\')
        return _gecko_path

    elif platform.system() == 'Linux':
        _gecko_path = path / 'geckodriver'
        return _gecko_path

    else:
        print(f'Ajustar para plataforma {platform.system()}')
        return None


if __name__ == '__main__':
    # Imports
    import time
    from paths import driver_path, logs_path

    # Services
    gecko_path = get_path_geckodriver(driver_path)

    # Logs
    logs_filepath = logs_path / 'geckodriver.log'

    # Services
    service = FirefoxService(executable_path=gecko_path, log_path=logs_filepath)

    # Options
    options = FirefoxOptions()
    options.headless = False
    options.set_preference('intl.accept_languages', 'pt-BR, pt')

    # Driver
    driver = webdriver.Firefox(service=service, options=options)
    driver.get('https://github.com/SergeyPirogov/webdriver_manager')
    driver.maximize_window()

    # Close Connection
    time.sleep(4)
    driver.quit()

    # # Options
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # # https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/
    # options = webdriver.ChromeOptions()
    # #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # #options.add_experimental_option("useAutomationExtension", False)

    # # ddd
    # service = ChromeService(
    #     # executable_path=gecko_path
    # )
    # driver = webdriver.Chrome(service=service, options=options)
    # driver.get('https://github.com/SergeyPirogov/webdriver_manager')

    # # Close Connection
    # time.sleep(4)
    # driver.quit()

    # Message
    print('Driver close!!')
