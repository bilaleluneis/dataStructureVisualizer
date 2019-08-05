__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Optional, Dict
from persistence.abstract import T
from .abstract import AbstractPersistence
from json import dump, load
from pathlib import Path


class JsonFilePersistence(AbstractPersistence):

    def __init__(self):
        super().__init__()
        self.__file_name: str = str(Path.home()) + "/persistence.json"

    def _persist(self, data: Optional[Dict[str, T]]) -> None:
        with open(self.__file_name, "w") as persistence:
            dump(data, persistence, indent=4)

    def _retrieve(self) -> Optional[Dict[str, T]]:
        if not Path(self.__file_name).exists():
            return None
        with open(self.__file_name) as persistence:
            data: Optional[Dict[str, T]] = load(persistence)
            return data
