__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Optional, Dict
from persistence.abstract import T
from .abstract import AbstractPersistence


class InMemoryPersistence(AbstractPersistence):

    def __init__(self):
        super().__init__()
        self.__data_in_memory: Optional[Dict[str, T]] = None

    def _persist(self, data: Optional[Dict[str, T]]) -> None:
        self.__data_in_memory = data

    def _retrieve(self) -> Optional[Dict[str, T]]:
        return self.__data_in_memory
