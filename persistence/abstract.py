__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from abc import ABC, abstractmethod
from typing import TypeVar, Optional, Dict

T = TypeVar("T")


class AbstractPersistence(ABC):

    def __init__(self):
        pass

    @property
    def data(self) -> Optional[Dict[str, T]]:
        return self._retrieve()

    @data.setter
    def data(self, updated_data: Optional[Dict[str, T]]) -> None:
        self._persist(updated_data)

    @abstractmethod
    def _persist(self, data: Optional[Dict[str, T]]) -> None:
        pass

    @abstractmethod
    def _retrieve(self) -> Optional[Dict[str, T]]:
        pass
