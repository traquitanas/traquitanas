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

<br>


Passado algum tempo, consegui herdar da classe `webdriver.Firefox`

```python
from paths import driver_path, logs_path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from traquitanas.scrapping import gecko


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
        gecko_path = gecko.get_path_geckodriver(
            my_driver_path,
            verify_ssl=kwargs['verify_ssl']
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
        adds.add_extension_xpath(self, my_adds_path)
```
