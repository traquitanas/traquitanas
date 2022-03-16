import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver(download_path, headless=False, adds_path=os.path.join('..', 'adds'),
                  log_path=os.path.join('..', 'logs')):
    # Create directory
    os.makedirs(adds_path, exist_ok=True)
    os.makedirs(log_path, exist_ok=True)
    os.makedirs(download_path, exist_ok=True)

    # Xpath
    url = 'https://addons.mozilla.org/firefox/downloads/file/3588871/xpath_finder-1.0.2-fx.xpi'
    r = requests.get(url)
    with open(os.path.join(adds_path, 'xpath.xpi'), 'wb') as f:
        f.write(r.content)

        # Driver Firefox com Profile
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', 'pt-BR, pt')
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.dir', download_path)
    profile.set_preference('browser.download.manager.showWhenStarting', 'false')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                           'application/octet-stream;application/vnd.ms-excel;text/html')
    profile.update_preferences()

    # Driver Firefox com Options
    options = Options()
    options.headless = headless

    # Driver
    driver = webdriver.Firefox(
        firefox_profile=profile,
        options=options,
        service_log_path=os.path.join(log_path, 'geckodriver.log')
    )
    driver.install_addon(os.path.abspath(os.path.join(adds_path, 'xpath.xpi')), temporary=True)
    return driver
