# -*- coding: utf-8 -*-

__title__ = 'pywebtask'
__version__ = '0.1.3'
__build__ = 0x000103
__author__ = 'Sebastián José Seba'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Sebastián José Seba'


from .webtasks import run, run_file

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
