__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from .abstract import AbstractArray, ArrayIndexOutOfBoundError
from typing import List, Type, SupportsInt, Optional


class ArrayListImpl(AbstractArray):

    def __init__(self) -> None:
        super().__init__()
        self.__internal_array: List[Type[int, SupportsInt]] = [int] * 0

    def __str__(self) -> str:
        description: str = "{} [".format(self._class_name)

        for entry in self.__internal_array:
            description += "{}, ".format(entry)

        if self.size > 0:
            description = description[:-2]  # remove last space and last ','

        description += "]"
        return description

    @property
    def size(self) -> int:
        array_size: int = 0
        for _ in self.__internal_array:
            array_size += 1
        return array_size

    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        if at_index < 0 or at_index >= self.size:
            return None  # index provided falls out of range of the array!
        else:
            get_value: Type[int, SupportsInt] = self.__internal_array[at_index]
            return int(get_value)  # return a copy of that value and not reference!

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        resolved_index: int

        if at_index is None:
            resolved_index = self.size - 1
        else:
            resolved_index = at_index

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:
            new_array: List[Type[int, SupportsInt]] = [int] * (self.size - 1)
            new_array_index: int = 0

            for index in range(self.size):
                if index != resolved_index:
                    new_array[new_array_index] = (int(self.__internal_array[index]))
                    new_array_index += 1

            del self.__internal_array
            self.__internal_array = new_array

        return value_at_index

    def set(self, value: int, at_index: int) -> None:
        if at_index < 0 or at_index >= self.size:
            class_name: str = self._class_name
            error: str = "{} _set[{}] = {} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)
        else:
            self.__internal_array[at_index] = int(value)  # make a copy and place in index of the array

    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        inserted_value: List[Type[int, SupportsInt]] = [int] * 1
        inserted_value[0] = int(value)
        if at_index is None:
            self.__internal_array += inserted_value
        elif at_index in range(0, self.size):
            left_array: List[Type[int, SupportsInt]] = list(self.__internal_array[:at_index])
            right_array: List[Type[int, SupportsInt]] = list(self.__internal_array[at_index:])
            del self.__internal_array
            self.__internal_array = left_array + inserted_value + right_array
        else:
            class_name: str = self._class_name
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)
