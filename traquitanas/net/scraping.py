"""

"""

import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def create_driver(
    download_path,
    headless=False,
    adds_path=os.path.join('..', 'adds'),
    log_path=os.path.join('..', 'logs'),
):
    """

    :param download_path: Pasta de download
    :param headless: True or False
    :param adds_path: dddd
    :param log_path: dddsdsdsd
    :return:
    :rtype: object
    """

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
    profile.set_preference(
        'browser.helperApps.neverAsk.saveToDisk',
        'application/octet-stream;application/vnd.ms-excel;text/html',
    )

    # profile.set_preference('browser.download.manager.showWhenStarting', False)
    # profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/vnd.google-earth.kml+xml,application/rar,application/pdf,application/vnd.ms-excel,application/octet-stream,application/msword,text/xml,text/kml,application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml,image/x-png,image/png,image/jpeg,text/plain,text/html,application/x-msdownload')
    # profile.set_preference('browser.helperApps.alwaysAsk.force', False)
    profile.set_preference('browser.aboutConfig.showWarning', False)
    # profile.set_preference('pdfjs.disabled', True)
    # profile.set_preference('print.print_headerright', '')
    # profile.set_preference('print.print_headercenter', '')
    # profile.set_preference('print.print_headerleft', '')
    # profile.set_preference('print.print_footerright', '')
    # profile.set_preference('print.print_footercenter', '')
    # profile.set_preference('print.print_footerleft', '')

    profile.update_preferences()

    # Driver Firefox com Options
    options = Options()
    options.headless = headless

    # Driver
    global driver
    driver = webdriver.Firefox(
        firefox_profile=profile,
        options=options,
        service_log_path=os.path.join(log_path, 'geckodriver.log'),
    )
    driver.install_addon(
        os.path.abspath(os.path.join(adds_path, 'xpath.xpi')), temporary=True
    )
    return driver


if __name__ == '__main__':
    pass
