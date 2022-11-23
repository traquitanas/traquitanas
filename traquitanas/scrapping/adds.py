"""
_summary_

:return: _description_
:rtype: _type_
"""


import requests


def add_extension_xpath(my_driver, adds_path):
    """
    _summary_

    :param my_driver: _description_
    :type my_driver: _type_
    """

    # Add-ons Xpath
    xpath_path = adds_path / 'xpath.xpi'
    xpath_path = xpath_path.absolute().resolve()
    if not xpath_path.is_file():
        url = 'https://addons.mozilla.org/firefox/downloads/file/3588871/xpath_finder-1.0.2-fx.xpi'
        r = requests.get(url, timeout=60, verify=False)

        with open(xpath_path, 'wb') as f:
            f.write(r.content)

    # Add
    my_driver.install_addon(str(xpath_path), temporary=True)
    return my_driver


if __name__ == '__main__':
    pass
