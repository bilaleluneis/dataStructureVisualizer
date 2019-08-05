__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from persistence.abstract import AbstractPersistence
from persistence.memory import InMemoryPersistence

persistence: AbstractPersistence = InMemoryPersistence()
