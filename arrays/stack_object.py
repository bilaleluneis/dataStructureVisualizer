__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from .abstract import AbstractArray
from typing import Optional


class Stack(object):

    def __init__(self, array: AbstractArray):
        self.__internal_array: AbstractArray = array

    @property
    def size(self):
        return self.__internal_array.size

    def __str__(self) -> str:
        description = str(self.__internal_array)
        replace_list = ["ArrayListImpl", "ArrayNodeImpl"]
        for _ in replace_list:
            description = description.replace(_, type(self).__name__)
        return description

    def push(self, value) -> None:
        self.__internal_array.insert(value)

    def pop(self) -> Optional[int]:
        return self.__internal_array.remove()

    def get(self, at_index) -> Optional[int]:
        return self.__internal_array.get(at_index)
