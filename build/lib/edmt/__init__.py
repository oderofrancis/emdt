from .edmt import *

# check version

"""
Example 

import edmt
edmt.__version__

"""

from . import  _version

__version__ = _version.get_versions()["version"]