"""
Used when import all
Example: from traquitanas import *

https://stackoverflow.com/questions/4902974/python-import-subpackage-from-a-package-not-working

"""

from traquitanas.net import downloads
from traquitanas.scrapping import adds, gecko, scrapping

# from traquitanas import scrapping

# Net
__all__ = ['downloads', 'scrapping', 'gecko', 'adds']
