from codecs import open  # To use a consistent encoding
from os import path

__all__ = ['version', '__version__']

here = path.abspath(path.dirname(__file__))

# Get the version number from the relevant file
with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read()

__version__ = version