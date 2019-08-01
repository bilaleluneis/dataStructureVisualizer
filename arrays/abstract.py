__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from abc import ABC, abstractmethod
from typing import Optional


class ArrayIndexOutOfBoundError(Exception):
    pass


class AbstractArray(ABC):

    def __init__(self) -> None:
        self._class_name: str = type(self).__name__

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        pass

    @abstractmethod
    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        pass

    @abstractmethod
    def set(self, value: int, at_index: int) -> None:
        pass

    @abstractmethod
    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        pass
