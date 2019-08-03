from __future__ import annotations

__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from .abstract import AbstractArray, ArrayIndexOutOfBoundError
from typing import TypeVar, SupportsInt, Optional

# Type is of or subtype of int, bool
T = TypeVar("T", int, bool, SupportsInt)


class InvalidTypeError(Exception):
    pass


class Node:
    def __init__(self, uid: int, a_value: T) -> None:
        self.__uid: Optional[int] = None
        self.__value: Optional[T] = None
        self.__child_node: Optional[Node] = None
        self.value = a_value
        self.id = uid

    def __repr__(self) -> str:
        return "Node(id={}, value={})".format(self.id, self.value)

    @property
    def value(self) -> T:
        if type(self.__value) is int:
            return int(self.__value)
        else:  # must be a boolean type
            return bool(self.__value)

    @value.setter
    def value(self, new_value: T) -> None:
        if type(new_value) is int:
            self.__value = int(new_value)
        elif type(new_value) is bool:
            self.__value = bool(new_value)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def id(self) -> int:
        return int(self.__uid)

    @id.setter
    def id(self, new_id: int) -> None:
        if type(new_id) is int:
            self.__uid = int(new_id)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def child(self) -> Optional[Node]:
        return self.__child_node

    @child.setter
    def child(self, node: Optional[Node]) -> None:
        if node is None:
            self.__child_node = None
        else:
            self.__child_node = Node(node.id, node.value)


class ArrayNodeImpl(AbstractArray):

    def __init__(self) -> None:
        super().__init__()
        self.__node: Optional[Node] = None

    def __str__(self) -> str:
        description: str = "{} [".format(self._class_name)

        if self.size > 0:
            for i in range(self.size):
                current_value = self.get(i)
                description += "{}, ".format(current_value)

            description = description[:-2]
        description += "]"

        return description

    @property
    def size(self) -> int:
        return self.__offspring_counter(self.__node)

    def get(self, at_index: int) -> Optional[int]:
        if at_index < 0 or at_index >= self.size:
            return None
        else:
            return self.__get_node(at_index).value

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index = self.size - 1

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:  # if the node does exist
            node_to_remove = self.__get_node(resolved_index)
            last_node = self.__find_last_node()
            second_to_last_node = self.__get_parent_node(last_node.id)
            node_to_remove.id = last_node.id
            node_to_remove.value = last_node.value
            if second_to_last_node is None:  # if there's only one node
                self.__node = None
            else:
                second_to_last_node.child = None
                self.__shift_id(resolved_index+1, -1)

        return value_at_index

    def set(self, value: int, at_index: int) -> None:
        node_to_set = self.__get_node(at_index)
        if node_to_set is not None:
            node_to_set.value = value

    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index: int = int(self.size)

        if resolved_index in range(self.size+1):  # if index = size, put it at the end.
            self.__shift_id(resolved_index, 1)
            last_node: Node = self.__find_last_node()
            if last_node is None:  # if the array is empty
                self.__node: Node = Node(resolved_index, value)  # resolved_index can only be 0 if array is empty
            else:
                last_node.child = Node(resolved_index, value)
        else:
            class_name: str = self._class_name
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)

    """ utility methods """

    def __get_node(self, at_index: int) -> Optional[Node]:
        root_node = self.__node
        while root_node is not None:
            if root_node.id == at_index:
                return root_node
            else:
                root_node = root_node.child
        return root_node

    def __get_parent_node(self, at_index: int) -> Optional[Node]:
        root_node: Node = self.__node
        if root_node.id == at_index:
            return None
        else:
            while root_node is not None and root_node.child is not None:
                if root_node.child.id == at_index:
                    return root_node
                else:
                    root_node = root_node.child

    # def __get_parent_node_2(self):

    def __offspring_counter(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        else:
            return self.__offspring_counter(node.child) + 1

    def __shift_id(self, from_index: int, number: int) -> None:
        root_node = self.__node
        while root_node is not None:
            if root_node.id >= from_index:
                root_node.id += number
            root_node = root_node.child

    def __find_last_node(self) -> Optional[Node]:
        root_node: Optional[Node] = self.__node
        if root_node is None:
            return None
        else:
            while root_node.child is not None:
                root_node = root_node.child
            return root_node

