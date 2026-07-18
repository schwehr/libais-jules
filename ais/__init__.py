"""Bring the C++ extension into the ais namespace."""

from _ais import decode, DecodeError
from ais.io import open, NmeaFile
import logging

logging.basicConfig()

__all__ = ["decode", "DecodeError", "open", "NmeaFile"]

__license__ = "Apache 2.0"
__version__ = "0.17"
