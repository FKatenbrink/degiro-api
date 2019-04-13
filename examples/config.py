import os
from logging.config import fileConfig
fileConfig('examples/logging_config.ini')

DEGIRO_USERNAME = os.getenv('DEGIRO_USERNAME', '<SECRET>')
DEGIRO_PASSWORD = os.getenv('DEGIRO_PASSWORD', '<SECRET>')
