Após testar diversas formas de usar o [**_Selenium_**](https://selenium-python.readthedocs.io/) e sua necessidade de instalação de componentes adicionais, optei por criar uma função com intuito de facilitar a criação de drivers em quaisquer ambientes (_Windows_ ou _Linux_).

Uma alternativa que pareceu interessante foi o [**_webdriver_manager_**](https://pypi.org/project/webdriver-manager/). Contudo, ainda assim, fazia-se necessário a indicação de um arquivo `.env` com o _GH_TOKEN_, possibilitando diversas _requests_ e... eu não estava disposto a utilizar essa variável de ambiente em todo projeto.

<br>

```python
from paths import driver_path, logs_path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from traquitanas.scrapping import gecko


# Gecko
gecko_path = gecko.get_path_geckodriver(driver_path)

# Logs
logs_filepath = logs_path / 'geckodriver.log'

# Services
service = FirefoxService(
  executable_path=gecko_path,
  log_path=logs_filepath
)

# Options
options = FirefoxOptions()
options.headless = False

# Create Driver
driver = webdriver.Firefox(service=service, options=options)
```
