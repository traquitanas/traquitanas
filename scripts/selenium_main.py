"""
Testes e Erro
"""

import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from traquitanas.scrapping import gecko # To Download Gecko Driver and Get Path to Gecko

# Base Path
project_path = Path(__file__).absolute().parents[1]
print(project_path)

# Create Paths
scrapy_path = project_path / 'scrapy'
scrapy_path.mkdir(exist_ok=True)

driver_path = scrapy_path / 'driver'
driver_path.mkdir(exist_ok=True)

logs_path = scrapy_path / 'logs'
logs_path.mkdir(exist_ok=True)

adds_path = scrapy_path / 'adds'
adds_path.mkdir(exist_ok=True)


# Set Class
class Driver:
    def __init__(self, driver_path, logs_path):
        # Services
        service = FirefoxService(
            executable_path=gecko.get_path_geckodriver(
                driver_path, verify_ssl=True
            ),
            log_path=logs_path / 'geckodriver.log',
        )

        # Driver
        self._driver = webdriver.Firefox(service=service)

    def login(self, url):
        # Get URL
        self._driver.get(url)

    def fechar(self):
        self._driver.quit()


# Classe
page = Driver(driver_path, logs_path)
page.login('https://github.com/')

# Do Something

# Close Connection
time.sleep(2)
page.fechar()
