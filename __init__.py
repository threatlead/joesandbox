from .joesandbox import JoeSandbox
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
